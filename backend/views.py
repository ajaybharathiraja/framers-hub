from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import FarmerRegistrationForm, CustomerRegistrationForm

def register_farmer(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            from .models import ResearchEvent
            ResearchEvent.objects.create(user=user, event_type='USER_REGISTERED', metadata={'role': 'farmer'})
            login(request, user)
            return redirect('farmer_dashboard')
    else:
        form = FarmerRegistrationForm()
    return render(request, 'backend/register_farmer.html', {'form': form})

def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            from .models import ResearchEvent
            ResearchEvent.objects.create(user=user, event_type='USER_REGISTERED', metadata={'role': 'customer'})
            login(request, user)
            return redirect('customer_dashboard')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'backend/register_customer.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            from .models import ResearchEvent
            ResearchEvent.objects.create(user=user, event_type='LOGIN')
            if user.role == 'farmer':
                return redirect('farmer_dashboard')
            elif user.role == 'customer':
                return redirect('customer_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'backend/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

from django.db.models import Sum, Count, Avg
from django.utils import timezone
from datetime import timedelta

@login_required
def farmer_dashboard(request):
    if request.user.role != 'farmer':
        return redirect('customer_dashboard')
        
    farmer = request.user.farmer_profile
    
    # 1. Total Income (sum of actual completed farmer sales)
    # Using 'CONFIRMED' and 'DELIVERED' as successful states
    successful_orders = OrderItem.objects.filter(
        listing__product__farmer=farmer,
        order__status__in=['CONFIRMED', 'PROCESSING', 'READY/SHIPPED', 'DELIVERED']
    )
    
    total_income = sum(item.quantity * item.price_at_sale for item in successful_orders) or Decimal('0.00')
    total_sales = successful_orders.count()
    
    # Active Products
    active_products = Listing.objects.filter(product__farmer=farmer, is_active=True).count()
    
    # Inventory
    total_inventory = Inventory.objects.filter(product__farmer=farmer).aggregate(
        total=Sum('available_quantity')
    )['total'] or Decimal('0.00')
    
    # Average Selling Price
    avg_price = successful_orders.aggregate(avg=Avg('price_at_sale'))['avg'] or Decimal('0.00')
    
    # Daily, Weekly, Monthly Income
    now = timezone.now()
    daily_orders = successful_orders.filter(order__created_at__date=now.date())
    weekly_orders = successful_orders.filter(order__created_at__gte=now - timedelta(days=7))
    monthly_orders = successful_orders.filter(order__created_at__gte=now - timedelta(days=30))
    
    daily_income = sum(item.quantity * item.price_at_sale for item in daily_orders) or Decimal('0.00')
    weekly_income = sum(item.quantity * item.price_at_sale for item in weekly_orders) or Decimal('0.00')
    monthly_income = sum(item.quantity * item.price_at_sale for item in monthly_orders) or Decimal('0.00')
    
    context = {
        'total_income': total_income,
        'total_sales': total_sales,
        'active_products': active_products,
        'total_inventory': total_inventory,
        'avg_price': avg_price,
        'daily_income': daily_income,
        'weekly_income': weekly_income,
        'monthly_income': monthly_income,
    }
    
    return render(request, 'backend/farmer_dashboard.html', context)

@login_required
def customer_dashboard(request):
    if request.user.role != 'customer':
        return redirect('farmer_dashboard')
        
    customer = request.user.customer_profile
    
    from .models import Order, Listing, CartItem
    from django.db.models import Sum
    
    orders = Order.objects.filter(customer=customer)
    total_orders = orders.count()
    total_spent = orders.aggregate(total=Sum('total_amount'))['total'] or 0
    
    recent_orders = orders.order_by('-created_at')[:3]
    
    cart_items_count = CartItem.objects.filter(cart__customer=customer).aggregate(total=Sum('quantity'))['total'] or 0
    
    # Simple randomized approach for featured products
    featured_products = Listing.objects.filter(is_active=True).order_by('?')[:4]
    
    context = {
        'total_orders': total_orders,
        'total_spent': total_spent,
        'recent_orders': recent_orders,
        'cart_items_count': cart_items_count,
        'featured_products': featured_products,
    }
    
    return render(request, 'backend/customer_dashboard.html', context)

from django.db import transaction
from .models import Product, Listing, Inventory, ProductImage
from .forms import ProductForm, ListingForm, InventoryForm

@login_required
def marketplace(request):
    if request.user.role != 'customer':
        return redirect('farmer_dashboard')
    
    query = request.GET.get('q', '')
    from django.shortcuts import get_object_or_404
    listings = Listing.objects.filter(is_active=True, inventory__available_quantity__gt=0).select_related('product', 'product__farmer')
    
    if query:
        listings = listings.filter(product__commodity__icontains=query)
        
    return render(request, 'backend/marketplace.html', {'listings': listings})

@login_required
def farmer_add_product(request):
    if request.user.role != 'farmer':
        return redirect('customer_dashboard')
    
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        inventory_form = InventoryForm(request.POST)
        
        if product_form.is_valid() and inventory_form.is_valid():
            with transaction.atomic():
                product = product_form.save(commit=False)
                product.farmer = request.user.farmer_profile
                product.save()
                
                listing = Listing.objects.create(
                    product=product,
                    selling_price_per_kg=0,
                    is_active=False
                )
                
                inventory = inventory_form.save(commit=False)
                inventory.product = product
                inventory.reserved_quantity = 0
                inventory.save()
                
                return redirect('farmer_set_pricing', listing_id=listing.id)
    else:
        product_form = ProductForm()
        inventory_form = InventoryForm()
        
    return render(request, 'backend/farmer_add_product.html', {
        'product_form': product_form,
        'inventory_form': inventory_form
    })

@login_required
def farmer_set_pricing(request, listing_id):
    if request.user.role != 'farmer':
        return redirect('customer_dashboard')
        
    from django.shortcuts import get_object_or_404
    listing = get_object_or_404(Listing, id=listing_id, product__farmer=request.user.farmer_profile)
    
    if request.method == 'POST':
        listing_form = ListingForm(request.POST, instance=listing)
        if listing_form.is_valid():
            listing = listing_form.save(commit=False)
            listing.price_at_listing = listing.selling_price_per_kg
            listing.is_active = True
            listing.save()
            
            from .models import ResearchEvent
            metadata = {
                'product_id': listing.product.id, 
                'price': str(listing.selling_price_per_kg),
                'ai_predicted_price': str(listing.ai_predicted_price) if listing.ai_predicted_price else None,
                'reference_market_price': str(listing.reference_market_price) if listing.reference_market_price else None
            }
            ResearchEvent.objects.create(user=request.user, event_type='PRODUCT_LISTED', metadata=metadata)
            
            return redirect('farmer_products')
    else:
        listing_form = ListingForm(instance=listing if listing.selling_price_per_kg > 0 else None)
        
    return render(request, 'backend/farmer_set_pricing.html', {
        'listing': listing,
        'listing_form': listing_form
    })

@login_required
def farmer_products(request):
    if request.user.role != 'farmer':
        return redirect('customer_dashboard')
    products = Product.objects.filter(farmer=request.user.farmer_profile)
    return render(request, 'backend/farmer_products.html', {'products': products})

from ai_services.crop_recommendation.data_loader import load_crop_data
from ai_services.dynamic_pricing.data_loader import load_raw_market_data

@login_required
def crop_recommendation_view(request):
    if request.user.role != 'farmer':
        return redirect('customer_dashboard')
        
    try:
        crop_df = load_crop_data()
        crop_samples = crop_df.sample(5).to_dict(orient='records')
    except Exception:
        crop_samples = []
        
    from .models import ResearchEvent
    ResearchEvent.objects.create(user=request.user, event_type='CROP_RECOMMENDATION_REQUESTED')
        
    import json
    return render(request, 'backend/crop_recommendation.html', {
        'crop_samples': crop_samples,
        'crop_samples_json': json.dumps(crop_samples),
    })

@login_required
def dynamic_pricing_view(request):
    if request.user.role != 'farmer':
        return redirect('customer_dashboard')
        
    try:
        market_df = load_raw_market_data().dropna(subset=['State/UT', 'District', 'Market', 'Commodity', 'Modal Price Per Kg'])
        raw_samples = market_df.sample(5).to_dict(orient='records')
        market_samples = []
        for row in raw_samples:
            market_samples.append({
                'state': row.get('State/UT'),
                'district': row.get('District'),
                'market': row.get('Market'),
                'commodity': row.get('Commodity'),
                'variety': row.get('Variety'),
                'grade': row.get('Grade'),
                'min_price': row.get('Min Price Per Kg'),
                'max_price': row.get('Max Price Per Kg'),
                'modal_price': row.get('Modal Price Per Kg'),
                'date': row.get('Price Date')
            })
    except Exception:
        market_samples = []
    
    import json
    for m in market_samples:
        if hasattr(m['date'], 'isoformat'):
            m['date'] = m['date'].isoformat()
        else:
            m['date'] = str(m['date'])
            
    from .models import ResearchEvent
    ResearchEvent.objects.create(user=request.user, event_type='MARKET_PRICE_VIEWED')
            
    return render(request, 'backend/dynamic_pricing.html', {
        'market_samples': market_samples,
        'market_samples_json': json.dumps(market_samples)
    })

@login_required
def marketplace(request):
    if request.user.role != 'customer':
        return redirect('farmer_dashboard')
    
    query = request.GET.get('q', '')
    listings = Listing.objects.filter(is_active=True, product__inventory__available_quantity__gt=0).select_related('product', 'product__farmer')
    
    if query:
        listings = listings.filter(product__commodity__icontains=query)
        
    vegetables = ['Tomato', 'Onion', 'Potato', 'Cabbage', 'Cauliflower', 'Brinjal', 'Carrot', 'Capsicum', 'Green Chilli', 'Lady Finger', 'Bitter gourd', 'Bottle gourd', 'Ridge gourd', 'Sponge gourd', 'Pumpkin', 'Sweet Potato', 'Beetroot', 'Radish', 'Spinach', 'Coriander Leaves', 'Mint Leaves', 'Curry Leaves', 'Drumstick', 'Garlic', 'Ginger']
    fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes', 'Papaya', 'Pomegranate', 'Guava', 'Pineapple', 'Water Melon', 'Musk Melon', 'Lemon', 'Sweet Lime', 'Sapota', 'Jack Fruit', 'Plum', 'Pear', 'Peach', 'Cherry', 'Strawberry']
    flowers = ['Rose', 'Marigold', 'Jasmine', 'Chrysanthemum', 'Tuberose', 'Aster', 'Gladiolus', 'Carnation', 'Orchid', 'Gerbera', 'Lily']
    
    categorized_listings = {
        'Vegetables': [],
        'Fruits': [],
        'Flowers': [],
        'Others': []
    }
    
    for listing in listings:
        c = listing.product.commodity
        if any(v.lower() in c.lower() for v in vegetables):
            categorized_listings['Vegetables'].append(listing)
        elif any(f.lower() in c.lower() for f in fruits):
            categorized_listings['Fruits'].append(listing)
        elif any(fl.lower() in c.lower() for fl in flowers):
            categorized_listings['Flowers'].append(listing)
        else:
            categorized_listings['Others'].append(listing)
            
    # Remove empty categories
    categorized_listings = {k: v for k, v in categorized_listings.items() if v}
        
    return render(request, 'backend/marketplace.html', {
        'categorized_listings': categorized_listings,
        'query': query
    })

@login_required
def product_details(request, pk):
    if request.user.role != 'customer':
        return redirect('farmer_dashboard')
    from django.shortcuts import get_object_or_404
    listing = get_object_or_404(Listing.objects.select_related('product', 'product__inventory', 'product__farmer'), pk=pk, is_active=True)
    
    from .models import ResearchEvent
    ResearchEvent.objects.create(user=request.user, event_type='PRODUCT_VIEWED', metadata={'listing_id': listing.id})
    
    return render(request, 'backend/product_details.html', {'listing': listing})

from .models import Cart, CartItem, Order, OrderItem
from .services import PaymentService
from decimal import Decimal

@login_required
def add_to_cart(request, listing_id):
    if request.user.role != 'customer':
        return redirect('farmer_dashboard')
        
    if request.method == 'POST':
        quantity = Decimal(request.POST.get('quantity', 1))
        from django.shortcuts import get_object_or_404
        listing = get_object_or_404(Listing.objects.select_related('product__inventory'), id=listing_id, is_active=True)
        
        if quantity > listing.product.inventory.available_quantity:
            return redirect('product_details', pk=listing_id)
            
        cart, _ = Cart.objects.get_or_create(customer=request.user.customer_profile)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, listing=listing, defaults={'quantity': 0})
        
        if cart_item.quantity + quantity <= listing.product.inventory.available_quantity:
            cart_item.quantity += quantity
            cart_item.save()
            from .models import ResearchEvent
            ResearchEvent.objects.create(user=request.user, event_type='PRODUCT_ADDED_TO_CART', metadata={'listing_id': listing.id, 'quantity': str(quantity)})
            
    referer = request.META.get('HTTP_REFERER', 'marketplace')
    return redirect(referer)

@login_required
def cart_view(request):
    if request.user.role != 'customer':
        return redirect('farmer_dashboard')
        
    cart, created = Cart.objects.get_or_create(customer=request.user.customer_profile)
    items = cart.items.select_related('listing', 'listing__product')
    
    subtotal = sum(item.quantity * item.listing.selling_price_per_kg for item in items)
    
    return render(request, 'backend/cart.html', {'items': items, 'subtotal': subtotal})

@login_required
def update_cart_item(request, item_id):
    if request.user.role != 'customer' or request.method != 'POST':
        return redirect('farmer_dashboard')
        
    try:
        cart_item = CartItem.objects.select_related('listing__product__inventory').get(
            id=item_id, 
            cart__customer=request.user.customer_profile
        )
        new_quantity = Decimal(request.POST.get('quantity', cart_item.quantity))
        
        if new_quantity <= 0:
            cart_item.delete()
        elif new_quantity <= cart_item.listing.product.inventory.available_quantity:
            cart_item.quantity = new_quantity
            cart_item.save()
    except CartItem.DoesNotExist:
        pass
        
    return redirect('cart_view')

@login_required
def remove_cart_item(request, item_id):
    if request.user.role != 'customer' or request.method != 'POST':
        return redirect('farmer_dashboard')
        
    try:
        CartItem.objects.filter(
            id=item_id, 
            cart__customer=request.user.customer_profile
        ).delete()
    except Exception:
        pass
        
    return redirect('cart_view')

@login_required
def checkout(request):
    if request.user.role != 'customer':
        return redirect('farmer_dashboard')
        
    cart = Cart.objects.get(customer=request.user.customer_profile)
    items = cart.items.select_related('listing', 'listing__product__inventory')
    
    if not items.exists():
        return redirect('marketplace')
        
    if request.method == 'POST':
        with transaction.atomic():
            total_amount = Decimal('0.00')
            for item in items:
                listing = Listing.objects.select_for_update().get(id=item.listing_id)
                if listing.product.inventory.available_quantity < item.quantity:
                    raise ValueError(f"Not enough inventory for {listing.product.commodity}")
                
                listing.product.inventory.reserved_quantity += item.quantity
                listing.product.inventory.save()
                
                total_amount += item.quantity * listing.selling_price_per_kg
                
            order = Order.objects.create(customer=request.user.customer_profile, total_amount=total_amount)
            
            for item in items:
                OrderItem.objects.create(
                    order=order,
                    listing=item.listing,
                    quantity=item.quantity,
                    price_at_sale=item.listing.selling_price_per_kg
                )
                
            cart.items.all().delete()
            
            payment = PaymentService.create_payment(order, total_amount)
            PaymentService.verify_payment(payment.id, success=True)
            
            from .models import ResearchEvent
            ResearchEvent.objects.create(user=request.user, event_type='PAYMENT_SUCCESS', metadata={'order_id': order.id, 'amount': str(total_amount)})
            ResearchEvent.objects.create(user=request.user, event_type='ORDER_CREATED', metadata={'order_id': order.id, 'total': str(total_amount)})
            
            return redirect('order_history')
            
    if request.method == 'GET':
        from .models import ResearchEvent
        ResearchEvent.objects.create(user=request.user, event_type='CHECKOUT_STARTED')
            
    return render(request, 'backend/checkout.html', {'items': items})

@login_required
def order_history(request):
    if request.user.role == 'customer':
        orders = Order.objects.filter(customer=request.user.customer_profile).order_by('-created_at')
        return render(request, 'backend/customer_orders.html', {'orders': orders})
    elif request.user.role == 'farmer':
        orders = Order.objects.filter(items__listing__product__farmer=request.user.farmer_profile).distinct().order_by('-created_at')
        return render(request, 'backend/farmer_orders.html', {'orders': orders})

@login_required
def update_order_status(request, order_id):
    if request.user.role != 'farmer' or request.method != 'POST':
        return redirect('customer_dashboard')
        
    status = request.POST.get('status')
    if status in dict(Order.STATUS_CHOICES):
        order = Order.objects.filter(id=order_id, items__listing__product__farmer=request.user.farmer_profile).first()
        if order:
            order.status = status
            order.save()
            if status == 'DELIVERED':
                from .models import ResearchEvent
                ResearchEvent.objects.create(user=request.user, event_type='ORDER_COMPLETED', metadata={'order_id': order.id})
                
    referer = request.META.get('HTTP_REFERER', 'order_history')
    return redirect(referer)

from .forms import TAMSurveyForm

@login_required
def tam_survey_view(request):
    if request.method == 'POST':
        form = TAMSurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.user = request.user
            survey.save()
            if request.user.role == 'farmer':
                return redirect('farmer_dashboard')
            else:
                return redirect('customer_dashboard')
    else:
        form = TAMSurveyForm()
        
    return render(request, 'backend/tam_survey.html', {'form': form})


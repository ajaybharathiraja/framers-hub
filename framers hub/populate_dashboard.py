import os
import django
import pandas as pd
import random
from datetime import date, timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uzhavarhub_project.settings')
django.setup()

from backend.models import User, FarmerProfile, CustomerProfile, Product, Listing, Inventory, Order, OrderItem

def populate():
    print("Loading dataset...")
    df = pd.read_csv('data/raw/combined_commodity_prices_per_kg.csv')
    
    # Get test_farmer
    try:
        farmer_user = User.objects.get(username='test_farmer')
        farmer_profile = farmer_user.farmer_profile
    except Exception as e:
        print("test_farmer not found or missing profile.")
        return

    # Delete existing products for test_farmer to avoid duplicates on multiple runs
    Product.objects.filter(farmer=farmer_profile).delete()

    print(f"Populating data for {farmer_user.username}...")

    # Get a sample of 5 unique commodities
    latest_data = df.sort_values('Price Date', ascending=False)
    sample_data = latest_data.drop_duplicates(subset=['Commodity']).head(5)

    # Make sure we have a test customer for orders
    customer_user, _ = User.objects.get_or_create(username='test_customer', defaults={'email': 'test_cust@example.com', 'role': 'customer'})
    customer_profile, _ = CustomerProfile.objects.get_or_create(user=customer_user)

    for index, row in sample_data.iterrows():
        state = row['State/UT']
        district = row.get('District', 'Unknown')
        market = row['Market']
        commodity = row['Commodity']
        variety = row.get('Variety', '')
        price = row['Modal Price Per Kg']

        # Create Product
        product = Product.objects.create(
            farmer=farmer_profile,
            commodity=commodity,
            variety=variety if pd.notna(variety) else '',
            grade=row.get('Grade', ''),
            description=f"Fresh {commodity} straight from {market}, {state}.",
            location=market,
            harvest_date=date.today() - timedelta(days=random.randint(1, 10))
        )
        
        # Create Listing
        listing = Listing.objects.create(
            product=product,
            selling_price_per_kg=price,
            is_active=True
        )
        
        # Create Inventory
        Inventory.objects.create(
            product=product,
            total_quantity=random.randint(200, 1000),
            reserved_quantity=0
        )

        # Create some random orders for this listing to populate income
        for i in range(random.randint(2, 5)):
            # Orders spread across the last month
            order_date = timezone.now() - timedelta(days=random.randint(0, 30))
            
            qty = random.randint(10, 50)
            order = Order.objects.create(
                customer=customer_profile,
                status='DELIVERED',
                total_amount=qty * price
            )
            # Override created_at for historical data charting
            order.created_at = order_date
            order.save()

            OrderItem.objects.create(
                order=order,
                listing=listing,
                quantity=qty,
                price_at_sale=price
            )

    print("Dashboard populated successfully with dataset values!")

if __name__ == '__main__':
    populate()

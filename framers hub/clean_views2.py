import re

with open('backend/views.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'def customer_dashboard' in line:
        customer_dashboard_idx = i
        break

# The REAL farmer_add_product starts with 'product_form = ProductForm(request.POST)' and 'inventory_form = InventoryForm(request.POST)' but NO 'listing_form'.
for i, line in enumerate(lines):
    if 'def farmer_add_product' in line and 'listing_form = ListingForm(request.POST)' not in ''.join(lines[i:i+20]):
        new_farmer_add_idx = i
        break

while '@login_required' not in lines[new_farmer_add_idx - 1]:
    new_farmer_add_idx -= 1
new_farmer_add_idx -= 1

imports_and_marketplace = """
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

"""

new_lines = lines[:customer_dashboard_idx+4] + [imports_and_marketplace] + lines[new_farmer_add_idx:]

with open('backend/views.py', 'w') as f:
    f.writelines(new_lines)
print("done")

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uzhavarhub_project.settings')
django.setup()

from django.test import Client
from backend.models import User, FarmerProfile, Product, Listing

def test_api():
    # Setup test user and listing
    user, created = User.objects.get_or_create(username='testapiuser', role='farmer')
    if created:
        user.set_password('password123')
        user.save()
        farmer = FarmerProfile.objects.create(
            user=user,
            phone='1234567890',
            state='Maharashtra',
            district='Pune',
            location='Pune',
            farming_information='Test'
        )
    else:
        farmer = user.farmer_profile
        
    product, _ = Product.objects.get_or_create(
        farmer=farmer,
        commodity='Onion',
        defaults={'location': 'Pune'}
    )
    
    listing, _ = Listing.objects.get_or_create(
        product=product,
        defaults={
            'selling_price_per_kg': '55.00',
            'price_at_listing': '55.00'
        }
    )
    
    client = Client(SERVER_NAME='localhost')
    client.login(username='testapiuser', password='password123')
    
    # Hit the API with listing_id
    url = f'/api/market-intelligence/?state=Maharashtra&district=Pune&market=Pune&commodity=Onion&listing_id={listing.id}'
    response = client.get(url)
    print("API Response Code:", response.status_code)
    
    # Reload listing
    listing.refresh_from_db()
    print(f"Listing ID: {listing.id}")
    print(f"Commodity: {listing.product.commodity}")
    print(f"Selling Price: {listing.selling_price_per_kg}")
    print(f"AI Predicted Price: {listing.ai_predicted_price}")
    print(f"Reference Market Price: {listing.reference_market_price}")

if __name__ == '__main__':
    test_api()

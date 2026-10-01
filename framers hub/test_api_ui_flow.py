import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uzhavarhub_project.settings')
django.setup()

from django.test import Client
from backend.models import User, FarmerProfile, Product, Listing

def test_flow():
    # Setup test user
    user, created = User.objects.get_or_create(username='testfarmer2', role='farmer')
    if created:
        user.set_password('password123')
        user.save()
        FarmerProfile.objects.create(
            user=user,
            phone='1234567890',
            state='Tamil Nadu',
            district='Ariyalur',
            location='Ariyalur(Uzhavar Sandhai)',
            farming_information='Test'
        )
    
    client = Client(SERVER_NAME='localhost')
    client.login(username='testfarmer2', password='password123')
    
    # 1. Add product (Draft)
    response = client.post('/farmer/products/add/', {
        'commodity': 'Tomato',
        'variety': '',
        'grade': '',
        'description': 'Fresh',
        'location': 'Ariyalur(Uzhavar Sandhai)',
        'total_quantity': '100.00'
    })
    
    print("Add Product Status (should redirect to pricing):", response.status_code)
    print("Redirect URL:", response.url if response.status_code == 302 else "No redirect")
    
    listing = Listing.objects.filter(product__farmer__user__username='testfarmer2').last()
    print("Listing Draft Created, ID:", listing.id)
    print("is_active:", listing.is_active)
    
    # 2. Simulate API Call
    url = f'/api/market-intelligence/?state=Tamil Nadu&district=Ariyalur&market=Ariyalur(Uzhavar Sandhai)&commodity=Tomato&listing_id={listing.id}'
    api_response = client.get(url)
    print("API Response Code:", api_response.status_code)
    
    # 3. Post Final Pricing
    final_response = client.post(f'/farmer/products/{listing.id}/pricing/', {
        'selling_price_per_kg': '45.00'
    })
    
    print("Set Pricing Status (should redirect to products):", final_response.status_code)
    
    # Reload listing
    listing.refresh_from_db()
    print(f"--- Final Listing State ---")
    print(f"ID: {listing.id}")
    print(f"Commodity: {listing.product.commodity}")
    print(f"Selling Price: {listing.selling_price_per_kg}")
    print(f"AI Predicted Price: {listing.ai_predicted_price}")
    print(f"Reference Market Price: {listing.reference_market_price}")
    print(f"is_active: {listing.is_active}")

if __name__ == '__main__':
    test_flow()

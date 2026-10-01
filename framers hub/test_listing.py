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
    else:
        user.set_password('password123')
        user.save()
    
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
    
    listing = Listing.objects.filter(product__farmer__user__username='testfarmer2').last()
    
    # 2. Simulate API Call
    url = f'/api/market-intelligence/?state=Tamil Nadu&district=Ariyalur&market=Ariyalur(Uzhavar Sandhai)&commodity=Tomato&listing_id={listing.id}'
    api_response = client.get(url)
    
    # 3. Post Final Pricing
    final_response = client.post(f'/farmer/products/{listing.id}/pricing/', {
        'selling_price_per_kg': '45.00'
    })
    
    # Reload listing
    listing.refresh_from_db()
    print(f"--- Actual DB Output ---")
    print(f"ai_predicted_price: {listing.ai_predicted_price}")
    print(f"reference_market_price: {listing.reference_market_price}")
    print(f"selling_price_per_kg: {listing.selling_price_per_kg}")
    print(f"is_active: {listing.is_active}")

if __name__ == '__main__':
    test_flow()

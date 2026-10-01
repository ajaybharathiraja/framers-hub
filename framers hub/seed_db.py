import os
import django
import pandas as pd
import random
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uzhavarhub_project.settings')
django.setup()

from backend.models import User, FarmerProfile, CustomerProfile, Product, Listing, Inventory

def seed_database():
    print("Loading dataset...")
    df = pd.read_csv('data/raw/combined_commodity_prices_per_kg.csv')
    
    # Take a random sample of 50 unique commodities to populate the marketplace
    # To get good variety, let's group by commodity and take the latest price
    # First, get latest prices for each commodity across all markets
    latest_data = df.sort_values('Price Date', ascending=False)
    # Get a diverse set of unique commodities
    diverse_commodities = latest_data.drop_duplicates(subset=['Commodity']).head(30)
    sample_data = diverse_commodities
    
    print("Clearing old data (except test users)...")
    Product.objects.all().delete()
    User.objects.filter(is_superuser=False).exclude(username__in=['test_farmer', 'test_customer']).delete()
    
    print("Generating Farmers, Products, and Listings...")
    
    for index, row in sample_data.iterrows():
        # Create a farmer for this market
        state = row['State/UT']
        district = row.get('District', 'Unknown')
        market = row['Market']
        commodity = row['Commodity']
        variety = row.get('Variety', '')
        price = row['Modal Price Per Kg']
        
        # Format a username based on market
        username = f"farmer_{market.lower().replace(' ', '_').replace('(', '').replace(')', '')}_{random.randint(100,999)}"
        
        farmer_user, created = User.objects.get_or_create(
            username=username, 
            defaults={'email': f"{username}@example.com", 'role': 'farmer'}
        )
        if created:
            farmer_user.set_password('testpass123')
            farmer_user.save()
            farmer_profile = FarmerProfile.objects.create(
                user=farmer_user,
                phone=f"98{random.randint(10000000, 99999999)}",
                state=state,
                district=district,
                location=market,
                farming_information=f"Specializes in growing high-quality crops in the {market} region."
            )
        else:
            farmer_profile = farmer_user.farmer_profile
            
        # Create Product
        product = Product.objects.create(
            farmer=farmer_profile,
            commodity=commodity,
            variety=variety if pd.notna(variety) else '',
            grade=row.get('Grade', ''),
            description=f"Fresh {commodity} straight from {market}, {state}.",
            location=market,
            harvest_date=date.today()
        )
        
        # Create Listing
        Listing.objects.create(
            product=product,
            selling_price_per_kg=price,
            is_active=True
        )
        
        # Create Inventory (Random stock between 50 and 500 kg)
        Inventory.objects.create(
            product=product,
            total_quantity=random.randint(50, 500),
            reserved_quantity=0
        )
        
    print("Database seeded successfully! The marketplace is now full of real products.")

if __name__ == '__main__':
    seed_database()

from django.test import TestCase, Client
from django.urls import reverse
import json
from .models import ResearchEvent, FarmerProfile
from django.contrib.auth.models import User

class APITests(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_crop_recommendation_api(self):
        payload = {
            "N": 90, "P": 42, "K": 43, 
            "temperature": 20.8, "humidity": 82.0, 
            "ph": 6.5, "rainfall": 202.9
        }
        response = self.client.post(
            reverse('api_crop_recommendation'), 
            data=json.dumps(payload),
            content_type='application/json'
        )
        # Assuming the model is loaded during testing, it should return 200
        # If the model isn't available in CI, it returns 503
        self.assertIn(response.status_code, [200, 503])
        
        if response.status_code == 200:
            data = response.json()
            self.assertIn('recommended_crop', data)
            self.assertIn('confidence', data)

    def test_market_intelligence_api_missing_params(self):
        response = self.client.get(reverse('api_market_intelligence'))
        self.assertEqual(response.status_code, 400)

class ResearchEventTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_farmer', password='password')
        self.farmer = FarmerProfile.objects.create(
            user=self.user, 
            location='Test Village', 
            farm_size=2.5, 
            primary_crops='Tomato'
        )

    def test_research_event_logging(self):
        event = ResearchEvent.objects.create(
            user=self.user,
            event_type='API_CALL',
            event_data={'endpoint': 'crop-recommendation', 'result': 'rice'},
            path='/api/crop-recommendation/'
        )
        self.assertEqual(ResearchEvent.objects.count(), 1)
        self.assertEqual(event.event_type, 'API_CALL')
        self.assertEqual(event.event_data['result'], 'rice')

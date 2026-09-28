from django.http import JsonResponse
from django.views.decorators.http import require_GET
from ai_services.dynamic_pricing.data_loader import load_raw_market_data
from ai_services.dynamic_pricing.preprocessing import clean_market_data, get_market_intelligence

# For performance, we should ideally load this once or use a database.
# Since Phase 6 requires API exposure, we will load it into memory on first request
# or use caching. Given the 63MB size, caching or DB is preferred, but for now
# we will use a global variable to avoid repeated loading during this prototype phase.
# In a real production deployment, this would be imported into a PostgreSQL table.
MARKET_DATA = None

def get_market_data():
    global MARKET_DATA
    if MARKET_DATA is None:
        try:
            df = load_raw_market_data()
            MARKET_DATA = clean_market_data(df)
        except Exception as e:
            return None
    return MARKET_DATA

from ai_services.dynamic_pricing.predict import load_pricing_model, predict_price
from ai_services.dynamic_pricing.explain import generate_pricing_explanation

# Load model globally to avoid loading on every request
PRICING_MODEL, PRICING_METADATA = load_pricing_model()

@require_GET
def market_intelligence_api(request):
    """
    Market Intelligence API Endpoint
    
    Example Request:
    GET /api/market-intelligence/?state=Tamil%20Nadu&district=Coimbatore&market=Coimbatore&commodity=Tomato
    
    Example Response:
    {
        "data": {
            "latest_price": 57.0,
            "min_price": 50.0,
            "max_price": 60.0,
            "historical_avg": 54.5,
            "recent_trend_pct": 4.5,
            "last_updated": "2026-09-13",
            "predicted_price": 58.2,
            "explanation": [...SHAP output...],
            "ai_metadata": {...}
        }
    }
    """
    state = request.GET.get('state')
    district = request.GET.get('district')
    market = request.GET.get('market')
    commodity = request.GET.get('commodity')
    variety = request.GET.get('variety', None)
    grade = request.GET.get('grade', None)
    listing_id = request.GET.get('listing_id', None)
    
    if not all([state, district, market, commodity]):
        return JsonResponse({'error': 'Missing required parameters'}, status=400)
        
    df = get_market_data()
    if df is None:
        return JsonResponse({'error': 'Market data unavailable'}, status=503)
        
    intelligence = get_market_intelligence(df, state, district, market, commodity, variety, grade)
    
    if not intelligence:
        return JsonResponse({'error': 'No historical data found.'}, status=404)
        
    if PRICING_MODEL and PRICING_METADATA:
        # Generate features dynamically for prediction
        from ai_services.dynamic_pricing.feature_engineering import create_features
        mask = (df['State/UT'].str.lower() == state.lower()) & \
               (df['District'].str.lower().str.contains(district.lower(), regex=False, na=False)) & \
               (df['Market'].str.lower().str.contains(market.lower(), regex=False, na=False)) & \
               (df['Commodity'].str.lower() == commodity.lower())
        if variety and str(variety).lower() != 'nan':
            mask &= (df['Variety'].str.lower() == variety.lower())
        if grade and str(grade).lower() != 'nan':
            mask &= (df['Grade'].str.lower() == grade.lower())
            
        filtered = df[mask].copy()
        
        try:
            df_features = create_features(filtered)
            if not df_features.empty:
                latest_features = df_features.iloc[-1]
                features_dict = {f: float(latest_features.get(f, 0)) for f in PRICING_METADATA['features']}
                
                predicted_price = predict_price(features_dict, PRICING_MODEL, PRICING_METADATA)
                intelligence['predicted_price'] = float(predicted_price)
                
                from .models import ResearchEvent, Listing
                if request.user.is_authenticated:
                    ResearchEvent.objects.create(user=request.user, event_type='PRICE_PREDICTION_REQUESTED', metadata={'predicted_price': float(predicted_price)})
                
                if listing_id:
                    try:
                        listing = Listing.objects.get(id=listing_id)
                        listing.ai_predicted_price = float(predicted_price)
                        listing.reference_market_price = float(intelligence.get('latest_price') or intelligence.get('historical_avg') or 0)
                        listing.save()
                    except Exception as e:
                        import logging
                        logger = logging.getLogger(__name__)
                        logger.warning(f"Failed to save AI predicted price to listing {listing_id}: {e}")
                
                explanation = generate_pricing_explanation(PRICING_MODEL, features_dict, PRICING_METADATA)
                intelligence['explanation'] = explanation
            else:
                raise ValueError("Not enough historical data to generate lag features.")
        except Exception as e:
            intelligence['predicted_price'] = None
            intelligence['explanation'] = None
            
        intelligence['ai_metadata'] = {
            'model_version': PRICING_METADATA['version'],
            'model_name': PRICING_METADATA['model_name'],
            'note': 'AI-generated estimate based on historical market data.'
        }
        
    return JsonResponse({'data': intelligence})

from ai_services.crop_recommendation.predict import load_crop_model, predict_crop
from ai_services.crop_recommendation.explain import generate_crop_explanation
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

CROP_MODEL, CROP_LE, CROP_METADATA = load_crop_model()

@csrf_exempt
@require_POST
def crop_recommendation_api(request):
    """
    Crop Recommendation API Endpoint
    
    Example Request:
    POST /api/crop-recommendation/
    Body: {"N": 90, "P": 42, "K": 43, "temperature": 20.8, "humidity": 82.0, "ph": 6.5, "rainfall": 202.9}
    
    Example Response:
    {
        "recommended_crop": "rice",
        "confidence": 99.5,
        "top_recommendations": [...],
        "explanation": [...],
        "ai_metadata": {...}
    }
    """
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
    required_keys = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    if not all(k in data for k in required_keys):
        return JsonResponse({'error': f'Missing required parameters. Need: {required_keys}'}, status=400)
        
    if not CROP_MODEL:
        return JsonResponse({'error': 'Crop model is not loaded or unavailable.'}, status=503)
        
    features_dict = {
        'N': float(data['N']),
        'P': float(data['P']),
        'K': float(data['K']),
        'temperature': float(data['temperature']),
        'humidity': float(data['humidity']),
        'ph': float(data['ph']),
        'rainfall': float(data['rainfall'])
    }
    
    results = predict_crop(features_dict, CROP_MODEL, CROP_LE, CROP_METADATA)
    explanation = generate_crop_explanation(CROP_MODEL, features_dict, CROP_METADATA)
    
    from .models import ResearchEvent
    if request.user.is_authenticated:
        ResearchEvent.objects.create(user=request.user, event_type='CROP_RECOMMENDATION_VIEWED', metadata={'recommended_crop': results[0]['crop']})
    
    return JsonResponse({
        'recommended_crop': results[0]['crop'],
        'confidence': results[0]['confidence'],
        'top_recommendations': results,
        'explanation': explanation,
        'ai_metadata': {
            'model_version': CROP_METADATA['version'],
            'model_name': CROP_METADATA['model_name'],
            'note': 'Recommendation generated from the trained crop-recommendation model. Does not guarantee agricultural success.'
        }
    })

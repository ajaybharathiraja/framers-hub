import traceback
import pandas as pd
from ai_services.dynamic_pricing.predict import load_pricing_model, predict_price
from ai_services.dynamic_pricing.feature_engineering import create_features
from ai_services.dynamic_pricing.explain import generate_pricing_explanation

try:
    PRICING_MODEL, PRICING_METADATA = load_pricing_model()
    df = pd.DataFrame({'State/UT':['Tamil Nadu'], 'District':['Nagapattinam'], 'Market':['Vedaranyam(Uzhavar Sandhai)'], 'Commodity':['Onion'], 'Price Date':pd.to_datetime(['2023-01-01']), 'Modal Price Per Kg':[30.88]})
    df_features = create_features(df)
    latest_features = df_features.iloc[-1]
    features_dict = {f: float(latest_features.get(f, 0)) for f in PRICING_METADATA['features']}
    print('Features:', features_dict)
    
    pred = predict_price(features_dict, PRICING_MODEL, PRICING_METADATA)
    print('Pred:', pred)
    
    explanation = generate_pricing_explanation(PRICING_MODEL, features_dict, PRICING_METADATA)
    print('Explanation success')
except Exception as e:
    traceback.print_exc()

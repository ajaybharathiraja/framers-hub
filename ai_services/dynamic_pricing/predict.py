import joblib
import json
import os
import pandas as pd

def load_pricing_model():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    model_path = os.path.join(base_dir, 'ai_services/dynamic_pricing/models/best_pricing_model.joblib')
    meta_path = os.path.join(base_dir, 'ai_services/dynamic_pricing/models/metadata.json')
    
    if not os.path.exists(model_path) or not os.path.exists(meta_path):
        return None, None
        
    model = joblib.load(model_path)
    with open(meta_path, 'r') as f:
        metadata = json.load(f)
        
    return model, metadata

def predict_price(features_dict, model, metadata):
    """
    Predicts the price given a dictionary of features matching the model's training features.
    """
    feature_cols = metadata['features']
    # Create DataFrame with a single row, ensuring columns match
    df = pd.DataFrame([features_dict], columns=feature_cols).fillna(0)
    prediction = model.predict(df)[0]
    return prediction

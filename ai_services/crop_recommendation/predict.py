import joblib
import json
import os
import pandas as pd
import numpy as np

def load_crop_model():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    model_path = os.path.join(base_dir, 'ai_services/crop_recommendation/models/crop_rf_v1.0.joblib')
    le_path = os.path.join(base_dir, 'ai_services/crop_recommendation/models/label_encoder.joblib')
    meta_path = os.path.join(base_dir, 'ai_services/crop_recommendation/models/metadata.json')
    
    if not os.path.exists(model_path) or not os.path.exists(meta_path) or not os.path.exists(le_path):
        return None, None, None
        
    model = joblib.load(model_path)
    le = joblib.load(le_path)
    with open(meta_path, 'r') as f:
        metadata = json.load(f)
        
    return model, le, metadata

def predict_crop(features_dict, model, le, metadata):
    """
    Predicts the recommended crop and probabilities.
    """
    feature_cols = metadata['features']
    df = pd.DataFrame([features_dict], columns=feature_cols)
    
    # Predict probabilities
    probs = model.predict_proba(df)[0]
    
    # Get top 3 indices
    top_3_idx = np.argsort(probs)[-3:][::-1]
    
    results = []
    for idx in top_3_idx:
        crop_name = le.inverse_transform([idx])[0]
        confidence = probs[idx] * 100
        results.append({
            'crop': crop_name,
            'confidence': float(confidence)
        })
        
    return results

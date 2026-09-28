import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

def preprocess_crop_data(df, fit=True):
    """
    Validates and preprocesses crop data.
    """
    required_cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'label']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
            
    df_clean = df.dropna().copy()
    
    X = df_clean[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = df_clean['label']
    
    if fit:
        le = LabelEncoder()
        y_encoded = le.fit_transform(y)
        # Save LabelEncoder
        joblib.dump(le, 'ai_services/crop_recommendation/models/label_encoder.joblib')
        return X, y_encoded, le
    else:
        # Just return X for prediction preprocessing
        return X

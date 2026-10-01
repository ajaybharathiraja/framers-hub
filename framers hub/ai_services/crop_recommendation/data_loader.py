import pandas as pd
import os

def load_crop_data(filepath='data/raw/Crop_recommendation.csv'):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Crop dataset not found at {filepath}")
    
    df = pd.read_csv(filepath)
    return df

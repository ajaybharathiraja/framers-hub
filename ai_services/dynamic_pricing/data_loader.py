import pandas as pd
import os

def load_raw_market_data(filepath='data/raw/combined_commodity_prices_per_kg.csv'):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}")
    
    df = pd.read_csv(filepath)
    return df

def save_processed_data(df, filepath='data/processed/market_prices_cleaned.csv'):
    df.to_csv(filepath, index=False)

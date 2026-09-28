import pandas as pd
import os

def load_raw_market_data(filepath='data/raw/combined_commodity_prices_per_kg.csv'):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    abs_filepath = os.path.join(base_dir, filepath)
    
    if not os.path.exists(abs_filepath):
        raise FileNotFoundError(f"Dataset not found at {abs_filepath}")
    
    df = pd.read_csv(abs_filepath)
    return df

def save_processed_data(df, filepath='data/processed/market_prices_cleaned.csv'):
    df.to_csv(filepath, index=False)

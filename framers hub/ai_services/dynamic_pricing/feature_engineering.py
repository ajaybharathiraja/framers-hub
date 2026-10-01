import pandas as pd
import numpy as np

def create_features(df):
    """
    Creates temporal and rolling features for price prediction.
    Must be grouped by Market and Commodity to prevent leakage across markets.
    """
    df = df.copy()
    
    # Sort by date
    df = df.sort_values(by=['State/UT', 'District', 'Market', 'Commodity', 'Price Date'])
    
    # Temporal features
    df['year'] = df['Price Date'].dt.year
    df['month'] = df['Price Date'].dt.month
    df['week'] = df['Price Date'].dt.isocalendar().week
    df['day_of_week'] = df['Price Date'].dt.dayofweek
    
    # Cyclical encoding for month and day_of_week
    df['month_sin'] = np.sin(2 * np.pi * df['month']/12.0)
    df['month_cos'] = np.cos(2 * np.pi * df['month']/12.0)
    df['day_sin'] = np.sin(2 * np.pi * df['day_of_week']/7.0)
    df['day_cos'] = np.cos(2 * np.pi * df['day_of_week']/7.0)
    
    # Lag features
    groups = df.groupby(['State/UT', 'District', 'Market', 'Commodity'])
    df['lag_1'] = groups['Modal Price Per Kg'].shift(1)
    df['lag_7'] = groups['Modal Price Per Kg'].shift(7)
    df['lag_30'] = groups['Modal Price Per Kg'].shift(30)
    
    # Rolling features (use closed='left' if we were doing daily resample, 
    # but here shift is safer to avoid leakage of current day)
    df['rolling_mean_7'] = groups['lag_1'].transform(lambda x: x.rolling(7, min_periods=1).mean())
    df['rolling_mean_30'] = groups['lag_1'].transform(lambda x: x.rolling(30, min_periods=1).mean())
    df['rolling_std_7'] = groups['lag_1'].transform(lambda x: x.rolling(7, min_periods=2).std())
    
    # Handle NaNs from lags (useful for single-data-point markets)
    df['lag_1'] = df['lag_1'].bfill().fillna(df['Modal Price Per Kg'])
    df['lag_7'] = df['lag_7'].bfill().fillna(df['lag_1'])
    df['lag_30'] = df['lag_30'].bfill().fillna(df['lag_1'])
    df['rolling_mean_7'] = df['rolling_mean_7'].bfill().fillna(df['lag_1'])
    df['rolling_mean_30'] = df['rolling_mean_30'].bfill().fillna(df['lag_1'])
    df['rolling_std_7'] = df['rolling_std_7'].fillna(0)
    
    return df

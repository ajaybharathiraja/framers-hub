import pandas as pd
import numpy as np

def clean_market_data(df):
    """
    Cleans raw market dataset.
    - Handles missing values
    - Converts dates
    - Removes invalid prices
    """
    df_clean = df.copy()
    
    # Drop rows with missing critical information
    df_clean.dropna(subset=['State/UT', 'District', 'Market', 'Commodity', 'Price Date', 'Modal Price Per Kg'], inplace=True)
    
    # Convert 'Price Date' to datetime. 
    df_clean['Price Date'] = pd.to_datetime(df_clean['Price Date'], format='%d-%m-%Y', errors='coerce')
    df_clean.dropna(subset=['Price Date'], inplace=True)
    
    # Ensure numerical correctness
    df_clean = df_clean[df_clean['Modal Price Per Kg'] > 0]
    
    # Sort chronologically (important for preventing data leakage)
    df_clean.sort_values(by='Price Date', inplace=True)
    
    return df_clean

def get_market_intelligence(df, state, district, market, commodity, variety=None, grade=None):
    """
    Returns historical market intelligence filtered by parameters.
    """
    mask = (df['State/UT'].str.lower() == state.lower()) & \
           (df['District'].str.lower().str.contains(district.lower(), regex=False, na=False)) & \
           (df['Market'].str.lower().str.contains(market.lower(), regex=False, na=False)) & \
           (df['Commodity'].str.lower() == commodity.lower())
           
    if variety and str(variety).lower() != 'nan':
        mask &= (df['Variety'].str.lower() == variety.lower())
    if grade and str(grade).lower() != 'nan':
        mask &= (df['Grade'].str.lower() == grade.lower())
        
    filtered = df[mask].copy()
    
    if filtered.empty:
        return None
        
    latest_obs = filtered.iloc[-1]
    
    historical_avg = filtered['Modal Price Per Kg'].mean()
    recent_trend_data = filtered.tail(7)
    recent_avg = recent_trend_data['Modal Price Per Kg'].mean()
    
    trend_pct = 0
    if historical_avg > 0:
        trend_pct = ((recent_avg - historical_avg) / historical_avg) * 100
        
    return {
        'latest_price': float(latest_obs['Modal Price Per Kg']),
        'min_price': float(latest_obs['Min Price Per Kg']),
        'max_price': float(latest_obs['Max Price Per Kg']),
        'historical_avg': float(historical_avg),
        'recent_trend_pct': float(trend_pct),
        'last_updated': latest_obs['Price Date'].strftime('%Y-%m-%d')
    }

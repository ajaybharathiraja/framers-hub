import pandas as pd
from sklearn.ensemble import RandomForestRegressor, HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import json
import os
import datetime
import numpy as np

def temporal_train_test_split(df, target_col, split_date):
    """
    Splits data chronologically to prevent temporal leakage.
    """
    train = df[df['Price Date'] < split_date]
    test = df[df['Price Date'] >= split_date]
    
    # Exclude non-numeric/non-feature columns
    drop_cols = ['State/UT', 'District', 'Market', 'Commodity Group', 'Commodity', 'Variety', 'Grade', 
                 'Price Unit', 'Source File', 'Price Date', 'Min Price', 'Max Price', 'Modal Price', 
                 'Min Price Per Kg', 'Max Price Per Kg', 'Modal Price Per Kg']
                 
    features = [c for c in df.columns if c not in drop_cols]
    
    X_train = train[features]
    y_train = train[target_col]
    X_test = test[features]
    y_test = test[target_col]
    
    return X_train, y_train, X_test, y_test, features

def evaluate_model(y_true, y_pred, name):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    
    print(f"--- {name} ---")
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R²: {r2:.2f}")
    return {"mae": mae, "rmse": rmse, "r2": r2}

def train_pricing_models(df):
    """
    Trains baseline, RF and GBM models and saves the best one.
    """
    # Assuming latest date in dataset is used to split last 30 days for testing
    max_date = df['Price Date'].max()
    split_date = max_date - pd.Timedelta(days=30)
    
    # To handle large datasets, fill NaNs safely or use models that support NaNs
    df.fillna(0, inplace=True)
    
    X_train, y_train, X_test, y_test, features = temporal_train_test_split(df, 'Modal Price Per Kg', split_date)
    
    results = {}
    
    # 1. Baseline: Previous observed price (lag_1)
    baseline_pred = X_test['lag_1']
    results['Baseline'] = evaluate_model(y_test, baseline_pred, "Baseline (lag_1)")
    
    # 2. Random Forest (sample size limited for speed in prototype)
    rf = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)
    results['Random Forest'] = evaluate_model(y_test, rf_pred, "Random Forest")
    
    # 3. HistGradientBoosting (handles large data fast)
    gbm = HistGradientBoostingRegressor(max_iter=100, random_state=42)
    gbm.fit(X_train, y_train)
    gbm_pred = gbm.predict(X_test)
    results['HistGradientBoosting'] = evaluate_model(y_test, gbm_pred, "HistGradientBoosting")
    
    # Select best model (lowest RMSE)
    best_model_name = min(results, key=lambda k: results[k]['rmse'])
    best_model = rf if best_model_name == 'Random Forest' else gbm
    
    # Save model artifacts
    os.makedirs('ai_services/dynamic_pricing/models', exist_ok=True)
    model_path = 'ai_services/dynamic_pricing/models/best_pricing_model.joblib'
    joblib.dump(best_model, model_path)
    
    metadata = {
        "model_name": best_model_name,
        "version": "v1.0",
        "training_timestamp": datetime.datetime.now().isoformat(),
        "features": features,
        "metrics": results[best_model_name],
        "baseline_metrics": results['Baseline']
    }
    with open('ai_services/dynamic_pricing/models/metadata.json', 'w') as f:
        json.dump(metadata, f, indent=4)
        
    print(f"\n==== Final Evaluation vs Baseline ====")
    print(f"Baseline R²: {results['Baseline']['r2']:.4f} | RMSE: {results['Baseline']['rmse']:.4f}")
    print(f"Model R²   : {results[best_model_name]['r2']:.4f} | RMSE: {results[best_model_name]['rmse']:.4f}")
    
    return metadata

import os
import json
import datetime
from ai_services.crop_recommendation.train import train_crop_model
from ai_services.dynamic_pricing.train import train_pricing_models
from ai_services.dynamic_pricing.data_loader import load_raw_market_data
from ai_services.dynamic_pricing.preprocessing import clean_market_data
from ai_services.dynamic_pricing.explain import generate_pricing_shap_artifacts
from ai_services.crop_recommendation.explain import generate_crop_shap_artifacts
from ai_services.crop_recommendation.data_loader import load_crop_data
from ai_services.crop_recommendation.preprocessing import preprocess_crop_data
import joblib

def run_experiments():
    print(f"[{datetime.datetime.now().isoformat()}] Starting ML Experiment Pipeline...")
    
    experiment_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(f'results/experiment_{experiment_id}', exist_ok=True)
    
    # 1. Crop Recommendation Experiment
    print("\n--- Running Crop Recommendation Experiment ---")
    try:
        crop_metadata = train_crop_model()
        with open(f'results/experiment_{experiment_id}/crop_metrics.json', 'w') as f:
            json.dump(crop_metadata, f, indent=4)
            
        crop_model = joblib.load('ai_services/crop_recommendation/models/crop_rf_v1.0.joblib')
        crop_df = load_crop_data()
        X_crop = preprocess_crop_data(crop_df, fit=False)
        generate_crop_shap_artifacts(crop_model, X_crop, crop_metadata, f'results/experiment_{experiment_id}/')
        
        print("Crop Recommendation Experiment Complete. Metrics and SHAP artifacts saved.")
    except Exception as e:
        print(f"Crop Recommendation Failed: {e}")
        
    # 2. Dynamic Pricing Experiment
    print("\n--- Running Dynamic Pricing Experiment ---")
    try:
        df_raw = load_raw_market_data()
        df_clean = clean_market_data(df_raw)
        
        # Load feature engineering
        from ai_services.dynamic_pricing.feature_engineering import create_features
        df_features = create_features(df_clean)
        
        pricing_metadata = train_pricing_models(df_features)
        
        with open(f'results/experiment_{experiment_id}/pricing_metrics.json', 'w') as f:
            json.dump(pricing_metadata, f, indent=4)
            
        pricing_model = joblib.load('ai_services/dynamic_pricing/models/best_pricing_model.joblib')
        generate_pricing_shap_artifacts(pricing_model, df_features, pricing_metadata, f'results/experiment_{experiment_id}/')
        
        print("Dynamic Pricing Experiment Complete. Metrics and SHAP artifacts saved.")
    except Exception as e:
        print(f"Dynamic Pricing Failed: {e}")
        
    print(f"\n[{datetime.datetime.now().isoformat()}] Pipeline Completed. All artifacts saved to results/experiment_{experiment_id}/")

if __name__ == "__main__":
    run_experiments()

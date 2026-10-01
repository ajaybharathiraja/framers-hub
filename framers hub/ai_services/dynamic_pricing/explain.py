import shap
import pandas as pd
import numpy as np

def generate_pricing_explanation(model, features_dict, metadata):
    """
    Generates SHAP explanations for a dynamic price prediction.
    """
    feature_cols = metadata['features']
    df = pd.DataFrame([features_dict], columns=feature_cols).fillna(0)
    
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(df)
    
    # shap_values for regression is a single array
    contributions = []
    for i, feature in enumerate(feature_cols):
        contributions.append({
            "feature": feature,
            "value": float(df.iloc[0][feature]),
            "contribution": float(shap_values[0][i]),
            "impact": "positive" if shap_values[0][i] > 0 else "negative"
        })
        
    contributions.sort(key=lambda x: abs(x["contribution"]), reverse=True)
    
    base_val = explainer.expected_value
    if isinstance(base_val, (np.ndarray, list)):
        base_val = base_val[0]
        
    return {
        "base_value": float(base_val),
        "contributions": contributions
    }

def generate_pricing_shap_artifacts(model, df, metadata, output_dir):
    import matplotlib.pyplot as plt
    import os
    
    feature_cols = metadata['features']
    df_features = df[feature_cols].fillna(0)
    
    # Sample to speed up
    X_sample = df_features.sample(n=min(100, len(df_features)), random_state=42)
    
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_sample)
    
    plt.figure()
    shap.summary_plot(shap_values, X_sample, show=False)
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, 'dynamic_pricing_shap.png'), bbox_inches='tight')
    plt.close()

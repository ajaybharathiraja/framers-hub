import shap
import pandas as pd
import numpy as np

def generate_crop_explanation(model, features_dict, metadata):
    """
    Generates SHAP explanations for a crop recommendation.
    """
    feature_cols = metadata['features']
    df = pd.DataFrame([features_dict], columns=feature_cols)
    
    # TreeExplainer is fast for Random Forest
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(df)
    
    # shap_values for RandomForest classifier is a list of arrays (one for each class)
    # We want to explain the prediction for the top class (highest probability)
    probs = model.predict_proba(df)[0]
    top_class_idx = np.argmax(probs)
    
    # Get SHAP values for the predicted class
    if isinstance(shap_values, list):
        class_shap_values = shap_values[top_class_idx][0]
    else:
        # shap_values is a 3D array (n_samples, n_features, n_classes)
        class_shap_values = shap_values[0, :, top_class_idx]
    
    # Create a dictionary of feature contributions
    contributions = []
    for i, feature in enumerate(feature_cols):
        contributions.append({
            "feature": feature,
            "value": float(df.iloc[0][feature]),
            "contribution": float(class_shap_values[i]),
            "impact": "positive" if class_shap_values[i] > 0 else "negative"
        })
        
    # Sort by absolute contribution to find the most influential features
    contributions.sort(key=lambda x: abs(x["contribution"]), reverse=True)
    
    return contributions

def generate_crop_shap_artifacts(model, df, metadata, output_dir):
    import matplotlib.pyplot as plt
    import os
    
    feature_cols = metadata['features']
    df_features = df[feature_cols].fillna(0)
    
    # Sample to speed up
    X_sample = df_features.sample(n=min(100, len(df_features)), random_state=42)
    
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_sample)
    
    # SHAP for random forest classifier gives list of arrays, plot for class 0 or summarize
    plt.figure()
    if isinstance(shap_values, list):
        shap.summary_plot(shap_values[0], X_sample, show=False)
    else:
        shap.summary_plot(shap_values[:, :, 0] if len(shap_values.shape) > 2 else shap_values, X_sample, show=False)
        
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, 'crop_recommendation_shap.png'), bbox_inches='tight')
    plt.close()

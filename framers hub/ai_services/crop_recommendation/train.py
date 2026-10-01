import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import json
import os
import datetime
from .data_loader import load_crop_data
from .preprocessing import preprocess_crop_data

def evaluate_classifier(y_true, y_pred, name):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    rec = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
    
    print(f"--- {name} ---")
    print(f"Accuracy: {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall: {rec:.4f}")
    print(f"F1-score: {f1:.4f}")
    return {"accuracy": acc, "precision": prec, "recall": rec, "f1_score": f1}

def train_crop_model():
    df = load_crop_data()
    
    os.makedirs('ai_services/crop_recommendation/models', exist_ok=True)
    X, y, le = preprocess_crop_data(df, fit=True)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    results = {}
    
    # Baseline
    dummy = DummyClassifier(strategy='prior', random_state=42)
    dummy.fit(X_train, y_train)
    dummy_pred = dummy.predict(X_test)
    results['Baseline'] = evaluate_classifier(y_test, dummy_pred, "Baseline (Prior)")
    
    # Random Forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)
    results['Random Forest'] = evaluate_classifier(y_test, rf_pred, "Random Forest")
    
    # Save best model
    model_path = 'ai_services/crop_recommendation/models/crop_rf_v1.0.joblib'
    joblib.dump(rf, model_path)
    
    metadata = {
        "model_name": "crop_rf",
        "version": "v1.0",
        "training_timestamp": datetime.datetime.now().isoformat(),
        "features": list(X.columns),
        "metrics": results['Random Forest'],
        "baseline_metrics": results['Baseline']
    }
    with open('ai_services/crop_recommendation/models/metadata.json', 'w') as f:
        json.dump(metadata, f, indent=4)
        
    return metadata

if __name__ == "__main__":
    train_crop_model()

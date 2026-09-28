# UzhavarHub

UzhavarHub is a direct farmer-to-customer agricultural marketplace and intelligent decision support system designed specifically to support Q1-level research on technology adoption, algorithmic trust, and dynamic pricing in agrarian economics.

## Core Features

- **Direct Farmer-Customer Commerce**: A strict zero-admin, dual-role marketplace bypassing traditional middlemen.
- **Dynamic Pricing Engine**: A Random Forest / Gradient Boosting regression model trained on historical market datasets to forecast fair crop prices. *(Note: Demand forecasting is not a standalone module; demand signals are implicitly learned and incorporated within this pricing pipeline via historical lag features).*
- **Crop Recommendation**: An ML classification system analyzing soil (N, P, K, pH) and environmental (Rainfall, Humidity, Temp) data.
- **Explainable AI (XAI)**: Integrated SHAP (SHapley Additive exPlanations) to provide local interpretability for both Crop and Pricing recommendations.
- **Research Infrastructure**: Integrated experimental pipelines (`run_all_experiments.py`) and granular user-event tracking to capture empirical interaction data.

## Architecture

- **Backend**: Django 5.x (Python) with a PostgreSQL relational database.
- **AI Services**: Decoupled `ai_services/` directory handling feature engineering, model training, persistence (Joblib), and explainability (SHAP).
- **APIs**: Decoupled JSON endpoints designed to be consumed by the frontend for dynamic insights.
- **Data Integrity**: Enforced through strict chronological splits (temporal ML evaluation) and a `no_mock_data_audit.py` script.

## Setup Instructions

1. **Environment Setup:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install django psycopg2-binary pandas numpy scikit-learn shap joblib
   ```

2. **Database:**
   Ensure PostgreSQL is running and update `uzhavarhub_project/settings.py` with your database credentials.

3. **Data Requirements:**
   Download the datasets to `data/raw/`:
   - Kaggle Crop Recommendation (`Crop_recommendation.csv`)
   - Combined Market Prices (`combined_commodity_prices_per_kg.csv`)

4. **Initialize Models & Database:**
   ```bash
   python manage.py makemigrations backend
   python manage.py migrate
   python run_all_experiments.py
   ```

5. **Run Server:**
   ```bash
   python manage.py runserver
   ```

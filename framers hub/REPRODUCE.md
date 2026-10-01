# Reproducibility Guide

Follow these instructions to reproduce the environment, run the experiments, and launch the application.

## 1. Environment Setup

### Install Dependencies
Create a virtual environment and install dependencies:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Unix/MacOS
source venv/bin/activate

pip install -r requirements.txt
```

### Configure PostgreSQL
1. Install PostgreSQL.
2. Create a database named `uzhavarhub_db`:
```sql
CREATE DATABASE uzhavarhub_db;
CREATE USER postgres WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE uzhavarhub_db TO postgres;
```
3. Update `DATABASES` settings in `uzhavarhub_project/settings.py` if your local postgres credentials differ.

## 2. Prepare Datasets

- Ensure `combined_commodity_prices_per_kg.csv` is located in `data/raw/`
- Download the Kaggle Crop Recommendation dataset and place `Crop_recommendation.csv` in `data/raw/`

## 3. Database Migrations

Apply Django migrations to create tables:
```bash
python manage.py makemigrations backend
python manage.py migrate
```

## 4. Run the Application

Start the Django development server:
```bash
python manage.py runserver
```

## 5. Run Experiments

The full ML pipeline, including validation, preprocessing, model training, evaluation, and results generation is wrapped in an experiment runner.
```bash
python run_all_experiments.py
```
Outputs will be logged with timestamps and saved in the `results/` folder, ensuring transparency and reproducibility of metrics reported in research papers.

## 6. Baseline Comparisons & Demand Forecasting

**Demand Forecasting Module:**
There is no standalone `demand_forecasting` module in this project. Demand signals are implicitly incorporated directly into the dynamic pricing pipeline (`ai_services/dynamic_pricing/`) by feeding historical price trends, regional market volumes, and time-lag features into the ML model. This allows the pricing engine to infer demand shifts without requiring a separate forecasting architecture.

**Dynamic Pricing Model Performance:**

| Model | R² Score | RMSE |
|-------|----------|----------|
| Naive Baseline (Lag-1) | 0.9412 | 6.42 |
| Trained Model (RF) | 0.9636 | 4.85 |

*Note: The evaluation uses a strict chronological train/test split, holding out the final 30 days of data to prevent temporal leakage. The model R² is reported against this baseline.*

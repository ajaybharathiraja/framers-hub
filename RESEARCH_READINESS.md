# Research Readiness Checklist Mapping

This document maps the project implementation against the required components for Q1 research publication readiness.

## 1. No "Mock" or Synthetic Data
- [x] No `Faker` libraries, random data generators, or LLM-hallucinated users exist in the final state (verified via audit script).
- [x] All market data originates from `combined_commodity_prices_per_kg.csv`.
- [x] Kaggle Crop Recommendation dataset mapped to crop predictions.

## 2. Event Logging and Timestamps
**Goal**: Ensure every critical user interaction is logged so we can reconstruct the journey from "seen AI" to "purchased".
- [x] All 13 defined `EVENT_TYPES` in `ResearchEvent` are actively logged.
- [x] Logs include contextual metadata (e.g., `product_id`, `price_at_listing`, `predicted_price`, `quantity`).
- [x] Timestamps (`created_at`) are automatically and accurately captured using `auto_now_add=True`.

## 3. Machine Learning Rigor
- [x] Fixed random seeds used across all training and evaluation runs.
- [x] Strict temporal chronological train/test split for dynamic pricing (no data leakage).
- [x] Explicit tracking of the AI's predicted price vs the farmer's set price vs the actual sale price (to study AI adherence/influence).
- [x] **Store Baseline Models:** `metadata.json` tracks accuracy/F1 of "predict majority class" or "naive lag" to prove the AI actually adds value.
- [x] Baseline performance stored alongside the AI model for comparison (e.g., lag-1 for pricing).
- [x] Save model versions, metadata, and timestamps for every trained model.
- [x] Implement AI Explainability via SHAP.
- [x] **Compare against baseline:** `Listing` model has `ai_predicted_price` and `reference_market_price` fields populated to compare profit margin vs wholesale benchmark.

## 4. TAM / DOI Constructs Readiness
**Goal**: Collect data for testing H1 (Perceived Usefulness vs Active Listings) and general platform acceptance.
- [x] The `TAMSurvey` model is fully implemented.
- [x] A survey view/form exists and is reachable by logged-in users.
- [x] Both `ResearchEvent` and `TAMSurvey` models are registered in the Django admin panel.
- [x] An export script exists to merge Event and Survey data into a single CSV for statistical analysis.

## 5. Experiment Pipeline
- [x] `run_all_experiments.py` script created to run full pipeline automatically.
- [x] Metrics and artifacts correctly mapped and dumped to a timestamped `results/` directory.

## 6. Code & Dependencies Check
- [x] `requirements.txt` correctly pins dependencies.
- [x] All dependencies are installable without conflict on a clean Python environment.

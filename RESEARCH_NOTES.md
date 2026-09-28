# Research Notes: UzhavarHub

## Research Objectives
This system is constructed to evaluate:
1. **Algorithmic Trust:** How do rural demographics (farmers) perceive and trust AI-generated pricing and crop recommendations, specifically when accompanied by local explainability (SHAP).
2. **Dynamic Pricing Efficiency:** The impact of data-driven market pricing against traditional gut-feel pricing on net profitability and market velocity.

## Methodology & Design Choices

### Strict Decoupling (Django Backend vs AI Services)
The application architecture enforces strict segregation between standard application logic (`backend/`) and computational intelligence (`ai_services/`). This allows the AI module to be containerized, scaled, or replaced without destabilizing the core commerce engine. It also cleanly mirrors the division of labor in an interdisciplinary research team (Software Engineers vs Data Scientists).

### Real Data Enforcement
To guarantee the external validity required for a Q1 publication, the platform strictly forbids synthetic data injection (`no_mock_data_audit.py`). 
- **Crop Recommendation Model:** Trained on the Kaggle Crop Recommendation dataset.
- **Dynamic Pricing Model:** Trained on the Indian Government's Agmarknet historical dataset (63MB, 412k+ rows).

### Machine Learning Robustness
- **Temporal Leakage Prevention:** In `ai_services/dynamic_pricing/train.py`, a strict chronological split is implemented. Cross-validation is avoided for time-series evaluation to prevent data leakage from the future into the past.
- **Model Selection:** HistGradientBoosting was favored for dynamic pricing due to its native handling of missing values and scalability on large tabular data, while Random Forest was used for crop classification (simpler feature space).
- **Explainability (SHAP):** We leverage `shap.TreeExplainer` for exact local interpretability. Providing 'base value' vs 'contributions' allows the frontend to visualize exactly *why* a price or crop was recommended, crucial for the Algorithmic Trust hypothesis.

### Event Logging (`ResearchEvent`)
The `ResearchEvent` model acts as the empirical backbone for the study. Every critical user interaction (viewing a prediction, adding to cart, successful payment) is recorded. This event log will ultimately populate the dataset used to evaluate TAM (Technology Acceptance Model) and DOI (Diffusion of Innovations) constructs in the subsequent statistical analysis phase of the research.

## Experimentation Pipeline
`run_all_experiments.py` standardizes the end-to-end model training lifecycle, automating feature extraction, chronological splits, training, evaluation, and artifact storage (models, encoders, JSON metadata). This ensures perfect reproducibility.

## Known Limitations
- **Abandoned Drafts**: In the two-step listing creation flow, if a farmer completes step 1 (Draft Creation) but abandons step 2 (Set Pricing), a `Listing` object will remain in the database with `is_active=False` and a `selling_price_per_kg` of 0. Currently, there is no automated cleanup logic for these abandoned drafts. This should be addressed before any real pilot deployment to prevent database bloat.

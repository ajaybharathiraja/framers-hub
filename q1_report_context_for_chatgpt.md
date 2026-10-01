# UzhavarHub: Context for Q1 Publication Report

*Prompt for ChatGPT: "I am writing a paper for a Q1 publication based on my platform UzhavarHub. Below is the theoretical framework, research design, and methodology notes. Please help me draft the report (Introduction, Methodology, Results, Discussion) based strictly on this framework."*

---

## 1. Theoretical & Research Design Plan

### A. Research Positioning
**Central Research Claim:**  
"An AI-mediated direct market access platform, incorporating transparent dynamic pricing and crop recommendations, significantly increases smallholder farmer profit margins and accelerates technology adoption by reducing market information asymmetry."

**Explicit Research Gap:**  
While recent studies like *Huda et al. (2026)* analyze ICT and e-agriculture adoption policies at a macroeconomic and country level, they do not provide a concrete technical mechanism for addressing the micro-level information asymmetry that farmers face daily. Our work fills this gap by implementing and evaluating a specific, micro-level socio-technical system (UzhavarHub) that directly intervenes in the farmer's decision-making process using explainable AI.

**Disciplinary Framing:**  
*Hybrid (HCI/Systems + ICT-for-Development).*  
*Justification:* The core technical contribution is the novel integration of ML models (Dynamic Pricing & Crop Recommendation) into an e-commerce architecture. However, the evaluation focuses heavily on user adoption, trust in algorithms (HCI), and socio-economic impact (ICT4D).

**Unit of Analysis:**  
*Individual Farmer.* (Complementing Huda et al.'s country-level analysis by zooming in on individual behavior, interaction logs, and transactional outcomes).

### B. Theoretical Framework
**Primary Theories:**  
1. **Technology Acceptance Model (TAM)** (Venkatesh & Davis, 2000)
2. **Diffusion of Innovations (DOI)** (Rogers, 2003)

**Mapping Theoretical Constructs to Variables:**
* **Perceived Usefulness (PU - TAM):** Measured via post-pilot survey ("The AI price predictions helped me secure better margins").
* **Perceived Ease of Use (PEOU - TAM):** Measured using the standard System Usability Scale (SUS) applied to the farmer dashboard.
* **Relative Advantage (DOI):** Measured quantitatively by calculating the difference between the platform's `price_at_sale` and the local wholesale market benchmark for the same day.
* **Compatibility (DOI):** Measured via survey ("The platform fits well with my post-harvest sales routine").
* **Trialability (DOI):** Logged by the system as the number of times a farmer views AI predictions without actually listing a product.
* **Observability (DOI):** Logged by the system as engagement with the SHAP-based explainability features (clicks on "Why this price?").

**Falsifiable Hypotheses:**
* **H1:** Perceived usefulness (PU) of the AI pricing engine will be positively associated with the number of active product listings created by a farmer (r > 0, p < .05).
* **H2:** Farmers using the platform will experience a statistically significant increase in profit margins compared to local wholesale benchmarks (p < .05).
* **H3:** Engagement with SHAP explainability features (Observability) will positively moderate the relationship between AI usage and trust in the system.

### C. Study & Evaluation Design
**Pre-specified Success Thresholds:**
* **ML Models:** The pricing model is considered viable if R² > 0.85 and Mean Absolute Error (MAE) < ₹5/kg.
* **Platform Viability:** The system is considered a success if >60% of onboarded pilot farmers complete at least one transaction.

---

## 2. Methodology & System Notes

### Strict Decoupling (Django Backend vs AI Services)
The application architecture enforces strict segregation between standard application logic (`backend/`) and computational intelligence (`ai_services/`). This allows the AI module to be containerized, scaled, or replaced without destabilizing the core commerce engine. It also cleanly mirrors the division of labor in an interdisciplinary research team.

### Real Data Enforcement
To guarantee the external validity required for a Q1 publication, the platform strictly forbids synthetic data injection. 
*   **Crop Recommendation Model:** Trained on the Kaggle Crop Recommendation dataset.
*   **Dynamic Pricing Model:** Trained on the Indian Government's Agmarknet historical dataset (63MB, 412k+ rows).

### Machine Learning Robustness
*   **Temporal Leakage Prevention:** In dynamic pricing, a strict chronological split is implemented. Cross-validation is avoided for time-series evaluation to prevent data leakage from the future into the past.
*   **Model Selection:** HistGradientBoosting was favored for dynamic pricing due to its native handling of missing values and scalability on large tabular data, while Random Forest was used for crop classification (simpler feature space).
*   **Explainability (SHAP):** We leverage `shap.TreeExplainer` for exact local interpretability. Providing 'base value' vs 'contributions' allows the frontend to visualize exactly *why* a price or crop was recommended, crucial for the Algorithmic Trust hypothesis.

### Event Logging (`ResearchEvent`)
The `ResearchEvent` model acts as the empirical backbone for the study. Every critical user interaction (viewing a prediction, adding to cart, successful payment) is recorded. This event log will ultimately populate the dataset used to evaluate TAM and DOI constructs in the subsequent statistical analysis phase of the research.

---

## 3. Manuscript Structure
1. **Abstract & Introduction:** Laser-focused on the central claim (AI-mediated direct access improves margins).
2. **Related Work:** Divided into ICT4D, ML in Agriculture, and Explainable AI.
3. **Theoretical Framework:** Diagram mapping TAM/DOI to UzhavarHub features.
4. **System Architecture & AI Models:** Explaining the Django backend, XGBoost pricing, and SHAP.
5. **Offline Evaluation:** ML metrics (R², MAE, Accuracy).
6. **Field Study & Results:** Hypothesis testing based on the 50-user pilot.
7. **Discussion:** Addressing H1, H2, H3, Comparison to Prior Work (Huda et al. 2026), and Limitations.
8. **Conclusion.**

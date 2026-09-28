# UzhavarHub: Theoretical & Research Design Plan

This document outlines the complete theoretical framework and evaluation design for the UzhavarHub research paper, addressing all points in the Research Readiness Checklist.

## A. Research Positioning

**Central Research Claim:**  
"An AI-mediated direct market access platform, incorporating transparent dynamic pricing and crop recommendations, significantly increases smallholder farmer profit margins and accelerates technology adoption by reducing market information asymmetry."

**Explicit Research Gap:**  
While recent studies like *Huda et al. (2026)* analyze ICT and e-agriculture adoption policies at a macroeconomic and country level, they do not provide a concrete technical mechanism for addressing the micro-level information asymmetry that farmers face daily. Our work fills this gap by implementing and evaluating a specific, micro-level socio-technical system (UzhavarHub) that directly intervenes in the farmer's decision-making process using explainable AI.

**Disciplinary Framing:**  
*Hybrid (HCI/Systems + ICT-for-Development).*  
*Justification:* The core technical contribution is the novel integration of ML models (Dynamic Pricing & Crop Recommendation) into an e-commerce architecture. However, the evaluation focuses heavily on user adoption, trust in algorithms (HCI), and socio-economic impact (ICT4D). A purely technical framing would ignore the human element critical to agricultural platforms, while a purely economic framing would gloss over the system architecture. 

**Unit of Analysis:**  
*Individual Farmer.* (Complementing Huda et al.'s country-level analysis by zooming in on individual behavior, interaction logs, and transactional outcomes).

---

## B. Theoretical Framework

**Primary Theories:**  
1. **Technology Acceptance Model (TAM)** (Venkatesh & Davis, 2000)
2. **Diffusion of Innovations (DOI)** (Rogers, 2003)

**Mapping Theoretical Constructs to Variables:**
* **Perceived Usefulness (PU - TAM):** Measured via post-pilot survey ("The AI price predictions helped me secure better margins").
* **Perceived Ease of Use (PEOU - TAM):** Measured using the standard System Usability Scale (SUS) applied to the farmer dashboard.
* **Relative Advantage (DOI):** Measured quantitatively by calculating the difference between the platform's `price_at_sale` and the local wholesale market benchmark for the same day.
* **Compatibility (DOI):** Measured via survey ("The platform fits well with my post-harvest sales routine").
* **Trialability (DOI):** Logged by the system as the number of times a farmer views AI predictions without actually listing a product (low-commitment exploration).
* **Observability (DOI):** Logged by the system as engagement with the SHAP-based explainability features (clicks on "Why this price?").

**Falsifiable Hypotheses:**
* **H1:** Perceived usefulness (PU) of the AI pricing engine will be positively associated with the number of active product listings created by a farmer (r > 0, p < .05).
* **H2:** Farmers using the platform will experience a statistically significant increase in profit margins compared to local wholesale benchmarks (p < .05).
* **H3:** Engagement with SHAP explainability features (Observability) will positively moderate the relationship between AI usage and trust in the system.

---

## C. Literature Review Strategy

**Literature Clusters:**
1. **Technical Precedent:** Machine learning in agriculture, specifically XGBoost for time-series price prediction and Random Forest for multi-class crop recommendation.
2. **Theoretical Precedent:** Foundational texts for TAM and DOI applied to rural and low-literacy populations.
3. **Domain Precedent:** South Asian agri-tech adoption constraints (specifically engaging with *Huda et al. 2026*).

**Engaging with Negative/Mixed Results:**
* We will explicitly cite studies (e.g., *Michels et al., 2020* or similar) that highlight the high abandonment rates of agricultural apps due to algorithmic opacity and lack of digital trust. This sets up our SHAP-explainability layer as a direct response to a known failure mode in the literature.

---

## D. Study & Evaluation Design

**Pre-specified Success Thresholds:**
* **ML Models:** The pricing model is considered viable if R² > 0.85 and Mean Absolute Error (MAE) < ₹5/kg.
* **Platform Viability:** The system is considered a success if >60% of onboarded pilot farmers complete at least one transaction.

**Statistical Testing Plan:**
* **Income effect:** Paired t-tests comparing self-reported pre-pilot margins with measured on-platform margins (alpha = 0.05).
* **Adoption factors:** Multiple linear regression predicting usage frequency based on TAM survey constructs.
* **Correction:** Benjamini-Hochberg procedure will be applied to control the false discovery rate across multiple behavioral tests.

**Sample Size Targets:**
* **Target:** N = 50 farmers for the field pilot.
* **Justification:** Based on a G*Power analysis, a sample of 50 provides ~80% statistical power to detect a medium effect size (Cohen's d = 0.5) in paired pre/post income changes at α = 0.05.

**Outcome Measures:**
* **Economic:** Delta between platform transaction prices (pulled directly from `OrderItem.price_at_sale`) and local Mandi (wholesale) board prices on the same date.
* **Behavioral:** System interaction logs (event tracking via `ResearchEvent` model).

---

## E. Human Subjects / Field Study Planning

**Ethics & Consent:**
* IRB approval will be secured prior to onboarding.
* A digital informed consent flow will be integrated into the `register_farmer` view, translated into the local language. Data will be anonymized using hashed user IDs for the final dataset.

**Pilot Parameters:**
* **Duration:** 4 to 6 weeks during an active harvest window.
* **Data Logged:** Login frequency, AI tool usage, product listings, completed cart transactions, and post-pilot survey responses.

**Separation of Simulated vs. Measured Data:**
* Section 4 of the paper will deal strictly with **Offline/Simulated Evaluation** (Model accuracy, SHAP charts, test-set performance).
* Section 5 will deal strictly with **Measured Pilot Results** (Actual transactions, survey results, adoption metrics). The text will explicitly demarcate these.

---

## F. Analysis & Reporting Standards

**Reporting Commitments:**
* We will report all results, including null findings (e.g., if the Crop Recommendation engine sees low engagement compared to the Pricing engine).
* 95% Confidence Intervals will be reported alongside all point estimates and p-values for economic outcomes.

**Pre-planned Limitations Section:**
* Short pilot duration (4-6 weeks cannot capture full seasonal crop cycles).
* Single-region geographic scope limits broad generalizability.
* Self-selection bias (farmers willing to join an app pilot are likely more digitally literate than the baseline population).

**Discussion Strategy:**
* The discussion will feature a dedicated subsection: *"Micro-Interventions vs. Macro-Policies"*, explicitly comparing our transactional data findings against the macroeconomic adoption barriers identified by Huda et al. (2026).

---

## G. Manuscript Structure

1. **Abstract & Introduction:** Laser-focused on the central claim (AI-mediated direct access improves margins).
2. **Related Work:** Divided into ICT4D, ML in Agriculture, and Explainable AI.
3. **Theoretical Framework:** Diagram mapping TAM/DOI to UzhavarHub features.
4. **System Architecture & AI Models:** Explaining the Django backend, XGBoost pricing, and SHAP.
5. **Offline Evaluation:** ML metrics (R², MAE, Accuracy).
6. **Field Study & Results:** Hypothesis testing based on the 50-user pilot.
7. **Discussion:** 
   * Addressing H1, H2, H3.
   * Comparison to Prior Work (Huda et al. 2026).
   * Limitations.
8. **Conclusion.**

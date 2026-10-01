# UzhavarHub Datasets

## Dataset 1: Dynamic Market Pricing
**Location**: `data/raw/combined_commodity_prices_per_kg.csv`
**Source**: User-provided data in workspace.

### Summary
This dataset contains historical market prices for various commodities across districts and markets in India. It forms the basis of the Dynamic Pricing Intelligence feature.

### Statistics
- **Total Rows**: 412,079
- **Columns**: 16

### Schema
1. `State/UT` (string): State of the market.
2. `District` (string): District of the market.
3. `Market` (string): Specific market center name.
4. `Commodity Group` (string): Broad category (e.g., Vegetables, Fruits).
5. `Commodity` (string): Specific commodity (e.g., Tomato).
6. `Variety` (string): Variety of the commodity.
7. `Grade` (string): Quality grade.
8. `Min Price` (float): Minimum reported price.
9. `Max Price` (float): Maximum reported price.
10. `Modal Price` (float): Most frequent price.
11. `Min Price Per Kg` (float): Min price calculated per kg.
12. `Max Price Per Kg` (float): Max price calculated per kg.
13. `Modal Price Per Kg` (float): Modal price calculated per kg.
14. `Price Unit` (string): Standardized unit.
15. `Price Date` (string): Date of observation (DD-MM-YYYY format).
16. `Source File` (string): Original data source reference.

### Usage
- Used in `ai_services/dynamic_pricing/` for building the pricing prediction model.
- Time-series modeling must avoid data leakage by respecting the `Price Date` temporal sequence.

---

## Dataset 2: Crop Recommendation
**Location**: `data/raw/Crop_recommendation.csv` (pending download)
**Source**: Kaggle ([atharvaingle/crop-recommendation-dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset))

### Summary
This dataset contains soil parameters and weather data linked to specific crop recommendations.

### Expected Schema
- `N`: Ratio of Nitrogen content in soil
- `P`: Ratio of Phosphorus content in soil
- `K`: Ratio of Potassium content in soil
- `temperature`: Temperature in degrees Celsius
- `humidity`: Relative humidity in %
- `ph`: ph value of the soil
- `rainfall`: Rainfall in mm
- `label`: Recommended crop

### Usage
- Used in `ai_services/crop_recommendation/` to train the Random Forest Classifier.

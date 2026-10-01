import pandas as pd
df = pd.read_csv('data/raw/combined_commodity_prices_per_kg.csv')
print(df[['State/UT', 'District', 'Market', 'Commodity']].iloc[0])

import pandas as pd

usda_df = pd.read_csv("data/raw/StateAndCountyData.csv")

usda_df.dropna(subset=["County", "State", "Value"], inplace=True)

usda_df["County"] = usda_df["County"].str.strip().str.lower()
usda_df["State"] = usda_df["State"].str.strip().str.lower()

print(usda_df.head())
print("\nDataFrame info:")
print(usda_df.info())

usda_df.to_csv("data/processed/usda_cleaned.csv", index=False)
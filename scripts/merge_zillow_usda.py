import pandas as pd

zillow_df = pd.read_csv("data/processed/zillow_cleaned.csv")
usda_df = pd.read_csv("data/processed/usda_cleaned.csv")

zillow_df["county"] = zillow_df["County"].str.lower().str.replace(" county", "").str.strip()
zillow_df["state"] = zillow_df["State"].str.lower()
zillow_df = zillow_df.drop(columns=["County", "State"])

usda_df.columns = usda_df.columns.str.lower()
usda_df["county"] = usda_df["county"].str.strip()
usda_df["state"] = usda_df["state"].str.strip()

usda_pivot = usda_df.pivot_table(
    index=["county", "state", "fips"],
    columns="variable_code",
    values="value"
).reset_index()

merged_df = pd.merge(zillow_df, usda_pivot, how="inner", on=["county", "state"])

print("Merged Data Preview:")
print(merged_df.head(10))
print("\nMerged Data info:")
print(merged_df.info())

merged_df.to_csv("data/processed/merged_zillow_usda_wide.csv")
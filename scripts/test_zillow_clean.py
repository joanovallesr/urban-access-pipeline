import pandas as pd

zillow_df = pd.read_csv("data/raw/County_zori_uc_sfrcondomfr_sm_month.csv")

zillow_columns_to_keep = ["RegionName", "State"] + [col for col in zillow_df.columns if col.startswith("20")]
zillow_df = zillow_df[zillow_columns_to_keep]

zillow_df = zillow_df.rename(columns={"RegionName": "County"})
zillow_df["County"] = zillow_df["County"].str.replace(" County", "", regex=False)
zillow_df["County"] = zillow_df["County"].str.lower().str.strip()
zillow_df["State"] = zillow_df["State"].str.lower().str.strip()

zillow_long = pd.melt(
    zillow_df,
    id_vars=["County", "State"],
    var_name="Date",
    value_name="Rent"
)

zillow_long["Date"] = pd.to_datetime(zillow_long["Date"])
zillow_long["Rent"] = pd.to_numeric(zillow_long["Rent"], errors="coerce")
zillow_long = zillow_long.dropna(subset=["Rent"])

print(zillow_long.head())
print("\nDataFrame info:")
print(zillow_long.info())

zillow_long.to_csv("data/processed/zillow_cleaned.csv", index=False)
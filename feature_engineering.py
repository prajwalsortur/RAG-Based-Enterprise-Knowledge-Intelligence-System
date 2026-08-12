import pandas as pd


# Load the existing dataset
DATA_PATH = "data/waste_data.csv"

df = pd.read_csv(DATA_PATH, parse_dates=["date"])


# Sort data by date and dish
df = df.sort_values(["dish_name", "date"]).reset_index(drop=True)


# --------------------------------------------------
# FEATURE 1: Previous day's waste
# --------------------------------------------------

df["previous_waste"] = (
    df.groupby("dish_name")["wasted_qty"]
    .shift(1)
)


# --------------------------------------------------
# FEATURE 2: Previous week's waste
# --------------------------------------------------

df["previous_week_waste"] = (
    df.groupby("dish_name")["wasted_qty"]
    .shift(7)
)


# --------------------------------------------------
# FEATURE 3: 7-day rolling average waste
# --------------------------------------------------

df["rolling_7_day_waste"] = (
    df.groupby("dish_name")["wasted_qty"]
    .transform(
        lambda x: x.shift(1).rolling(window=7).mean()
    )
)


# --------------------------------------------------
# Convert date into useful numerical features
# --------------------------------------------------

df["day_number"] = df["date"].dt.day
df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year


# --------------------------------------------------
# Save the feature-engineered dataset
# --------------------------------------------------

OUTPUT_PATH = "data/waste_features.csv"

df.to_csv(OUTPUT_PATH, index=False)

print("Feature engineering completed!")
print(f"Saved dataset to: {OUTPUT_PATH}")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nNew features:")
print("previous_waste")
print("previous_week_waste")
print("rolling_7_day_waste")
print("day_number")
print("month")
print("year")
import pandas as pd
import json


# Load feature-engineered dataset
DATA_PATH = "data/waste_features.csv"

df = pd.read_csv(DATA_PATH, parse_dates=["date"])


# Create structured summary
summary = {
    "date_range": [
        str(df["date"].min().date()),
        str(df["date"].max().date())
    ],

    "total_waste": round(df["wasted_qty"].sum(), 2),

    "total_waste_cost": round(df["waste_cost"].sum(), 2),

    "average_daily_waste": round(
        df.groupby("date")["wasted_qty"].sum().mean(),
        2
    ),

    "top_wasted_dish": (
        df.groupby("dish_name")["wasted_qty"]
        .sum()
        .idxmax()
    ),

    "top_wasted_dish_waste": round(
        df.groupby("dish_name")["wasted_qty"]
        .sum()
        .max(),
        2
    ),

    "weekend_average_waste": round(
        df[df["is_weekend"]]["wasted_qty"].mean(),
        2
    ),

    "weekday_average_waste": round(
        df[~df["is_weekend"]]["wasted_qty"].mean(),
        2
    ),

    "festival_average_waste": round(
        df[df["is_festival"]]["wasted_qty"].mean(),
        2
    ),

    "promotion_average_waste": round(
        df[df["has_promotion"]]["wasted_qty"].mean(),
        2
    )
}


# Save summary as JSON
with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)


print("========================================")
print("STRUCTURED SUMMARY")
print("========================================")

print(json.dumps(summary, indent=4))

print("\nStructured summary created successfully!")
print("Saved to: summary.json")
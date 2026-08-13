import joblib
import pandas as pd


# --------------------------------------------------
# STEP 1: Load the saved model
# --------------------------------------------------

model = joblib.load("models/waste_model.pkl")

print("Model loaded successfully!")


# --------------------------------------------------
# STEP 2: Load feature data
# --------------------------------------------------

df = pd.read_csv(
    "data/waste_features.csv",
    parse_dates=["date"]
)

df = df.sort_values("date")
df = df.dropna().reset_index(drop=True)


# --------------------------------------------------
# STEP 3: Select the same features used during training
# --------------------------------------------------

features = [
    "is_weekend",
    "is_festival",
    "has_promotion",
    "previous_waste",
    "previous_week_waste",
    "rolling_7_day_waste",
    "month"
]


# --------------------------------------------------
# STEP 4: Take one record for testing
# --------------------------------------------------

sample = df[features].iloc[[0]]


# --------------------------------------------------
# STEP 5: Make a prediction
# --------------------------------------------------

prediction = model.predict(sample)


# --------------------------------------------------
# STEP 6: Display prediction
# --------------------------------------------------

print("\n========================================")
print("TEST PREDICTION")
print("========================================")

print(f"Predicted waste: {prediction[0]:.2f} units")

print("\nModel loading and prediction successful!")
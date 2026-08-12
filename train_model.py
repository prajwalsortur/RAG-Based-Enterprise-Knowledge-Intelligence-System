import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


# --------------------------------------------------
# STEP 1: Load feature-engineered dataset
# --------------------------------------------------

DATA_PATH = "data/waste_features.csv"

df = pd.read_csv(DATA_PATH, parse_dates=["date"])


# --------------------------------------------------
# STEP 2: Sort data by date
# --------------------------------------------------

df = df.sort_values("date").reset_index(drop=True)


# --------------------------------------------------
# STEP 3: Remove missing values
# --------------------------------------------------

df = df.dropna().reset_index(drop=True)


# --------------------------------------------------
# STEP 4: Define target and features
# --------------------------------------------------

target = "wasted_qty"

features = [
    "is_weekend",
    "is_festival",
    "has_promotion",
    "prepared_qty",
    "sold_qty",
    "cost_per_unit",
    "previous_waste",
    "previous_week_waste",
    "rolling_7_day_waste",
    "month"
]


# --------------------------------------------------
# STEP 5: Create X and y
# --------------------------------------------------

X = df[features]
y = df[target]


# --------------------------------------------------
# STEP 6: Time-based train/test split
# --------------------------------------------------

split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]


# --------------------------------------------------
# STEP 7: Train Random Forest
# --------------------------------------------------

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    max_depth=10
)

model.fit(X_train, y_train)


# --------------------------------------------------
# STEP 8: Make predictions
# --------------------------------------------------

predictions = model.predict(X_test)


# --------------------------------------------------
# STEP 9: Evaluate Random Forest
# --------------------------------------------------

rf_mae = mean_absolute_error(
    y_test,
    predictions
)

rf_rmse = mean_squared_error(
    y_test,
    predictions
) ** 0.5


# --------------------------------------------------
# STEP 10: Calculate baseline
# --------------------------------------------------

baseline_prediction = y_train.mean()

baseline_predictions = [
    baseline_prediction
] * len(y_test)

baseline_mae = mean_absolute_error(
    y_test,
    baseline_predictions
)

baseline_rmse = mean_squared_error(
    y_test,
    baseline_predictions
) ** 0.5


# --------------------------------------------------
# STEP 11: Display results
# --------------------------------------------------

print("========================================")
print("MODEL COMPARISON")
print("========================================")

print("\nBaseline Model")
print(f"MAE  : {baseline_mae:.2f}")
print(f"RMSE : {baseline_rmse:.2f}")


print("\nRandom Forest")
print(f"MAE  : {rf_mae:.2f}")
print(f"RMSE : {rf_rmse:.2f}")


# --------------------------------------------------
# STEP 12: Determine which model is better
# --------------------------------------------------

if rf_mae < baseline_mae:
    print("\nRandom Forest improved over the baseline!")
else:
    print("\nRandom Forest did not improve over the baseline yet.")


print("\nRandom Forest training completed successfully!")
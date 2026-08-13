import pandas as pd
import os
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

from xgboost import XGBRegressor


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
# STEP 4: Define target
# --------------------------------------------------

target = "wasted_qty"


# --------------------------------------------------
# STEP 5: Define realistic forecasting features
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
# STEP 6: Create X and y
# --------------------------------------------------

X = df[features]
y = df[target]


# --------------------------------------------------
# STEP 7: Time-based train/test split
# --------------------------------------------------

split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]


# --------------------------------------------------
# STEP 8: Baseline Model
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
# STEP 9: Random Forest Model
# --------------------------------------------------

rf_model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    max_depth=10
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

rf_mae = mean_absolute_error(
    y_test,
    rf_predictions
)

rf_rmse = mean_squared_error(
    y_test,
    rf_predictions
) ** 0.5


# --------------------------------------------------
# STEP 10: XGBoost Model
# --------------------------------------------------

xgb_model = XGBRegressor(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="reg:squarederror",
    random_state=42
)

xgb_model.fit(X_train, y_train)

xgb_predictions = xgb_model.predict(X_test)

xgb_mae = mean_absolute_error(
    y_test,
    xgb_predictions
)

xgb_rmse = mean_squared_error(
    y_test,
    xgb_predictions
) ** 0.5


# --------------------------------------------------
# STEP 11: Display model comparison
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

print("\nXGBoost")
print(f"MAE  : {xgb_mae:.2f}")
print(f"RMSE : {xgb_rmse:.2f}")


# --------------------------------------------------
# STEP 12: Determine the best model
# --------------------------------------------------

models = {
    "Baseline": baseline_mae,
    "Random Forest": rf_mae,
    "XGBoost": xgb_mae
}

best_model = min(
    models,
    key=models.get
)

print("\n========================================")
print("BEST MODEL")
print("========================================")

print(f"Best model based on MAE: {best_model}")


# --------------------------------------------------
# STEP 13: XGBoost Feature Importance
# --------------------------------------------------

feature_importance = pd.DataFrame({
    "feature": features,
    "importance": xgb_model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    "importance",
    ascending=False
)

print("\n========================================")
print("XGBOOST FEATURE IMPORTANCE")
print("========================================")

for _, row in feature_importance.iterrows():
    print(
        f"{row['feature']:<25} "
        f"{row['importance']:.4f}"
    )


# --------------------------------------------------
# STEP 14: Training completed
# --------------------------------------------------

print("\nModel comparison completed successfully!")
# --------------------------------------------------
# STEP 15: Save the best Random Forest model
# --------------------------------------------------

os.makedirs("models", exist_ok=True)

model_path = "models/waste_model.pkl"

joblib.dump(rf_model, model_path)

print("\n========================================")
print("MODEL SAVED")
print("========================================")

print(f"Saved Random Forest model to: {model_path}")
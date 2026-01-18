import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import os

# Load processed data
X_train = pd.read_csv("X_train.csv")
X_test = pd.read_csv("X_test.csv")
y_train = pd.read_csv("y_train.csv").values.ravel()
y_test = pd.read_csv("y_test.csv").values.ravel()

# Create models directory
os.makedirs("models", exist_ok=True)

# -------------------------
# Linear Regression Model
# -------------------------
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

lr_mae = mean_absolute_error(y_test, lr_pred)
lr_r2 = r2_score(y_test, lr_pred)

print("🔹 Linear Regression Results")
print("MAE:", round(lr_mae, 2))
print("R2 Score:", round(lr_r2, 2))

# Save model
joblib.dump(lr_model, "models/linear_model.pkl")

# -------------------------
# Random Forest Model
# -------------------------
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_pred)
rf_r2 = r2_score(y_test, rf_pred)

print("\n🔹 Random Forest Results")
print("MAE:", round(rf_mae, 2))
print("R2 Score:", round(rf_r2, 2))

# Save model
joblib.dump(rf_model, "models/rf_model.pkl")

print("\n✅ Models trained and saved successfully!")

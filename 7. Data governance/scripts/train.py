# scripts/train.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import json
import os

# Load processed train and test data
train_df = pd.read_csv("data/processed/train.csv")
test_df = pd.read_csv("data/processed/test.csv")

# Separate features and target
X_train = train_df.drop(columns=["quality"])
y_train = train_df["quality"]
X_test = test_df.drop(columns=["quality"])
y_test = test_df["quality"]

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save metrics in DVC-readable JSON
os.makedirs("metrics", exist_ok=True)
metrics = {
    "mae": mae,
    "mse": mse,
    "r2_score": r2
}
with open("metrics/metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("Evaluation Metrics:")
print(json.dumps(metrics, indent=2))

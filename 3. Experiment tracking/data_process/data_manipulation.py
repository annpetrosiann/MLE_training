import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

# Load the Diabetes dataset
diabetes_data = load_diabetes()
X = pd.DataFrame(diabetes_data.data, columns=diabetes_data.feature_names)
y = pd.Series(diabetes_data.target, name="Progression")

# Create a data directory if it doesn't exist
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# Split the dataset into training and testing sets first
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale the features using only training data to fit the scaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convert scaled arrays back to dataframes
X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)

# Save the dataframes to CSV files
X_train_scaled.to_csv(os.path.join(data_dir, "X_train.csv"), index=False)
X_test_scaled.to_csv(os.path.join(data_dir, "X_test.csv"), index=False)
y_train.to_csv(os.path.join(data_dir, "y_train.csv"), index=False)
y_test.to_csv(os.path.join(data_dir, "y_test.csv"), index=False)

print("Files saved in 'data' folder:")
print("X_train is loaded into", os.path.join(data_dir, "X_train.csv"))
print("X_test is loaded into", os.path.join(data_dir, "X_test.csv"))
print("y_train is loaded into", os.path.join(data_dir, "y_train.csv"))
print("y_test is loaded into", os.path.join(data_dir, "y_test.csv"))
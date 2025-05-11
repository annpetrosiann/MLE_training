""""
This script loads the Iris dataset, splits and scales the features.
"""

import logging
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure the data directory exists
os.makedirs('./data', exist_ok=True)
logging.info(f"Data directory is created.")

# Load dataset
logging.info("Loading the Iris dataset.")
iris = load_iris()
X, y = iris.data, iris.target
logging.info("Dataset loaded successfully.")

# Split data into train and test
logging.info("Splitting data into train and test sets.")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
logging.info("Data splitting complete.")

# Scale the data
logging.info("Scaling the data.")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
logging.info("Data scaling complete.")

# Save to data directory
logging.info("Saving training and testing datasets into 'data' directory.")
train_df = pd.DataFrame(X_train_scaled, columns=iris.feature_names)
train_df['target'] = y_train
test_df = pd.DataFrame(X_test_scaled, columns=iris.feature_names)
test_df['target'] = y_test
train_df.to_csv('./data/train.csv', index=False)
test_df.to_csv('./data/test.csv', index=False)
logging.info("Datasets saved successfully.")

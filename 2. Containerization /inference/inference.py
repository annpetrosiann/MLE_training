"""
This script loads the latest trained model, data for inference and predicts results.
"""

import pandas as pd
from sklearn.metrics import accuracy_score
import joblib
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the pre-trained model
logging.info("Loading the trained model from 'saved_model' directory.")
model = joblib.load('./saved_model/model.joblib')
logging.info("Model loaded successfully.")

# Load the test data
logging.info("Loading test data from 'data' directory.")
test_df = pd.read_csv('./data/test.csv')
X_test = test_df.drop('target', axis=1)  # Extract features
y_test = test_df['target']  # Extract target variable
logging.info("Test data loaded successfully.")

# Perform predictions using the loaded model
logging.info("Making predictions...")
predictions = model.predict(X_test)

# Calculate the accuracy of the model on test data
test_accuracy = accuracy_score(y_test, predictions)
logging.info(f"Predictions are complete. Accuracy is {test_accuracy*100:.2f}%.")

print('Inference is finished. Check log for accuracy details.')
"""
This script prepares the data, runs the training, and saves the model.
"""

import logging
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Checking if the model directory exists...")
model_dir = os.path.join('saved_model')
os.makedirs(model_dir, exist_ok=True)
logging.info(f"Model directory at '{model_dir}' is ready.")

# Load data
logging.info("Loading training data from 'data' directory.")
train_df = pd.read_csv('./data/train.csv')
X_train = train_df.drop('target', axis=1)
y_train = train_df['target']
logging.info("Data loading complete.")

# Train model
logging.info("Starting model training...")
model = LogisticRegression(max_iter=50)
model.fit(X_train, y_train)
logging.info("Model training complete.")

# Save the model
model_path = os.path.join(model_dir, 'model.joblib')
joblib.dump(model, model_path)
logging.info(f"Model saved at {model_path}.")

# Optionally, print accuracy on training dataset
predictions = model.predict(X_train)
training_accuracy = accuracy_score(y_train, predictions)
logging.info(f"Training accuracy is {training_accuracy*100:.2f}%.")
print('Training is finished.')

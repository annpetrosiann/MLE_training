# scripts/preprocess_data.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import os

# Ensure output directory exists
os.makedirs("data/processed", exist_ok=True)

# Load and clean data
df = pd.read_csv("data/raw/winequality-red.csv", sep=";")
df = df.dropna().drop_duplicates()

# Split data
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Scale data
scaler = MinMaxScaler()
numeric_cols = train_df.select_dtypes(include='number').columns

train_df[numeric_cols] = scaler.fit_transform(train_df[numeric_cols])
test_df[numeric_cols] = scaler.transform(test_df[numeric_cols])

# Save splits
train_df.to_csv("data/processed/train.csv", index=False)
test_df.to_csv("data/processed/test.csv", index=False)

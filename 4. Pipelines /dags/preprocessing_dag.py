from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.compat.functools import cached_property
from airflow.models import Variable
from airflow.utils.file import mkdirs
from datetime import datetime, timedelta
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import OneHotEncoder
import os
import logging

default_args = {
    'owner': 'Anahit Petrosian',
    'start_date': datetime(2025, 4, 16),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'execution_timeout': timedelta(minutes=10),
    'depends_on_past': False,
}

dag = DAG(
    dag_id='data_preprocessing_pipeline',
    default_args=default_args,
    schedule=None,
    catchup=False,
    description='DAG for data preprocessing with download, merge, type correction, split, and OHE',
)

# Get absolute path
BASE_PATH = os.path.abspath('data_pipeline/') + '/'

### 1. Data Download
def download_data():
    try:
        mkdirs(BASE_PATH,mode=0o755)
        logging.info(f"Directory created at: {BASE_PATH}")
        logging.info(f"Directory exists: {os.path.exists(BASE_PATH)}")
        logging.info(f"Directory writable: {os.access(BASE_PATH, os.W_OK)}")

        df = pd.DataFrame({
            'user_id': [1, 2, 3, 4, 5],
            'age': ['25', '30', '35', '40', None],
            'city': ['NY', 'SF', 'LA', 'SF', 'NY']
        })
        file_path = os.path.join(BASE_PATH, 'data.csv')
        df.to_csv(file_path, index=False)
        logging.info(f"File created at: {file_path}")
    except Exception as e:
        logging.error(f"Failed to download data: {str(e)}")
        raise

### 2. Merge with Another Source
def merge_data():
    try:
        df = pd.read_csv(BASE_PATH + 'data.csv')
        # Simulate external source
        extra_info = pd.DataFrame({
             'user_id': [1, 2, 3, 4, 5],
             'group': ['A', 'B', 'A', 'B', 'A']
         })
        merged = pd.merge(df, extra_info, on='user_id')
        merged.to_csv(BASE_PATH + 'merged.csv', index=False)
        logging.info(f"Successfully merged data with {len(merged)} rows")
    except Exception as e:
        logging.error(f"Error in merging data: {e}")

### 3. Correct Data Types
def correct_types():
    df = pd.read_csv(BASE_PATH + 'merged.csv')
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df = df.dropna()  # Drop rows with missing age
    df.to_csv(BASE_PATH + 'cleaned.csv', index=False)
    logging.info("Data types corrected, missing values are handled")

### 4. Split: Train/Test + K-Fold
def split_data():
    df = pd.read_csv(BASE_PATH + 'cleaned.csv')
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    train.to_csv(BASE_PATH + 'train.csv', index=False)
    test.to_csv(BASE_PATH + 'test.csv', index=False)
    logging.info("Data is split into train and test sets.")

    # Save KFold indices for 3 splits
    kf = KFold(n_splits=3, shuffle=True, random_state=42)
    for fold, (train_idx, val_idx) in enumerate(kf.split(train)):
        fold_df = train.iloc[train_idx]
        fold_df.to_csv(BASE_PATH + f'cv_fold_{fold}.csv', index=False)
    logging.info(f"Saved K-Fold splits into {kf.get_n_splits()} folds.")

### 5. One-Hot Encoding
def one_hot_encode():
    df = pd.read_csv(BASE_PATH + 'train.csv')
    encoder = OneHotEncoder(sparse_output=False)
    encoded = encoder.fit_transform(df[['city', 'group']])
    columns = encoder.get_feature_names_out(['city', 'group'])
    
    logging.info(f"Encoded data shape: {encoded.shape}")
    logging.info(f"Columns: {columns}")

    df_encoded = pd.DataFrame(encoded, columns=columns)
    df_final = pd.concat([df.reset_index(drop=True), df_encoded], axis=1)
    df_final.to_csv(BASE_PATH + 'encoded_train.csv', index=False)
    logging.info("One-hot encoding applied to categorical features.")

# Define tasks
download_task = PythonOperator(
    task_id='download_data',
    python_callable=download_data,
    dag=dag
)

merge_task = PythonOperator(
    task_id='merge_data',
    python_callable=merge_data,
    dag=dag
)

type_task = PythonOperator(
    task_id='correct_data_types',
    python_callable=correct_types,
    dag=dag
)

split_task = PythonOperator(
    task_id='split_data',
    python_callable=split_data,
    dag=dag
)

ohe_task = PythonOperator(
    task_id='one_hot_encoding',
    python_callable=one_hot_encode,
    dag=dag
)

# Task dependencies
download_task >> merge_task >> type_task >> split_task >> ohe_task

# 🚀 Apache Airflow

This project defines a modular data preprocessing pipeline using [Apache Airflow](https://airflow.apache.org/). The pipeline includes tasks for downloading data, merging with additional sources, correcting data types, splitting into train/test sets with cross-validation, and applying one-hot encoding.

## 📁 Project Structure
```
├── dags                  
│   └── preprocessing_dag.py
├── Dockerfile         
├── docker-compose.yml                     
├── requirements.txt          
└── README.md
```

### DAG

The DAG is named `data_preprocessing_pipeline` and contains the following tasks:

1. **Download Data** - Creates a basic dataset.
2. **Merge Data** - Merges with a simulated external dataset.
3. **Correct Data Types** - Converts types and handles missing values.
4. **Split Data** - Splits into train/test and creates K-Fold splits.
5. **One-Hot Encode** - Applies one-hot encoding to categorical features.

### Output Files

- `data.csv` - Raw downloaded data
- `merged.csv` - After merging with external data
- `cleaned.csv` - Cleaned and type-corrected data
- `train.csv`, `test.csv` - Train/test split
- `cv_fold_0.csv`, `cv_fold_1.csv`, `cv_fold_2.csv` - K-Fold splits
- `encoded_train.csv` - One-hot encoded training data

All files are saved in the `data_pipeline/` directory.


## 🛠️ Usage

Make sure you have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed.

### 🐳 Start the Project with Docker Compose

```bash
  docker compose up --build
```
This will:
- Build the Airflow image
- Set up the webserver, scheduler, and other necessary services
- Launch Airflow at http://localhost:8088

## 📊 Airflow UI

After running the command, you’ll see a link to the Airflow UI. When you open it, you’ll be asked to enter a login and password. Use the credentials defined in your docker-compose.yml — in this case:

- Username: anahit
- Password: epam123

<img width="1506" alt="Screenshot 2025-04-18 at 10 41 42" src="https://github.com/user-attachments/assets/ac92d856-7035-431f-a2cc-e5509f32fcde" />

Once you're logged in, you’ll see the `data_preprocessing_pipeline`  listed on the homepage. You can trigger it from there to start the pipeline.

<img width="1507" alt="Screenshot 2025-04-18 at 10 41 59" src="https://github.com/user-attachments/assets/a18823a3-11eb-44c0-8bad-b997ee259c3d" />

The tasks will be queued and then executed in order. Once completed successfully, they will be marked as green (success).

<img width="1506" alt="Screenshot 2025-04-18 at 11 13 28" src="https://github.com/user-attachments/assets/71c0bdc5-035b-47cc-a892-5f3e4b328f30" />
<img width="1475" alt="Screenshot 2025-04-18 at 11 13 37" src="https://github.com/user-attachments/assets/fbe6976d-8806-499e-b22a-7f913a3dbe52" />

You can explore more by clicking on the DAG

<img width="1497" alt="Screenshot 2025-04-18 at 11 13 54" src="https://github.com/user-attachments/assets/73046054-70f5-4a70-a5cf-f2feffe719ff" />
<img width="874" alt="Screenshot 2025-04-18 at 11 14 29" src="https://github.com/user-attachments/assets/fbb61d7e-f690-4835-84af-b7f9057b252f" />


You'll find views like:
- Graph View 🗺️ — to visualize the pipeline structure
- Tree View 🌳 — to track task status over time
- Logs 📜 — to see detailed output from each task

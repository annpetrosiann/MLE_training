# 🏥 Diabetes Progression Prediction

*A machine learning pipeline to predict diabetes progression using various regression models, with MLflow for experiment tracking and Docker for containerization.*

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![MLflow](https://img.shields.io/badge/MLflow-2.20.1-orange.svg)
![Docker Compose](https://img.shields.io/badge/docker_compose-supported-brightgreen.svg)

This project uses the `Diabetes dataset` from scikit-learn, which includes physiological measurements from 442 patients. The features are 10 `baseline variables`(age, sex, BMI, average blood pressure (BP), and six blood serum measurements (s1-s6))
and `target` (quantitative measure of disease progression one year after baseline).

## 📌 Project Overview

This project implements a complete ML pipeline that:
1. Processes the Diabetes dataset from sklearn
2. Generates exploratory visualizations
3. Trains and compares 4 regression models:
   - Linear Regression
   - Lasso Regression
   - Decision Tree Regression
   - Random Forest Regression
4. Tracks all experiments using MLflow
5. Can be run either locally or via Docker containers

## 📂 Project Structure

```bash

3. Experiment tracking
├── data/                   # Available only after running data_manipulation.py
│   ├── X_test.csv          
│   ├── X_train.csv         
│   ├── y_test.csv          
│   └── y_train.csv         
│
├── data_process/             
│   ├── data_manipulation.py  # Data preprocessing
│   └── data_visualization.py # EDA visualizations
│
├── plots/                    # Available only after running data_visualization.py
│   ├── histograms.png       
│   ├── box_plot.png          
│   ├── scatter_plots.png     
│   └── correlation_heatmap.png
│
├── mlruns/                 # MLflow experiment tracking
│   ├── 0/                   
│   └── <run_ids>/           
│       ├── artifacts/        
│       └── metrics/           
│
├── models/                 
│   ├── linear_regression.py
│   ├── random_forest_regression.py
│   ├── decision_tree_regression.py
│   └── lasso_regression.py
│
├── docker/                 # Containerization
│   ├── MLflow/Dockerfile     # MLflow tracking server
│   └── train/Dockerfile      # Training environment
│
├── docker-compose.yml      # Orchestrates MLflow + training
├── requirements.txt        # Python dependencies
└── README.md
```


## 🖥️ Local Setup

1. **Create a virtual environment**:
  ```bash
   python3 -m venv {virtual_environment_name}
  ```
2. **Activate the virtual environment**:
    - On Windows:
      ```bash
      python3 -m venv {virtual_environment_name}
      ```
    - On macOS or Linux:
      ```bash
      source {virtual_environment_name}/bin/activate
      ```
3. **Install Dependencies**
     ```bash
     pip install --upgrade pip
     pip install -r requirements.txt
     ```

4. **Run Data Pipeline**
   ```bash
   python3 data_process/data_manipulation.py
   python3 data_process/data_visualization.py
   ```

5. **Train models**
   ```bash
   # Run individual models:
   python3 models/linear_regression.py
   python3 models/lasso_regression.py
   python3 models/decision_tree_regression.py
   python3 models/random_forest_regression.py

   # Or run all sequentially:
   for model in linear lasso decision_tree random_forest; 
   do
    python3 models/${model}_regression.py
   done
   ``` 
6. **Launch MLflow UI**
   ```bash
   # Start MLflow UI (default port: 5000)
   mlflow ui --port 5005
   # Access at: http://localhost:5005
   ```
   
## 🐳 Docker Setup
To run the application using Docker, make sure you have Docker and docker-compose installed on your system.

Building and Running Containers
Execute the following command to build and start the containers as specified in the docker-compose.yml file:

```bash
  docker-compose -f docker-compose.yml up --build
```

This command builds the Docker images and starts the services defined in the docker-compose.yml file, including the MLflow tracking server and the training application.

The MLflow UI will be accessible on `localhost:5005` after the services are up and running.
```bash

# Stop all services (preserves data)
docker-compose stop

# Stop and remove containers/networks
docker-compose down

# Remove all persistent data (mlruns)
docker-compose down -v

# View logs for specific service
docker-compose logs -f mlflow-ui
```
## 📊 MLFlow UI

In the MLflow UI, you will see two sections:
1. Experiments
2. Models

<img width="1509" alt="Screenshot 2025-04-09 at 18 00 42" src="https://github.com/user-attachments/assets/c29121e6-9a49-427f-b7ad-8dd2094acd47" />

In the Experiments section, you can see some visualizations and compare models. The best-performing model so far is the lasso regression, which is why we've registered it as the best one. You can find this model in the Models section (see below).


<img width="1501" alt="Screenshot 2025-04-09 at 18 00 57" src="https://github.com/user-attachments/assets/acbf95fa-ac43-4e11-b50f-fff1b4c9bd2b" />

For data visualization, click on "Data Plots" and go to "Artifacts" where you will see some plots.

<img width="487" alt="Screenshot 2025-04-09 at 18 02 30" src="https://github.com/user-attachments/assets/8d37d177-7fcb-4dab-abb8-51b184544637" />

In the Models section, you can select any model and navigate to "Artifacts" to find sample data and model artifacts. Additionally, in the "Overview" tab, you can view its parameters, and on the "Metrics" page, you can review its metrics.


<img width="1504" alt="Screenshot 2025-04-09 at 18 02 19" src="https://github.com/user-attachments/assets/bd889295-c1a2-40ba-8862-c884cbd6b611" />

All models are reproducible, meaning that if you do not manually change the model's parameters, they will consistently produce the same metrics.







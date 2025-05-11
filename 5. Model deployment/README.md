# Model Deployment

This project demonstrates a complete machine learning pipeline using the **Iris dataset**, packaged and deployed in two modes:

- 🌐 **Online prediction** via REST API using Flask
- 📦 **Batch prediction** via scheduled cron jobs

Includes Docker support, modern Python packaging (`pyproject.toml`), and testing with `pytest`.

---

## 📁 Project Structure
```
├── artifacts/
│   ├── model.pkl     
│   ├── scaler.pkl         
│   └── offline_predictions.csv
│
├── iris_deploy/          
│   ├── __init__.py     
│   ├── batch_runner.py  
│   ├── rest_server.py
│   └── training.py   
│         
├── test/               
│   ├── test_inference.py                      
│   └── test_rest_api.py    
│
├── Dockerfile
├── mycron.txt             
├── cron_logs/      
├── pyproject.toml    
├── .gitignore
├── requirements.txt       
└── README.md
```

---
### Details

- **Dataset**: `sklearn.datasets.load_iris()`
- **Model**: `RandomForestClassifier`
- **Preprocessing**: `StandardScaler`
- **Saved artifacts**: `artifacts/model.pkl`, `artifacts/scaler.pkl`,`artifacts/offline_predictions.csv`

## Install dependencies
```bash
pip install -r  requirements.txt
```

## 🔧 Train the model
```bash
python3 iris_deploy/training.py
```
This will load the `Iris dataset`, scale features using `StandardScaler`, train a `RandomForestClassifier` and save the model and scaler to the  `artifacts/` directory.


## 🌐 REST API (Online Prediction)
Start the Flask server:

```bash
python3 iris_deploy/rest_server.py
```
You can access it with provided UI.

**📬 Example cURL Request**
```bash
  curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"feature1": 5.1, "feature2": 3.5, "feature3": 1.4, "feature4": 0.2}'
  ```
Or use the built-in web UI to input features and get predictions. Results will be shown as class labels (see below).


![Untitled design](https://github.com/user-attachments/assets/b2e8f035-92c1-45c7-b421-36f47bf83d93)

## 📦 Batch Prediction
Run the full batch pipeline:

```bash
python3 iris_deploy/batch_runner.py
```
This will load the dataset, predict using saved model, save results to `artifacts/offline_predictions.csv` and automatically build the Docker image `(iris-rest-api)` using our `Dockerfile`.  After that you can run the container:
```bash
docker run -p 8080:8080 iris-rest-api
```
You’ll see the same UI for live predictions from the `rest_server.py`.

## Testing
Run tests using `pytest`:

``` bash
pytest test/test_rest_api.py
```
Tests include valid predictions, missing/invalid input, response time check (<1s), HTML form presence.

``` bash
pytest test/test_inference.py.py
```
This test checks prediction logic and expected outputs against known data samples.

## ⏰ Cron for Automated Batch Jobs

To automate daily batch runs, we use cron. An example cron job runs every day at 1:10 AM. You can see it in   `mycron.txt`.
Add it via:
 ``` bash
 crontab mycron.txt
```
Logs will be saved to `cron_logs/batch.log.` You can see one example in this repo.

## ⚙️ Python package
This project uses modern packaging via `pyproject.toml` (PEP 621).  Once installed locally:
```bash
pip install --editable . --config-settings editable_mode=compat
  ```
Then you can use the CLI commands listed below.
```bash
train-iris        # Train and save model + scaler
predict-batch     # Batch prediction + Docker build
run-server        # Start Flask REST API server
```
These commands are defined in `pyproject.toml` under `[project.scripts]`. 


📦 In summary: all source code is packaged under `iris_deploy`; online and batch modes reuse the same `artifacts`; the REST API is served via Flask and Docker; batch jobs are scheduled via cron; and the project is tested using `pytest`.

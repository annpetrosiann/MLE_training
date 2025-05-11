import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    explained_variance_score,
    mean_squared_log_error,
)
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
import os

# Set environment variable to silence specific warnings
os.environ["GIT_PYTHON_REFRESH"] = "quiet"


def log_dataset_info(X, y, prefix=""):
    """Log dataset information as parameters and tags."""
    mlflow.log_params(
        {f"{prefix}num_samples": len(X), f"{prefix}num_features": X.shape[1]}
    )

    mlflow.set_tags(
        {
            f"{prefix}features": str(list(X.columns)),
            f"{prefix}target": y.name if hasattr(y, "name") else "unnamed",
        }
    )


def train_and_evaluate_model(X_train, y_train, X_test, y_test):
    """Train the model and evaluate its performance."""
    # Model training
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=7,
        min_samples_split=2,
        min_samples_leaf=1,
        max_features="sqrt",
    )
    model.fit(X_train, y_train)

    # Evaluation
    predictions = model.predict(X_test)
    return model, predictions


def log_metrics_and_model(model, predictions, X_train, y_train, X_test, y_test):
    """Log metrics and save the model with MLflow."""
    metrics = {
        "mse": mean_squared_error(y_test, predictions),
        "mae": mean_absolute_error(y_test, predictions),
        "explained_variance": explained_variance_score(y_test, predictions),
        "msle": mean_squared_log_error(y_test, predictions),
    }
    mlflow.log_params(
        {
            "model_type": "Random Forest Regression",
            "n_estimators": model.n_estimators,
            "max_depth": model.max_depth,
            "min_samples_split": model.min_samples_split,
            "min_samples_leaf": model.min_samples_leaf,
            "max_features": model.max_features,
        }
    )
    mlflow.log_metrics(metrics)

    signature = infer_signature(X_train, predictions)
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        signature=signature,
        input_example=X_train.iloc[:5],
    )


def run_experiment():
    """Set up and run the MLflow experiment."""
    # Load data
    X_train = pd.read_csv("./data/X_train.csv")
    y_train = pd.read_csv(
        "./data/y_train.csv"
    ).values.ravel()  # Adjust y_train to be a 1D array
    X_test = pd.read_csv("./data/X_test.csv")
    y_test = pd.read_csv(
        "./data/y_test.csv"
    ).values.ravel()  # Adjust y_test to be a 1D array

    # Start MLflow run
    mlflow.set_experiment("Models")
    with mlflow.start_run(run_name="Random Forest Regression"):
        # Log dataset information
        log_dataset_info(X_train, y_train, "train_")
        log_dataset_info(X_test, y_test, "test_")
        mlflow.log_text(X_train.head().to_csv(index=False), "data/train_sample.csv")
        mlflow.log_text(X_test.head().to_csv(index=False), "data/test_sample.csv")

        model, predictions = train_and_evaluate_model(X_train, y_train, X_test, y_test)
        log_metrics_and_model(model, predictions, X_train, y_train, X_test, y_test)


if __name__ == "__main__":
    run_experiment()
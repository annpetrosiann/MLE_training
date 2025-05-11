import pandas as pd
import os
import subprocess
import pickle
from sklearn.datasets import load_iris

def main():

    # Get absolute path to the artifacts folder
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ARTIFACTS_PATH = os.path.join(BASE_DIR, "..", "artifacts")

    # Load model and scaler
    with open(os.path.join(ARTIFACTS_PATH, "model.pkl"), "rb") as f:
        model = pickle.load(f)

    with open(os.path.join(ARTIFACTS_PATH, "scaler.pkl"), "rb") as f:
        scaler = pickle.load(f)

    # Class label mapping
    class_labels = {
        0: "Iris-setosa",
        1: "Iris-versicolor",
        2: "Iris-virginica"
    }

    # Load built-in iris dataset
    iris = load_iris()
    X = iris["data"]
    y_true = iris["target"]
    feature_names = iris["feature_names"]

    # Scale features
    X_scaled = scaler.transform(X)

    # Predict
    y_pred = model.predict(X_scaled)
    y_labels = [class_labels[i] for i in y_pred]

    # Create dataframe
    df = pd.DataFrame(X, columns=feature_names)
    df["true_label"] = [class_labels[i] for i in y_true]
    df["predicted_label"] = y_labels
    df["predicted_class"] = y_pred

    # Save to CSV
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ARTIFACT_DIR = os.path.join(BASE_DIR, "artifacts")
    os.makedirs(ARTIFACT_DIR, exist_ok=True)
    df.to_csv(os.path.join(ARTIFACT_DIR, "offline_predictions.csv"), index=False)
    print("✅ Batch prediction complete.")

    # Build Docker image
    print("🚢 Building Docker image for REST API...")
    try:
        subprocess.run(["docker", "build", "-t", "iris-rest-api", "."], check=True)
        print("✅ Docker image 'iris-rest-api' built successfully.")
    except subprocess.CalledProcessError as e:
        print("❌ Docker build failed.")
        print(e)

if __name__ == "__main__":
    main()
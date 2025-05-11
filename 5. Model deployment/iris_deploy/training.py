from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle
import os


def main():
    # Load data
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Fit scaler and model
    scaler = StandardScaler().fit(X_train)
    X_train_scaled = scaler.transform(X_train)

    model = RandomForestClassifier().fit(X_train_scaled, y_train)

    # Save artifacts
    os.makedirs("../artifacts", exist_ok=True)

    with open("../artifacts/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

    with open("../artifacts/model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("✅ Training complete. Artifacts saved.")

if __name__ == "__main__":
    main()
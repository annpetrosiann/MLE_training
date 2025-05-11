import pickle
import numpy as np
import os
import pytest

@pytest.fixture(scope="module")
def load_artifacts():
    model_path = "artifacts/model.pkl"
    scaler_path = "artifacts/scaler.pkl"

    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        pytest.fail("Artifacts not found. Run training.py first.")

    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(scaler_path, "rb") as f:
        scaler = pickle.load(f)

    return model, scaler

def test_model_prediction(load_artifacts):
    model, scaler = load_artifacts
    sample = np.array([[5.1, 3.5, 1.4, 0.2]])  # Iris-setosa like

    scaled = scaler.transform(sample)
    prediction = model.predict(scaled)

    assert isinstance(prediction, np.ndarray)
    assert prediction.shape == (1,)
    assert prediction[0] in [0, 1, 2]  # valid iris classes

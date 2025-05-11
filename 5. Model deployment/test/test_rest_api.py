import requests
import pytest
import time

BASE_URL = "http://localhost:8080"

# ✅ 1. Normal prediction + response time
@pytest.mark.parametrize("features, expected_keys", [
    (
        {"feature1": 5.1, "feature2": 3.5, "feature3": 1.4, "feature4": 0.2},
        ["prediction"]
    ),
])
def test_predict_endpoint(features, expected_keys):
    start = time.time()
    response = requests.post(f"{BASE_URL}/predict", json=features)
    elapsed = time.time() - start

    assert response.status_code == 200
    data = response.json()
    for key in expected_keys:
        assert key in data
    assert isinstance(data["prediction"], (list, int))
    assert elapsed < 1.0, f"Too slow: {elapsed:.3f}s"
    print(f"✅ Passed in {elapsed:.4f}s")

# ✅ 2. Missing field
def test_missing_field():
    payload = {"feature1": 5.1, "feature2": 3.5}  # missing feature3 & 4
    response = requests.post(f"{BASE_URL}/predict", json=payload)
    assert response.status_code == 400
    assert "error" in response.json()
    print("✅ Handled missing field properly")

# ✅ 3. Invalid data types
def test_invalid_data_type():
    payload = {"feature1": "abc", "feature2": 3.5, "feature3": 1.4, "feature4": 0.2}
    response = requests.post(f"{BASE_URL}/predict", json=payload)
    assert response.status_code == 400
    assert "error" in response.json()
    print("✅ Handled invalid data type")

# ✅ 4. Home page test (GET /)
def test_home_page():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "<form" in response.text  # basic check to see if form exists
    print("✅ Home page loaded")

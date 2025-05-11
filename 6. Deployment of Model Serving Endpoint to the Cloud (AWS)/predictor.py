from flask import Flask, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model and scaler once at start
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

class_labels = {
    0: "🐍 Iris-setosa",
    1: "🌸 Iris-versicolor",
    2: "🌿 Iris-virginica"
}

@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200

@app.route("/invocations", methods=["POST"])
def predict():
    try:
        input_data = request.get_json()
        features = np.array(input_data["features"]).reshape(1, -1)
        scaled = scaler.transform(features)
        pred = model.predict(scaled)[0]
        label = class_labels.get(pred, f"Unknown ({pred})")
        return jsonify({"prediction": int(pred), "label": label})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

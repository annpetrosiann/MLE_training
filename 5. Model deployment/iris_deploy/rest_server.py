from flask import Flask, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model and scaler once when server starts
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIR = os.path.join(BASE_DIR, "artifacts")

with open(os.path.join(ARTIFACT_DIR, "model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(ARTIFACT_DIR, "scaler.pkl"), "rb") as f:
    scaler = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    class_labels = {
        0: "🐍 Iris-setosa",
        1: "🌸 Iris-versicolor",
        2: "🌿 Iris-virginica"
    }

    if request.method == "POST":
        try:
            f1 = float(request.form["feature1"])
            f2 = float(request.form["feature2"])
            f3 = float(request.form["feature3"])
            f4 = float(request.form["feature4"])
            input_array = np.array([[f1, f2, f3, f4]])
            scaled_input = scaler.transform(input_array)
            prediction = model.predict(scaled_input)[0]
            label = class_labels.get(prediction, f"Unknown ({prediction})")
            message = f"<div class='result'>🌟 Predicted Class: <strong>{label}</strong></div>"
        except Exception as e:
            message = f"<div class='error'>⚠️ Error: {str(e)}</div>"

    return f"""
    <html>
    <head>
        <title>Iris Prediction</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 50px;
                background-color: #f0f0f0;
            }}
            .container {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                width: 400px;
                margin: auto;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            input[type='text'] {{
                width: 90%;
                padding: 8px;
                margin: 8px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }}
            input[type='submit'] {{
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }}
            .result {{
                margin-top: 20px;
                padding: 10px;
                background-color: #e6ffe6;
                border: 1px solid #4CAF50;
                border-radius: 4px;
                font-size: 18px;
            }}
            .error {{
                margin-top: 20px;
                padding: 10px;
                background-color: #ffe6e6;
                border: 1px solid #e60000;
                border-radius: 4px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>🌱 Iris Flower Classifier</h2>
            <p>Enter flower measurements to predict the species 🌸</p>
            <form method="POST">
                Sepal Length: <br><input type="text" name="feature1" required><br>
                Sepal Width: <br><input type="text" name="feature2" required><br>
                Petal Length: <br><input type="text" name="feature3" required><br>
                Petal Width: <br><input type="text" name="feature4" required><br>
                <br>
                <input type="submit" value="🌼 Predict">
            </form>
            {message}
        </div>
    </body>
    </html>
    """

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_json = request.json
        input_features = [input_json[f"feature{i+1}"] for i in range(4)]
        input_array = np.array([input_features])
        scaled_input = scaler.transform(input_array)
        prediction = model.predict(scaled_input)
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

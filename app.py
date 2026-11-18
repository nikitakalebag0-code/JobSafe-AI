
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load trained Machine Learning model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return jsonify({
        "project": "JobSafe AI",
        "status": "Running Successfully"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}

    description = data.get("description", "").strip()

    if not description:
        return jsonify({
            "error": "Please enter job description"
        }), 400

    prediction = int(model.predict([description])[0])

    if prediction == 1:
        risk = "High"
        result = "Suspicious Job"
    else:
        risk = "Low"
        result = "Likely Genuine Job"

    return jsonify({
        "prediction": result,
        "risk_level": risk,
        "disclaimer": "AI prediction is not a guarantee. Verify the employer independently."
    })

if __name__ == "__main__":
    app.run()
    


from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to JobSafe AI Backend",
        "status": "Running"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    description = data.get("description", "").lower()

    if not description:
        return jsonify({
            "error": "Job description is required"
        }), 400

    red_flags = [
        "registration fee",
        "training fee",
        "pay money",
        "bank details",
        "otp",
        "urgent hiring",
        "guaranteed salary"
    ]

    found = [word for word in red_flags if word in description]

    if len(found) >= 2:
        risk = "High"
    elif len(found) == 1:
        risk = "Medium"
    else:
        risk = "Low"

    return jsonify({
        "risk_level": risk,
        "red_flags": found,
        "message": "Initial safety screening only. Not a guarantee of job authenticity."
    })

if __name__ == "__main__":
    app.run(debug=True)
           

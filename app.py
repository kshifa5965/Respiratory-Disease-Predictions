from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and encoders
model = joblib.load("model/respiratory_model.pkl")
gender_encoder = joblib.load("model/gender_encoder.pkl")
disease_encoder = joblib.load("model/disease_encoder.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    age = int(request.form["age"])
    gender = request.form["gender"]
    fever = int(request.form["fever"])
    cough = int(request.form["cough"])
    shortness = int(request.form["shortness"])
    chest_pain = int(request.form["chest_pain"])
    fatigue = int(request.form["fatigue"])
    wheezing = int(request.form["wheezing"])
    smoking = int(request.form["smoking"])
    spo2 = int(request.form["spo2"])

    # Encode gender
    gender = gender_encoder.transform([gender])[0]

    # Prepare input
    data = np.array([[age, gender, fever, cough,
                      shortness, chest_pain,
                      fatigue, wheezing,
                      smoking, spo2]])

    prediction = model.predict(data)
    disease = disease_encoder.inverse_transform(prediction)[0]

    return render_template("result.html", disease=disease)


if __name__ == "__main__":
    app.run(debug=True)
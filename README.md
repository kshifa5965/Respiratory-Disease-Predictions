# AI-Based Respiratory Disease Prediction System Using Machine Learning

## Project Overview

The AI-Based Respiratory Disease Prediction System is a web application that predicts possible respiratory diseases based on user symptoms. The system uses a Machine Learning model trained on a respiratory disease dataset and provides disease predictions through a user-friendly web interface.

This project is developed using Python, Flask, Scikit-learn, HTML, CSS, and JavaScript.

---

## Features

- Predicts respiratory diseases using Machine Learning
- User-friendly web interface
- Fast and accurate prediction
- Flask backend integration
- Responsive design
- Simple symptom input form
- Displays predicted disease instantly

---

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## Project Structure

```
Respiratory-Disease-Prediction/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── respiratory_dataset.csv
│
├── model/
│   ├── respiratory_model.pkl
│   ├── gender_encoder.pkl
│   └── disease_encoder.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── uploads/
```

---

## Dataset

The project uses a respiratory disease dataset containing patient information such as:

- Age
- Gender
- Fever
- Cough
- Shortness of Breath
- Chest Pain
- Fatigue
- Wheezing
- Smoking History
- SpO₂ Level

Target diseases include:

- Asthma
- Pneumonia
- Bronchitis
- COPD
- Tuberculosis
- Common Cold
- Healthy

---

## Machine Learning Algorithm

The project uses the **Decision Tree Classifier** from Scikit-learn.

### Steps

1. Load the dataset
2. Encode categorical values
3. Split features and target
4. Train the Decision Tree model
5. Save the trained model using Joblib
6. Load the model in Flask for prediction

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Respiratory-Disease-Prediction.git
```

### Open Project Folder

```bash
cd Respiratory-Disease-Prediction
```

### Install Required Libraries

```bash
pip install flask pandas numpy scikit-learn joblib
```

---

## Train the Machine Learning Model

```bash
python train_model.py
```

After training, the following files are generated:

```
model/
├── respiratory_model.pkl
├── gender_encoder.pkl
└── disease_encoder.pkl
```

---

## Run the Flask Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## How to Use

1. Open the application.
2. Enter patient details.
3. Select symptoms.
4. Click **Predict Disease**.
5. View the predicted respiratory disease.

---

## Project Workflow

```
Patient Details
        │
        ▼
HTML Form
        │
        ▼
Flask Backend
        │
        ▼
Machine Learning Model
        │
        ▼
Disease Prediction
        │
        ▼
Prediction Result
```

---

## Screenshots

### Home Page

(Add screenshot here)

### Prediction Result

(Add screenshot here)

---

## Future Enhancements

- Increase dataset size for better accuracy
- Add disease probability score
- Doctor recommendation system
- Patient history management
- Cloud deployment
- Mobile-friendly interface
- User authentication

---

## Requirements

- Python 3.10+
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

<img width="1504" height="1002" alt="Screenshot 2026-06-25 011607" src="https://github.com/user-attachments/assets/11cfb062-6b5e-4efe-ac8d-b68e3cc421d7" />

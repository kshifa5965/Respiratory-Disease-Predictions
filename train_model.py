import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load Dataset
data = pd.read_csv("dataset/respiratory_dataset.csv")

# Convert Gender to Numbers
gender_encoder = LabelEncoder()
data["Gender"] = gender_encoder.fit_transform(data["Gender"])

# Convert Disease to Numbers
disease_encoder = LabelEncoder()
data["Disease"] = disease_encoder.fit_transform(data["Disease"])

# Features (Input)
X = data.drop("Disease", axis=1)

# Target (Output)
y = data["Disease"]

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Save Model
joblib.dump(model, "model/respiratory_model.pkl")
joblib.dump(gender_encoder, "model/gender_encoder.pkl")
joblib.dump(disease_encoder, "model/disease_encoder.pkl")

print("Model trained successfully!")
print("Files saved in model folder.")
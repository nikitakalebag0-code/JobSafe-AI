
import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Load dataset
data = pd.read_csv("dataset.csv")

# Prepare training data
X = data["description"].astype(str)
y = data["label"]

# Create ML model
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Train model
model.fit(X, y)

# Save trained model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("JobSafe AI Model Trained Successfully!")

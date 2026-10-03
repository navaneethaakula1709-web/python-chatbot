import json
import os
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib


# ==========================================================
# PATH SETUP
# ==========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "python_questions.json"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "python_chatbot_model.pkl"
)


# ==========================================================
# LOAD DATASET
# ==========================================================

with open(DATA_PATH, "r", encoding="utf-8") as file:
    data = json.load(file)


questions = []
categories = []


for item in data:
    questions.append(item["question"])
    categories.append(item["category"])


# ==========================================================
# CREATE MACHINE LEARNING PIPELINE
# ==========================================================

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2)
        )
    ),

    (
        "classifier",
        LogisticRegression(
            max_iter=1000
        )
    )
])


# ==========================================================
# TRAIN MODEL
# ==========================================================

print("==============================================")
print("       PYTHON CHATBOT ML TRAINING")
print("==============================================")

print("Loading dataset...")
print("Total questions:", len(questions))

print()
print("Training Machine Learning model...")

model.fit(questions, categories)

print("Training completed successfully!")


# ==========================================================
# SAVE MODEL
# ==========================================================

os.makedirs(MODEL_DIR, exist_ok=True)

joblib.dump(model, MODEL_PATH)


print()
print("Model saved successfully!")
print("Model location:")
print(MODEL_PATH)

print("==============================================")
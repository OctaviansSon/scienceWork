import pickle
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

with open(MODEL_PATH, "rb") as f:
    vectorizer, model = pickle.load(f)

def ml_detect(query: str):
    X = vectorizer.transform([query])
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0].max()

    return {
        "decision": "VULNERABLE" if pred == 1 else "SAFE",
        "confidence": float(prob)
    }

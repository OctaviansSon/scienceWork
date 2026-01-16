import pickle
from llm.llm_check import llm_analyze
from ml.model import ml_detect
from llm.llm_check import llm_detect
with open("ml/model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

def hybrid_detect(query: str) -> dict:
    X = vectorizer.transform([query])
    ml_prob = model.predict_proba(X)[0][1]

    if ml_prob >= 0.7:
        return {
            "decision": "VULNERABLE",
            "source": "ML",
            "confidence": round(ml_prob, 3)
        }

    llm_result = llm_analyze(query)

    return {
        "decision": llm_result,
        "source": "LLM",
        "confidence": round(ml_prob, 3)
    }

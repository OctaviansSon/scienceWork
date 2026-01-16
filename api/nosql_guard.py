from pymongo import MongoClient
from ml.hybrid import hybrid_detect
from datetime import datetime

# mongo ports + connection
client = MongoClient("mongodb://localhost:27017/")
db = client["test_security"]
collection = db["users"]

# query guard
def execute_safe_nosql(query: str):
    analysis = hybrid_detect(query)

    log = {
        "query": query,
        "decision": analysis["decision"],
        "source": analysis["source"],
        "confidence": analysis["confidence"],
        "timestamp": datetime.now().isoformat()
    }

    # 1 Block vulnerables
    if analysis["decision"] == "VULNERABLE":
        return {
            "status": "BLOCKED",
            "log": log
        }

    # 2. Only controlled evals
    try:
        # eval for lab tests
        result = eval(query)
        return {
            "status": "EXECUTED",
            "result": list(result),
            "log": log
        }
    except Exception as e:
        return {
            "status": "ERROR",
            "error": str(e),
            "log": log
        }

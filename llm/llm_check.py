import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def llm_analyze(query: str) -> str:
    prompt = f"""
You are a cybersecurity expert.
Analyze the following SQL or NoSQL query and determine
whether it contains a security vulnerability.

Respond with ONLY one word:
SAFE or VULNERABLE.

Query:
{query}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    return response.json()["response"].strip()

def llm_detect(query: str) -> dict:
    decision = llm_analyze(query)
    return {
        "decision": decision,
        "confidence": 0.5  # llm cant give prob
    }
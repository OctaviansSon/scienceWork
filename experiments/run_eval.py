import pandas as pd
from ml.hybrid import hybrid_detect
from ml.model import ml_detect
from llm.llm_check import llm_detect

df = pd.read_csv("data/eval_queries.csv")

results = []

for _, row in df.iterrows():
    query = row["query"]
    true_label = row["label"]

    ml_pred = ml_detect(query)["decision"]
    llm_pred = llm_detect(query)["decision"]
    hybrid_pred = hybrid_detect(query)["decision"]

    results.append({
        "query": query,
        "true": true_label,
        "ml": ml_pred,
        "llm": llm_pred,
        "hybrid": hybrid_pred
    })

pd.DataFrame(results).to_csv("data/results.csv", index=False)
print("Evaluation finished. Results saved.")

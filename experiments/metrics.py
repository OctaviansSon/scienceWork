import pandas as pd
from sklearn.metrics import classification_report

df = pd.read_csv("data/results.csv")

for model in ["ml", "llm", "hybrid"]:
    print(f"\n=== {model.upper()} ===")
    print(classification_report(df["true"], df[model]))

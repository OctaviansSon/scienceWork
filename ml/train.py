import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv("data/queries.csv")

X = df["query"]
y = df["label"]

vectorizer = TfidfVectorizer(ngram_range=(1,3))
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

with open("ml/model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("ML model trained and saved")

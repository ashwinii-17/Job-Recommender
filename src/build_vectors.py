# src/build_vectors.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

# Paths
CLEANED_DATA_PATH = os.path.join("models", "cleaned_jobs.csv")
VECTORS_PATH = os.path.join("models", "job_vectors.pkl")
VECTORIZER_PATH = os.path.join("models", "tfidf_vectorizer.pkl")

def build_vectors():
    # Load cleaned dataset
    df = pd.read_csv(CLEANED_DATA_PATH)

    # Join skills into one string per job
    df["skills_text"] = df["job_skill_set"].apply(lambda x: " ".join(eval(x)))

    # TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(df["skills_text"])

    # Save vectors and vectorizer
    with open(VECTORS_PATH, "wb") as f:
        pickle.dump(vectors, f)
    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer, f)

    print(f"✅ Vectors saved to {VECTORS_PATH}")
    print(f"✅ Vectorizer saved to {VECTORIZER_PATH}")

if __name__ == "__main__":
    build_vectors()

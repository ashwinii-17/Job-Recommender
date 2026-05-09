# src/preprocess.py

import pandas as pd
import ast
import os

# Paths
DATA_PATH = os.path.join("data", "all_job_post.csv")
OUTPUT_PATH = os.path.join("models", "cleaned_jobs.csv")

def clean_dataset():
    # Load dataset
    df = pd.read_csv(DATA_PATH)

    # Convert job_skill_set from string to list
    def parse_skills(skill_str):
        try:
            return ast.literal_eval(skill_str)
        except Exception:
            return []

    df["job_skill_set"] = df["job_skill_set"].apply(parse_skills)

    # Remove rows without skills
    df = df[df["job_skill_set"].map(len) > 0]

    # Save cleaned dataset
    os.makedirs("models", exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    
    print(f"✅ Cleaned dataset saved to {OUTPUT_PATH}")
    print("🔹 Example row:")
    print(df.head(3))

if __name__ == "__main__":
    clean_dataset()

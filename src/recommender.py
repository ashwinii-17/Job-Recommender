# recommender.py
import pandas as pd

# Load cleaned jobs dataset
df = pd.read_csv("models/cleaned_jobs.csv") # job_skill_set column should be a list

def recommend_jobs(user_skills, top_n=5):
    """
    user_skills: list of strings, e.g., ['python', 'sql']
    top_n: number of jobs to return
    """
    user_skills = [skill.strip().lower() for skill in user_skills]  # clean input
    
    scores = []
    
    for idx, row in df.iterrows():
        job_skills = [skill.lower() for skill in eval(row['job_skill_set'])]  # convert string to list
        match_count = sum(1 for skill in user_skills if skill in job_skills)
        if match_count > 0:
            score = match_count / len(user_skills)  # proportion of matched skills
            scores.append((idx, score))
    
    # Sort by score descending
    scores.sort(key=lambda x: x[1], reverse=True)
    
    # Take top N
    top_indices = [idx for idx, score in scores[:top_n]]
    
    recommended_jobs = df.iloc[top_indices].copy()
    recommended_jobs['match_score'] = [score for idx, score in scores[:top_n]]
    recommended_jobs['match_score'] = recommended_jobs['match_score'] * 100  # convert to %
    
    return recommended_jobs

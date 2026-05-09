import streamlit as st
import pandas as pd
import pickle
from recommender import recommend_jobs

# Page title
st.set_page_config(page_title="Job Recommender", layout="wide")
st.title("💼 Job Recommender System")

st.write(
    "Enter your skills, experiences, or participated projects, and we will suggest suitable job roles with responsibilities."
)

# User input
user_input = st.text_area(
    "Enter your skills (comma-separated, e.g., Python, SQL, Machine Learning):"
)

top_n = st.slider("Number of job recommendations", min_value=1, max_value=10, value=5)

# Recommend jobs button
if st.button("Find Jobs"):
    if not user_input.strip():
        st.warning("Please enter your skills!")
    else:
        # Convert input to list
        skills_list = [skill.strip() for skill in user_input.split(",")]
        
        # Get recommendations
        recommendations = recommend_jobs(skills_list, top_n=top_n)
        
        st.success(f"Top {top_n} job recommendations based on your skills:")
        
        # Display results
        for idx, row in recommendations.iterrows():
            st.subheader(f"{row['job_title']} ({row['category']})")
            st.write(f"Skills Required: {row['job_skill_set']}")
            st.progress(row['match_score'] / 100)
            st.write(f"Match Score: {row['match_score']:.2f}%")
            st.markdown("---")

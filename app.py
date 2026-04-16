import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Job Market Skills Analyzer")

df = pd.read_csv("jobs.csv")

skills = [
    "python", "sql", "excel", "tableau", "power bi",
    "machine learning", "reporting", "communication",
    "dashboards", "analytics"
]

for skill in skills:
    df[skill] = df["description"].str.lower().str.contains(skill).astype(int)

st.subheader("Skill Summary by Role")
skill_summary = df.groupby("role_group")[skills].sum()
st.dataframe(skill_summary)

fig, ax = plt.subplots(figsize=(12,6))
skill_summary.T.plot(kind="bar", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Top Skills")
overall_skills = df[skills].sum().sort_values(ascending=False)
st.bar_chart(overall_skills)

st.subheader("Skill Percentage")
skill_percent = (df[skills].sum() / len(df) * 100)
st.bar_chart(skill_percent)
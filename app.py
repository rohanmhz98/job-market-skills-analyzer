import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("📊 Job Market Skills Analyzer")
st.markdown("---")
st.markdown("Analyze in-demand skills across Analyst, Business Analyst, and Data Scientist roles.")

st.title("Job Market Skills Analyzer")

df = pd.read_csv("jobs.csv")
skills = [
    "python", "sql", "excel", "tableau", "power bi",
    "machine learning", "reporting", "communication",
    "dashboards", "analytics"
]

skill_percent = (df[skills].sum() / len(df) * 100).sort_values(ascending=False)

col1, col2 = st.columns(2)
col1.metric("Total Jobs", len(df))
col2.metric("Top Skill", skill_percent.idxmax())

skills = [
    "python", "sql", "excel", "tableau", "power bi",
    "machine learning", "reporting", "communication",
    "dashboards", "analytics"
]

for skill in skills:
    df[skill] = df["description"].str.lower().str.contains(skill).astype(int)

st.subheader("Skill Summary by Role")
st.markdown("---")
skill_summary = df.groupby("role_group")[skills].sum()
st.dataframe(skill_summary)
role = st.selectbox("Select Role", df["role_group"].unique())

filtered = df[df["role_group"] == role]

st.subheader(f"Skills for {role}")

filtered_summary = filtered[skills].sum()

st.bar_chart(filtered_summary)

fig, ax = plt.subplots(figsize=(12,6))
skill_summary.T.plot(kind="bar", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("---")
st.subheader("Top Skills")
overall_skills = df[skills].sum().sort_values(ascending=False)
st.bar_chart(overall_skills)

st.markdown("---")
st.subheader("Skill Percentage")
skill_percent = (df[skills].sum() / len(df) * 100)
st.bar_chart(skill_percent)

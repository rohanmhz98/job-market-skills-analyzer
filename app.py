import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Job Market Skills Analyzer", layout="wide")

st.title("📊 Job Market Skills Analyzer")
st.markdown("Analyze in-demand skills across Analyst, Business Analyst, and Data Scientist roles.")
st.info("This app analyzes job descriptions to identify the most in-demand skills across different roles.")
st.markdown("---")

df = pd.read_csv("jobs.csv")

skills = [
    "python", "sql", "excel", "tableau", "power bi",
    "machine learning", "reporting", "communication",
    "dashboards", "analytics"
]

for skill in skills:
    df[skill] = df["description"].str.lower().str.contains(skill).astype(int)

skill_percent = (df[skills].sum() / len(df) * 100).sort_values(ascending=False)

col1, col2 = st.columns(2)
col1.metric("📄 Total Job Listings", len(df))
col2.metric("🔥 Most In-Demand Skill", skill_percent.idxmax().upper())

st.markdown("---")
st.subheader("Skill Summary by Role")

skill_summary = df.groupby("role_group")[skills].sum()
st.dataframe(skill_summary)

fig, ax = plt.subplots(figsize=(12, 6))
skill_summary.T.plot(kind="bar", ax=ax)
ax.set_title("Skill Demand by Job Role")
ax.set_xlabel("Skills")
ax.set_ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

st.markdown("---")
st.subheader("Filter by Role")

st.sidebar.header("Filters")
role = st.sidebar.selectbox("Select Role", df["role_group"].unique())
filtered = df[df["role_group"] == role]

st.subheader(f"Skills for {role}")
filtered_summary = filtered[skills].sum()
st.bar_chart(filtered_summary)

st.markdown("---")
st.subheader("Top Skills")
overall_skills = df[skills].sum().sort_values(ascending=False)
st.bar_chart(overall_skills)
st.download_button(
    "Download Dataset",
    df.to_csv(index=False),
    file_name="jobs.csv",
    mime="text/csv"
)

st.markdown("---")
st.subheader("Skill Percentage")
st.bar_chart(skill_percent)

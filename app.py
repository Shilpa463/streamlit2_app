import streamlit as st
import pandas as pd
import numpy as np

# Page settings
st.set_page_config(
    page_title="Study Tracker",
    page_icon="📚",
    layout="wide"
)

# Sample data
df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
})

# Title
st.title("📚 My Study Tracker")
st.caption("Small steps today, big achievements tomorrow! ✨")

st.divider()

# Metric cards
col1, col2, col3 = st.columns(3)

col1.metric("⏰ Total Study Hours", "55")
col2.metric("🎯 Average Marks", "55")
col3.metric("🏆 Highest Marks", "100", "+10 vs previous")

st.divider()

# Charts
left, right = st.columns(2)

with left:
    st.subheader("📈 Learning Progress")
    st.line_chart(df, x="Hours", y="Marks")

with right:
    st.subheader("📊 Marks Comparison")
    st.bar_chart(df, x="Hours", y="Marks", color="#14B8A6")

# Table
st.subheader("📝 Study Records")
st.dataframe(df, use_container_width=True, hide_index=True)


uploaded_file = st.file_uploader("Choose a file",type=["csv"])


if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.dataframe(data) 

st.success("🌟 Keep learning. Keep growing. Keep shining!")
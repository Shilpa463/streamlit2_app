import streamlit as st
import pandas as pd
import numpy as np


df = pd.DataFrame({
    "hours_of_study" :[1,2,3,4,5,6,7,8,9,10],
    "marks" : [10,20,30,40,50,60,70,80,90,100]
})


st.title("Dataframe Example")


st.dataframe(df)  #interactive table
st.table(df)   #static table


st.line_chart(df.set_index("hours_of_study"))  #line chart
st.bar_chart(df,x="hours_of_study",y="marks")  #bar chart


uploaded_file = st.file_uploader("Choose a file",type=["csv"])


if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.dataframe(data)  #interactive table

import streamlit as st
import pandas as pd

st.title("Chai sales Dashboard")

file = st.file_uploader("Upload your CSV file", type=['csv'])
if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary")
    st.write(df.describe())
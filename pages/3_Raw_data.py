import streamlit as st
from utils.helpers import load_data

st.set_page_config(page_title="Raw Data", layout="wide")

df = load_data()

st.title("Raw Data Explorer")
st.caption("Inspect the complete dataset used in the dashboard.")
st.dataframe(df, width="stretch")
st.write("Rows:", len(df))
st.write("Columns:", len(df.columns))
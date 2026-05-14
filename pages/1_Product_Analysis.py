import streamlit as st
import plotly.express as px
from utils.helpers import load_data

st.set_page_config(page_title="Product Analysis", layout="wide")

df = load_data()

st.title("Product Analysis Dashboard")
st.caption("Deep dive into category contribution and product profitability.")

category_sales = df.groupby(["Category", "Product"], as_index=False)["Sales"].sum()

fig = px.treemap(
    category_sales,
    path=["Category", "Product"],
    values="Sales",
    title="Category and Product Contribution to Revenue",
    template="plotly_dark",
    color="Sales",
    color_continuous_scale="purples"
)
fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig, width="stretch")

profitability = (
    df.groupby("Product", as_index=False)[["Sales", "Profit"]]
    .sum()
    .sort_values("Profit", ascending=False)
)

fig2 = px.scatter(
    profitability,
    x="Sales",
    y="Profit",
    text="Product",
    size="Profit",
    color="Profit",
    title="Sales vs Profit by Product",
    template="plotly_dark",
    color_continuous_scale="blues"
)
fig2.update_traces(textposition="top center")
fig2.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)
st.plotly_chart(fig2, width="stretch")
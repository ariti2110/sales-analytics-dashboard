import streamlit as st
import plotly.express as px
from utils.helpers import load_data

st.set_page_config(page_title="Regional Analysis", layout="wide")

df = load_data()

st.title("Regional Sales Analysis")
st.caption("Compare monthly sales patterns and category contribution across regions.")

region_month = df.groupby(
    [df["Order Date"].dt.to_period("M").astype(str), "Region"],
    as_index=False
)["Sales"].sum()

region_month.columns = ["Month", "Region", "Sales"]

fig = px.line(
    region_month,
    x="Month",
    y="Sales",
    color="Region",
    markers=True,
    title="Monthly Revenue by Region",
    template="plotly_dark"
)
fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)
st.plotly_chart(fig, width="stretch")

region_category = df.groupby(["Region", "Category"], as_index=False)["Sales"].sum()

fig2 = px.bar(
    region_category,
    x="Region",
    y="Sales",
    color="Category",
    barmode="group",
    title="Category Sales by Region",
    text_auto=".2s",
    template="plotly_dark"
)
fig2.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)
st.plotly_chart(fig2, width="stretch")
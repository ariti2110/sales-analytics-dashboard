import streamlit as st
import plotly.express as px
from utils.helpers import load_data, filter_data, calculate_kpis

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def get_data():
    return load_data()

def format_inr(value: float) -> str:
    return f"₹{value:,.0f}"

def inject_css():
    st.markdown("""
    <style>
        .main {
            background: linear-gradient(180deg, #0b0f19 0%, #111827 100%);
        }

        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }

        .hero-card {
            background: linear-gradient(135deg, rgba(139,92,246,0.18), rgba(59,130,246,0.12));
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 22px;
            padding: 1.5rem 1.5rem;
            margin-bottom: 1.25rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.25);
        }

        .hero-title {
            font-size: 2rem;
            font-weight: 800;
            color: #f8fafc;
            margin-bottom: 0.2rem;
        }

        .hero-subtitle {
            font-size: 0.98rem;
            color: #cbd5e1;
            margin-bottom: 0;
        }

        .section-title {
            font-size: 1.15rem;
            font-weight: 700;
            color: #f8fafc;
            margin-top: 0.5rem;
            margin-bottom: 0.75rem;
        }

        .kpi-card {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 18px;
            padding: 1rem 1rem 0.8rem 1rem;
            box-shadow: 0 8px 20px rgba(0,0,0,0.18);
        }

        .kpi-label {
            color: #94a3b8;
            font-size: 0.9rem;
            margin-bottom: 0.35rem;
        }

        .kpi-value {
            color: #ffffff;
            font-size: 1.5rem;
            font-weight: 800;
            line-height: 1.2;
        }

        .chart-card {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 20px;
            padding: 0.75rem 0.75rem 0.35rem 0.75rem;
            margin-top: 0.5rem;
            box-shadow: 0 8px 20px rgba(0,0,0,0.18);
        }

        div[data-testid="stSidebar"] {
            background: #0b1220;
            border-right: 1px solid rgba(255,255,255,0.06);
        }

        div[data-testid="stDataFrame"] {
            border-radius: 16px;
            overflow: hidden;
        }

        .footer-note {
            color: #94a3b8;
            font-size: 0.85rem;
            text-align: center;
            margin-top: 1.2rem;
        }
    </style>
    """, unsafe_allow_html=True)

df = get_data()
inject_css()

min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

st.markdown("""
<div class="hero-card">
    <div class="hero-title">📊 Sales Analytics Dashboard</div>
    <div class="hero-subtitle">
        Dark-themed interactive dashboard for tracking revenue trends, orders, AOV, product performance, and regional sales.
    </div>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("Filters")

    selected_regions = st.multiselect(
        "Region",
        options=sorted(df["Region"].unique()),
        default=sorted(df["Region"].unique())
    )

    selected_categories = st.multiselect(
        "Category",
        options=sorted(df["Category"].unique()),
        default=sorted(df["Category"].unique())
    )

    selected_products = st.multiselect(
        "Product",
        options=sorted(df["Product"].unique()),
        default=sorted(df["Product"].unique())
    )

    selected_dates = st.date_input(
        "Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

if isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 2:
    start_date, end_date = selected_dates
else:
    start_date, end_date = min_date, max_date

filtered_df = filter_data(
    df,
    selected_regions,
    selected_categories,
    selected_products,
    start_date,
    end_date
)

kpis = calculate_kpis(filtered_df)

st.markdown('<div class="section-title">Business Snapshot</div>', unsafe_allow_html=True)
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Revenue</div>
        <div class="kpi-value">{format_inr(kpis["total_revenue"])}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Orders</div>
        <div class="kpi-value">{kpis["total_orders"]:,}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">AOV</div>
        <div class="kpi-value">{format_inr(kpis["avg_order_value"])}</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Quantity Sold</div>
        <div class="kpi-value">{kpis["total_quantity"]:,}</div>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Profit</div>
        <div class="kpi-value">{format_inr(kpis["total_profit"])}</div>
    </div>
    """, unsafe_allow_html=True)

sales_trend = filtered_df.groupby("Order Date", as_index=False)["Sales"].sum()
fig1 = px.line(
    sales_trend,
    x="Order Date",
    y="Sales",
    markers=True,
    title="Revenue Trend Over Time",
    template="plotly_dark"
)
fig1.update_traces(line_color="#8b5cf6", marker_color="#22c55e")
fig1.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#f8fafc"),
    title_font=dict(size=20)
)

st.markdown('<div class="chart-card">', unsafe_allow_html=True)
st.plotly_chart(fig1, width="stretch")
st.markdown('</div>', unsafe_allow_html=True)

left, right = st.columns(2)

with left:
    top_products = (
        filtered_df.groupby("Product", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

    fig2 = px.bar(
        top_products,
        x="Product",
        y="Sales",
        color="Sales",
        title="Top 10 Products by Revenue",
        text_auto=".2s",
        template="plotly_dark",
        color_continuous_scale="purples"
    )
    fig2.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f8fafc"),
        coloraxis_showscale=False
    )

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.plotly_chart(fig2, width="stretch")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    region_sales = (
        filtered_df.groupby("Region", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    fig3 = px.pie(
        region_sales,
        names="Region",
        values="Sales",
        title="Region-wise Revenue Share",
        hole=0.5,
        template="plotly_dark"
    )
    fig3.update_traces(
        textinfo="percent+label",
        marker=dict(colors=["#8b5cf6", "#3b82f6", "#22c55e", "#f59e0b"])
    )
    fig3.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f8fafc")
    )

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.plotly_chart(fig3, width="stretch")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Filtered Dataset</div>', unsafe_allow_html=True)
st.dataframe(filtered_df, width="stretch")

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

st.markdown('<div class="footer-note">Built with Streamlit, Pandas, and Plotly.</div>', unsafe_allow_html=True)
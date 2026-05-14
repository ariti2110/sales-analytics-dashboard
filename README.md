# 📊 Sales Analytics Dashboard

An interactive **Sales Analytics Dashboard** built using **Python, Pandas, Plotly, and Streamlit**.

## Features
- Revenue, Orders, AOV, Quantity Sold, and Profit KPIs
- Interactive filters for Region, Category, Product, and Date Range
- Revenue trend line chart
- Top 10 products by revenue
- Region-wise revenue share
- Product-level and regional analysis pages
- Raw data explorer
- CSV download option

## Tech Stack
- Python
- Streamlit
- Pandas
- Plotly Express

## Project Structure
```bash
sales-analytics-dashboard/
│── app.py
│── requirements.txt
│── README.md
│── data/
│   └── sales_data.csv
│── pages/
│   ├── 1_Product_Analysis.py
│   ├── 2_Regional_Analysis.py
│   └── 3_Raw_Data.py
│── utils/
│   └── helpers.py
```

## Run Locally
```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

## Resume Bullet Points
- Built an interactive sales analytics dashboard using Streamlit, Pandas, and Plotly to analyze revenue trends, AOV, product performance, and regional sales.
- Designed a multipage business intelligence app with dynamic filters, KPI cards, and downloadable reports for decision-ready insights.
- Implemented reusable helper functions for data loading, KPI computation, and dashboard filtering to support scalable analytics workflows.
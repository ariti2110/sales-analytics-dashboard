import pandas as pd

def load_data(path: str = "data/sales_data.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df

def filter_data(df: pd.DataFrame, regions, categories, products, start_date, end_date) -> pd.DataFrame:
    filtered = df.copy()

    if regions:
        filtered = filtered[filtered["Region"].isin(regions)]
    if categories:
        filtered = filtered[filtered["Category"].isin(categories)]
    if products:
        filtered = filtered[filtered["Product"].isin(products)]

    filtered = filtered[
        (filtered["Order Date"].dt.date >= start_date) &
        (filtered["Order Date"].dt.date <= end_date)
    ]

    return filtered

def calculate_kpis(df: pd.DataFrame) -> dict:
    total_revenue = float(df["Sales"].sum())
    total_orders = int(df["Order ID"].nunique())
    avg_order_value = total_revenue / total_orders if total_orders else 0
    total_quantity = int(df["Quantity"].sum())
    total_profit = float(df["Profit"].sum())

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "avg_order_value": avg_order_value,
        "total_quantity": total_quantity,
        "total_profit": total_profit,
    }
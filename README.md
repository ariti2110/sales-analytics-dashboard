# 📊 Sales Analytics Dashboard







An interactive **Sales Analytics Dashboard** built using **Python, Pandas, Plotly, and Streamlit**. This project helps analyze business performance through revenue trends, average order value, product-level insights, regional comparisons, and interactive filtering.

## Demo Preview
Add screenshots here after running the app locally:

- `screenshots/dashboard-home.png`
- `screenshots/product-analysis.png`
- `screenshots/regional-analysis.png`

You can also add a live app link here after deployment:

**Live Demo:** `Add your Streamlit Cloud URL here`

## Features
- KPI cards for Revenue, Orders, AOV, Quantity Sold, and Profit
- Interactive sidebar filters for Region, Category, Product, and Date Range
- Revenue trend visualization over time
- Top-selling product analysis
- Region-wise sales comparison
- Multipage navigation for overview and deeper analysis
- Download filtered dataset as CSV

## Tech Stack
- **Python** for data processing logic
- **Pandas** for cleaning, transformation, and KPI computation
- **Plotly** for interactive charts
- **Streamlit** for dashboard UI and deployment

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

## Dataset Columns
The sample dataset contains the following columns:
- `Order ID`
- `Order Date`
- `Customer ID`
- `Region`
- `Category`
- `Product`
- `Quantity`
- `Unit Price`
- `Sales`
- `Profit`

## Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/sales-analytics-dashboard.git
cd sales-analytics-dashboard
pip install -r requirements.txt
```

## Run Locally
```bash
streamlit run app.py
```

After running the command, Streamlit will open the app in your browser locally.

## Deployment
You can deploy this project easily using **Streamlit Community Cloud**.

### Steps to deploy
1. Push this project to GitHub.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Click **New app**.
4. Select your GitHub repository.
5. Choose `app.py` as the main file.
6. Deploy the app.

## Resume Bullet Points
Use these directly in your resume:

- Built an interactive sales analytics dashboard using **Python, Pandas, Plotly, and Streamlit** to track revenue trends, AOV, top-selling products, and regional performance.
- Designed dynamic filters and multipage views to enable drill-down analysis and improve dashboard usability.
- Automated KPI generation and reporting workflows from transactional sales data using reusable helper functions.

## GitHub Highlights
This project demonstrates:
- Data cleaning and preprocessing with Pandas
- KPI engineering and exploratory analytics
- Interactive dashboard development with Streamlit
- Visual storytelling with Plotly charts
- Modular code structure for maintainability

## Future Enhancements
- Add sales forecasting using Prophet or ARIMA
- Add customer segmentation using RFM analysis or clustering
- Connect the app to SQL or cloud-based data storage
- Add authentication and role-based access
- Deploy with a public demo URL and screenshots

## Author
**Ariti**  
Data Science Intern | Aspiring Data Scientist | Software Developer

You can replace this section with your GitHub, LinkedIn, and portfolio links.

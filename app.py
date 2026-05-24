import streamlit as st

st.set_page_config(
    page_title="Financial Forecasting Dashboard",
    layout="wide"
)

st.title("Financial Forecasting & Model Comparison Dashboard")

st.markdown("""
Welcome to the Financial Forecasting Dashboard.

Compare Machine Learning and Deep Learning models
across different financial assets such as:

- Stocks
- Gold
- Crude Oil
""")

asset_choice = st.selectbox(
    "Choose Asset Type",
    [
        "Stocks",
        "Gold",
        "Crude Oil"
    ]
)

# STOCKS SECTION
if asset_choice == "Stocks":

    company_choice = st.selectbox(
        "Choose Company",
        [
            "Tesla",
            "Apple",
            "Amazon"
        ]
    )

    st.subheader(f"{company_choice} Analysis Dashboard")

    

# GOLD SECTION
elif asset_choice == "Gold":

    st.subheader("Gold Price Analysis Dashboard")

# CRUDE OIL SECTION
elif asset_choice == "Crude Oil":

    st.subheader("Crude Oil Price Analysis Dashboard")

st.info("Coming Soon")

import pandas as pd

results_df = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Random Forest",
        "XGBoost",
        "LSTM"
    ],

    "MAE": [
        5.7608,
        6.7108,
        7.0787,
        10.1034
    ],

    "RMSE": [
        8.0601,
        9.2664,
        9.5836,
        13.7530
    ],

    "R2 Score": [
        0.9691,
        0.9591,
        0.9563,
        0.9132
    ]
})

st.write("## Model Performance Comparison")

st.dataframe(results_df)
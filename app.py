import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

lr_pred_df = pd.read_csv(
    "data/final/lr_predictions.csv"
)
rf_pred_df = pd.read_csv(
    "data/final/rf_predictions.csv"
)
xgb_pred_df = pd.read_csv(
    "data/final/xgb_predictions.csv"
)

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

st.write("## R2 Score Comparison")

fig, ax = plt.subplots(figsize=(8,5))

sb.barplot(
    x="Model",
    y="R2 Score",
    data=results_df,
    ax=ax
)

ax.set_title("R2 Score Comparison")

st.pyplot(fig)


best_model = results_df.loc[
    results_df['R2 Score'].idxmax()
]

best_model_name = best_model['Model']

st.write("## Best Performing Model")

st.success(
    f"""
    Best Model: {best_model_name}

    R2 Score: {best_model['R2 Score']}

    RMSE: {best_model['RMSE']}
    """
)

# Load prediction file based on best model

if best_model_name == "Linear Regression":

    pred_df = pd.read_csv(
        "data/final/lr_predictions.csv"
    )

elif best_model_name == "Random Forest":

    pred_df = pd.read_csv(
        "data/final/rf_predictions.csv"
    )

elif best_model_name == "XGBoost":

    pred_df = pd.read_csv(
        "data/final/xgb_predictions.csv"
    )

elif best_model_name == "LSTM":

    pred_df = pd.read_csv(
        "data/final/lstm_predictions.csv"
    )

# Plot graph

st.write(
    f"## Actual vs Predicted Prices ({best_model_name})"
)

fig2, ax2 = plt.subplots(figsize=(12,6))

ax2.plot(
    pred_df["Actual"].values[:100],
    label="Actual"
)

ax2.plot(
    pred_df["Predicted"].values[:100],
    label="Predicted"
)

ax2.set_title(
    f"{best_model_name}: Actual vs Predicted"
)

ax2.legend()

st.pyplot(fig2)

st.write("## Model Insights")

if best_model_name == "Linear Regression":

    st.info("""
    Linear Regression performed best because the engineered
    features showed strong linear relationships with
    Company's stock prices.

    Lag features and moving averages contributed significantly
    to prediction accuracy.
    """)

elif best_model_name == "Random Forest":

    st.info("""
    Random Forest captured nonlinear patterns effectively
    and reduced sensitivity to noise.

    Feature importance analysis showed strong dependence
    on closing price and lag features.
    """)

elif best_model_name == "XGBoost":

    st.info("""
    XGBoost achieved strong predictive performance by
    sequentially correcting previous model errors.

    The model effectively utilized important price-based
    features for forecasting.
    """)

elif best_model_name == "LSTM":

    st.info("""
    LSTM captured temporal dependencies in stock prices,
    but performance was slightly limited due to dataset size.

    Deep learning models generally perform better with
    larger sequential datasets.
    """)
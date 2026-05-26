import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Financial Forecasting Dashboard",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------

st.markdown(
    """
    <h1 style='text-align:center; color:#00ADB5;'>
        Financial Asset Forecasting Dashboard
    </h1>

    <p style='text-align:center; font-size:20px;'>
        Compare Machine Learning & Deep Learning models
        on multiple financial assets.
    </p>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("Dashboard Controls")

dataset_name = st.sidebar.selectbox(

    "Choose Dataset",

    [
        "tesla",
        "apple",
        "gold",
        "oil",
        "samsung"
    ]
)

# -----------------------------
# LOAD DATA
# -----------------------------

comparison_df = pd.read_csv(
    f"results/{dataset_name}/{dataset_name}_comparison.csv"
)

pred_df = pd.read_csv(
    f"results/{dataset_name}/{dataset_name}_predictions.csv"
)

# -----------------------------
# BEST + WORST MODEL
# -----------------------------

best_model = comparison_df.iloc[0]["Model"]

worst_model = comparison_df.iloc[-1]["Model"]

# -----------------------------
# METRICS
# -----------------------------

st.subheader("Model Performance Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Best Model",
    best_model
)

col2.metric(
    "Worst Model",
    worst_model
)

col3.metric(
    "Best R² Score",
    round(
        comparison_df.iloc[0]["R2"],
        4
    )
)

col4.metric(
    "Lowest RMSE",
    round(
        comparison_df["RMSE"].min(),
        2
    )
)

# -----------------------------
# COMPARISON TABLE
# -----------------------------

st.subheader("Model Comparison Table")

st.dataframe(
    comparison_df,
    use_container_width=True
)

# -----------------------------
# GRAPH
# -----------------------------

st.subheader("Actual vs Predicted Prices")

fig, ax = plt.subplots(
    figsize=(14,6)
)

ax.plot(
    pred_df["Actual"],
    label="Actual"
)

ax.plot(
    pred_df["Predicted"],
    label="Predicted"
)

ax.set_title(
    f"{dataset_name.upper()} Price Prediction"
)

ax.set_xlabel("Time")

ax.set_ylabel("Price")

ax.legend()

st.pyplot(fig)

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("---")

st.markdown(
    """
    <center>
        Built using Machine Learning, Deep Learning,
        Streamlit & Python.
    </center>
    """,
    unsafe_allow_html=True
)
# Upgraded Streamlit Dashboard (`app.py`)
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import random

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="FinSight AI",
    layout="wide",
    page_icon="📈"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    /* Entire App */

    .stApp {

        background: linear-gradient(
            135deg,
            #020617,
            #0F172A,
            #111827
        );

        color: white;
    }

    /* Main */

    .main {

        background: transparent;
        color: white;
    }

    /* Headings */

    h1 {

        color: #F8FAFC !important;

        font-weight: 800 !important;

        letter-spacing: 1px;
    }

    h2, h3 {

        color: #38BDF8 !important;

        font-weight: 700 !important;
    }

    /* Normal Text */

    p, label, div {

        color: #E2E8F0;
    }

    /* Finance Fact Box */

    .fact-box {

        background: linear-gradient(
            135deg,
            #1E3A8A,
            #0F172A
        );

        padding: 28px;

        border-radius: 18px;

        border: 1px solid rgba(255,255,255,0.1);

        box-shadow: 0px 8px 30px rgba(56,189,248,0.25);

        margin-top: 25px;

        margin-bottom: 30px;

        font-size: 22px;

        color: white !important;

        line-height: 1.8;
    }

    /* Asset Box */

    .asset-box {

        background: linear-gradient(
            135deg,
            #111827,
            #1E293B
        );

        padding: 24px;

        border-radius: 18px;

        margin-top: 15px;

        margin-bottom: 20px;

        border: 1px solid rgba(255,255,255,0.08);

        box-shadow: 0px 6px 20px rgba(0,0,0,0.35);

        font-size: 18px;
    }

    /* Metric Cards */

    [data-testid="metric-container"] {

        background: linear-gradient(
            135deg,
            #111827,
            #1E293B
        );

        border: 1px solid rgba(255,255,255,0.08);

        padding: 18px;

        border-radius: 18px;

        box-shadow: 0px 4px 18px rgba(0,0,0,0.3);
    }

    /* Buttons */

    .stButton > button {

        background: linear-gradient(
            135deg,
            #2563EB,
            #38BDF8
        ) !important;

        color: white !important;

        font-size: 20px;

        font-weight: 700;

        border-radius: 14px;

        padding: 14px 24px;

        border: none;

        transition: all 0.3s ease;

        box-shadow: 0px 4px 18px rgba(56,189,248,0.35);
    }

    .stButton > button:hover {

        transform: translateY(-3px) scale(1.02);

        box-shadow: 0px 8px 25px rgba(56,189,248,0.5);

        color: white !important;
    }

    /* ----------------------------- */
    /* SELECTBOX FIX */
    /* ----------------------------- */

    .stSelectbox div[data-baseweb="select"] {

        background-color: white !important;

        border-radius: 12px !important;
    }

    .stSelectbox div[data-baseweb="select"] * {

        color: black !important;
    }

    .stSelectbox svg {

        fill: black !important;
    }

    /* Dropdown Menu */

    div[role="listbox"] {

        background-color: white !important;

        color: black !important;
    }

    div[role="option"] {

        color: black !important;

        background-color: white !important;
    }

    /* Tables */

    .stDataFrame {

        border-radius: 14px;

        overflow: hidden;
    }

    /* Divider */

    hr {

        border: 1px solid rgba(255,255,255,0.1);
    }

    </style>
    """,
    unsafe_allow_html=True
)
# --------------------------------------------------
# RANDOM FINANCE FACTS
# --------------------------------------------------

finance_facts = [

    "The stock market historically trends upward despite short-term crashes.",

    "Gold is considered a safe-haven asset during economic uncertainty.",

    "LSTM models are designed to understand sequential patterns in time-series data.",

    "Tesla stock once surged more than 700% within a single year.",

    "Overfitting happens when a model memorizes instead of learning patterns.",

    "Random Forest combines multiple decision trees for prediction.",

    "Machine Learning models often struggle with highly volatile markets.",

    "Linear Regression works surprisingly well on strongly trending datasets.",

    "Feature Engineering is often more important than model complexity.",

    "Forecasting financial markets is one of the hardest AI problems."
]

random_fact = random.choice(finance_facts)

# --------------------------------------------------
# ASSET DESCRIPTIONS
# --------------------------------------------------

asset_descriptions = {

    "tesla": "Tesla is a high-growth EV company known for extreme volatility and strong trend movement.",

    "apple": "Apple is one of the world's largest technology companies with relatively stable stock behavior.",

    "gold": "Gold is a traditional safe-haven financial asset often used during economic instability.",

    "oil": "Oil prices are heavily influenced by geopolitical events and global demand.",

    "samsung": "Samsung is a global electronics leader with strong market influence in Asia."
}

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "home"

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if st.session_state.page == "home":

    st.markdown(
        """
        <h1 style='text-align:center;'>
            FinSight AI
        </h1>
        <h3 style='text-align:center;'>
           A Multi-Model Financial Forecasting Dashboard
        </h3>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h4 style='text-align:center;'>
            Compare Machine Learning & Deep Learning Models
            on Financial Time-Series Data
        </h4>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class='fact-box'>
            <b>Did you know? 😯:</b><br>
            {random_fact}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## What do you want to do today?")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("📊 Model Comparison", use_container_width=True):
            st.session_state.page = "comparison"
            st.rerun()

    with col2:

        if st.button("🚀 Forecasting", use_container_width=True):
            st.session_state.page = "forecasting"
            st.rerun()

# --------------------------------------------------
# FORECASTING PAGE
# --------------------------------------------------

elif st.session_state.page == "forecasting":

    st.title("🚀 Forecasting")

    st.info("Advanced Future Forecasting Module Coming Soon...")

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"
        st.rerun()

# --------------------------------------------------
# MODEL COMPARISON PAGE
# --------------------------------------------------

elif st.session_state.page == "comparison":

    st.title("📊 Model Comparison")

    dataset_name = st.selectbox(
        "Select Dataset",
        [
            "tesla",
            "apple",
            "gold",
            "oil",
            "samsung"
        ]
    )

    
    st.markdown(
        f"""
        <div class='asset-box'>
            <b>{dataset_name.upper()}</b><br><br>
            {asset_descriptions[dataset_name]}
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------
    # LOAD FILES
    # --------------------------------------------------

    comparison_df = pd.read_csv(
        f"results/{dataset_name}/{dataset_name}_comparison.csv"
    )

    pred_df = pd.read_csv(
        f"results/{dataset_name}/{dataset_name}_predictions.csv"
    )

    # --------------------------------------------------
    # BEST / WORST MODELS
    # --------------------------------------------------

    best_model = comparison_df.iloc[0]["Model"]

    worst_model = comparison_df.iloc[-1]["Model"]

    # --------------------------------------------------
    # METRICS
    # --------------------------------------------------

    st.subheader("Performance Summary")

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
        "Best R²",
        round(comparison_df.iloc[0]["R2"], 4)
    )

    col4.metric(
        "Lowest RMSE",
        round(comparison_df["RMSE"].min(), 2)
    )

    # --------------------------------------------------
    # COMPARISON TABLE
    # --------------------------------------------------

    st.subheader("Model Comparison Table")

    st.dataframe(
        comparison_df,
        use_container_width=True
    )

    # --------------------------------------------------
    # R^2 BAR CHART
    # --------------------------------------------------

    st.subheader("Model Performance Comparison (R² Score)")
    fig_bar=go.Figure()
    fig_bar.add_trace(
        go.Bar(
            x=comparison_df["Model"],
            y=comparison_df["R2"],
            text=round(comparison_df["R2"], 4),
            textposition="outside",
        )
    )
    fig_bar.update_layout(

        template="plotly_dark",

        yaxis_title="R² Score",

        xaxis_title="Model",

        title=f"R² Score Comparison for {dataset_name.upper()}",

        height=500
    )
    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

    # --------------------------------------------------
    # INTERACTIVE PREDICTION GRAPH
    # --------------------------------------------------

    st.subheader("Interactive Forecast Visualization")

    fig = go.Figure()

    # Actual Line

    fig.add_trace(

        go.Scatter(

            y=pred_df["Actual"],

            mode="lines",
            name="Actual",

            line=dict(
                width=3
            )
        )
    )

    # Predicted Line

    fig.add_trace(

        go.Scatter(

            y=pred_df["Predicted"],

            mode="lines",
            name="Predicted",

            line=dict(
                width=3
            )
        )
    )

    fig.update_layout(

        title=f"{dataset_name.upper()} Price Forecast",

        xaxis_title="Time",

        yaxis_title="Price",

        template="plotly_dark",

        hovermode="x unified",

        height=600,
         legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------
    # INFERENCE SECTION
    # --------------------------------------------------

    st.subheader("Inference & Insights")


    best_r2 = comparison_df.iloc[0]["R2"]

    worst_r2 = comparison_df.iloc[-1]["R2"]

    st.success(
        f"{best_model} performed best with an R² score of {round(best_r2,4)}."
    )

    st.warning(
        f"{worst_model} struggled the most on this dataset with an R² score of {round(worst_r2,4)}."
    )

    if best_model == "Linear Regression":

        st.info(
            "Linear Regression performed well because the dataset shows strong trend continuity and linear relationships."
        )

    elif best_model == "LSTM":

        st.info(
            "LSTM captured sequential dependencies effectively, making it suitable for time-series forecasting."
        )

    elif best_model == "Random Forest":

        st.info(
            "Random Forest handled nonlinear relationships effectively using ensemble learning."
        )

    elif best_model == "XGBoost":

        st.info(
            "XGBoost optimized prediction performance using gradient boosting techniques."
        )

    # --------------------------------------------------
    # BACK BUTTON
    # --------------------------------------------------

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"
        st.rerun()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

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


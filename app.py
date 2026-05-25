import  streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

st.title("Financial Asset Forecasting Dashboard")

st.write(
    """
    Compare ML and Deep Learning models
    on multiple financial assets.
    """
)

asset_choice = st.selectbox(
    "Choose Asset",
    [
        "tesla",
        "apple",
        "gold",
        "oil",
        "samsung"
    ]
)

lr_model = joblib.load(
    f"models/{asset_choice}_linear_regression.pkl"
)

rf_model = joblib.load(
    f"models/{asset_choice}_random_forest.pkl"
)

xgb_model = joblib.load(
    f"models/{asset_choice}_xgboost.pkl"
)

scaler = joblib.load(
    f"models/{asset_choice}_scaler.pkl"
)

lstm_model = load_model(
    f"models/{asset_choice}_lstm.h5"
)

st.success(
    f"{asset_choice.upper()} models loaded successfully."
)
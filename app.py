import streamlit as st
import joblib
from tensorflow.keras.models import load_model  



st.title("Tesla Stock Prediction App")

model_choice = st.sidebar.selectbox(
    "Choose Model",
    [
        "Linear Regression",
        "Random Forest",
        "XGBoost",
        "LSTM"
    ]
)

st.write("Selected Model:", model_choice)

lr_model = joblib.load(
    "models/linear_regression.pkl"
)

rf_model = joblib.load(
    "models/random_forest.pkl"
)

xgb_model = joblib.load(
    "models/xgboost.pkl"
)

lstm_model = load_model(
    "models/lstm_tesla_stock_model.h5"
)

scaler = joblib.load(
    "models/scaler.pkl"
)

st.header("Enter Stock Data")

open_price = st.number_input("Open Price")

high_price = st.number_input("High Price")

low_price = st.number_input("Low Price")

volume = st.number_input("Volume")

predict_button = st.button("Predict Stock Price")

if predict_button:

    input_data = [[
        volume,
        open_price,
        high_price,
        low_price
    ]]

    prediction = lr_model.predict(input_data)

    st.success(
        f"Predicted Closing Price: ${prediction[0]}"
    )
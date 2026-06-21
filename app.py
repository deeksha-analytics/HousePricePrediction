import streamlit as st
import pickle
import pandas as pd

# Load model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page Configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# Title
st.title("🏠 House Price Prediction Application")
st.markdown(
    "Predict house prices using a Machine Learning Linear Regression Model."
)

# Sidebar
st.sidebar.header("About Project")
st.sidebar.info(
    """
    Machine Learning House Price Prediction Application

    Model: Linear Regression

    Dataset: California Housing Dataset

    Built using:
    - Python
    - Scikit-Learn
    - Streamlit
    """
)

# User Inputs
st.header("Enter House Details")

col1, col2 = st.columns(2)

with col1:
    MedInc = st.number_input(
        "Median Income",
        value=5.0
    )
    HouseAge = st.number_input(
        "House Age",
        value=20.0
    )
    AveRooms = st.number_input(
        "Average Rooms",
        value=5.0
    )
    AveBedrms = st.number_input(
        "Average Bedrooms",
        value=1.0
    )

with col2:
    Population = st.number_input(
        "Population",
        value=1000.0
    )
    AveOccup = st.number_input(
        "Average Occupancy",
        value=3.0
    )
    Latitude = st.number_input(
        "Latitude",
        value=34.0
    )
    Longitude = st.number_input(
        "Longitude",
        value=-118.0
    )

# Prediction
if st.button("Predict Price"):

    input_data = pd.DataFrame(
        [[
            MedInc,
            HouseAge,
            AveRooms,
            AveBedrms,
            Population,
            AveOccup,
            Latitude,
            Longitude
        ]],
        columns=[
            "MedInc",
            "HouseAge",
            "AveRooms",
            "AveBedrms",
            "Population",
            "AveOccup",
            "Latitude",
            "Longitude"
        ]
    )
    prediction = model.predict(input_data)
    actual_price = prediction[0] * 100000
    st.success(
        f"🏡 Estimated House Price: ${actual_price:,.2f}"
    )
# Footer
st.markdown("---")
st.markdown(
    "Created by Deeksha Mishra | B.Tech CSE (Data Science)"
)
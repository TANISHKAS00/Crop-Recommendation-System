import streamlit as st
import pandas as pd
import joblib

# =========================
# LOAD MODELS
# =========================

crop_model = joblib.load("model.pkl")
crop_encoder = joblib.load("label_encoder.pkl")

soil_encoder = joblib.load("soil_encoder.pkl")

fertilizer_model = joblib.load("fertilizer_model.pkl")
fertilizer_encoder = joblib.load("fertilizer_encoder.pkl")

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Smart Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)

# =========================
# TITLE
# =========================

st.title("🌾 Smart Crop Recommendation System")
st.markdown(
    "### AI Based Crop & Fertilizer Recommendation"
)

st.markdown("---")

# =========================
# INPUTS
# =========================

col1, col2 = st.columns(2)

with col1:

    N = st.number_input(
        "Nitrogen (N)",
        min_value=0,
        max_value=200,
        value=90
    )

    P = st.number_input(
        "Phosphorus (P)",
        min_value=0,
        max_value=200,
        value=40
    )

    K = st.number_input(
        "Potassium (K)",
        min_value=0,
        max_value=200,
        value=40
    )

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=60.0,
        value=25.0
    )

with col2:

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0
    )

    ph = st.number_input(
        "Soil pH",
        min_value=0.0,
        max_value=14.0,
        value=6.5
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=500.0,
        value=200.0
    )

    soil_type = st.selectbox(
        "Soil Type",
        soil_encoder.classes_
    )

# =========================
# BUTTON
# =========================

if st.button("🚀 Recommend Crop & Fertilizer"):

    soil_encoded = soil_encoder.transform(
        [soil_type]
    )[0]

    # =========================
    # CROP PREDICTION
    # =========================

    crop_input = pd.DataFrame(
        [[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall,
            soil_encoded
        ]],
        columns=[
            "N",
            "P",
            "K",
            "temperature",
            "humidity",
            "ph",
            "rainfall",
            "soil_type"
        ]
    )

    crop_prediction = crop_model.predict(
        crop_input
    )

    crop_name = crop_encoder.inverse_transform(
        crop_prediction
    )[0]

    # =========================
    # FERTILIZER PREDICTION
    # =========================

    fertilizer_input = pd.DataFrame(
        [[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall,
            soil_encoded
        ]],
        columns=[
            "N",
            "P",
            "K",
            "temperature",
            "humidity",
            "ph",
            "rainfall",
            "soil_type"
        ]
    )

    fertilizer_prediction = fertilizer_model.predict(
        fertilizer_input
    )

    fertilizer_name = fertilizer_encoder.inverse_transform(
        fertilizer_prediction
    )[0]

    st.markdown("---")

    st.success(
        f"🌱 Recommended Crop: {crop_name}"
    )

    st.info(
        f"💊 Recommended Fertilizer: {fertilizer_name}"
    )

    st.markdown("---")

    st.subheader("📊 Input Summary")

    summary = pd.DataFrame({

        "Parameter": [
            "Nitrogen",
            "Phosphorus",
            "Potassium",
            "Temperature",
            "Humidity",
            "pH",
            "Rainfall",
            "Soil Type"
        ],

        "Value": [
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall,
            soil_type
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True
    )
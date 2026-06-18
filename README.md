# 🌾 AI-Powered Crop & Fertilizer Recommendation System using Machine Learning

An intelligent Machine Learning-based agricultural decision support system that recommends the most suitable crop and fertilizer based on soil nutrients, weather conditions, rainfall, pH level, and soil type.

The project compares multiple Machine Learning models and automatically selects the best-performing model for deployment through an interactive Streamlit web application.

---

## 🚀 Live Application

🔗 Streamlit App

[https://crop-recommendation-system-mhepwy5vnwwfwuarbu5jgy.streamlit.app/]

---

## 📂 GitHub Repository

🔗 Repository Link

[https://github.com/TANISHKAS00/Crop-Recommendation-System]

---


---

# 📖 Project Overview

Agriculture is one of the most important sectors worldwide. Farmers often face challenges in selecting the right crop and fertilizer according to soil and environmental conditions.

This project uses Machine Learning techniques to assist farmers in making informed decisions by predicting:

✅ Best Crop to Cultivate

✅ Recommended Fertilizer

based on real-world agricultural parameters.

The system provides instant recommendations through a user-friendly Streamlit interface.

---

# 🎯 Problem Statement

Farmers often rely on traditional knowledge and experience while selecting crops and fertilizers.

Incorrect decisions may result in:

- Lower crop yield
- Soil degradation
- Increased fertilizer costs
- Reduced profitability

This project aims to solve these issues using data-driven recommendations.

---

# 🎯 Objectives

- Recommend the most suitable crop
- Recommend appropriate fertilizer
- Analyze soil conditions
- Compare multiple machine learning models
- Select the best-performing model
- Deploy the solution as a web application

---

# 📊 Dataset Description

The project is based on the Crop Recommendation Dataset.

### Features Used

| Feature | Description |
|----------|------------|
| N | Nitrogen Content |
| P | Phosphorus Content |
| K | Potassium Content |
| Temperature | Temperature (°C) |
| Humidity | Relative Humidity (%) |
| pH | Soil pH |
| Rainfall | Rainfall (mm) |
| Soil Type | Soil Category |
| Crop Label | Target Crop |
| Fertilizer | Recommended Fertilizer |

---

# 🌱 Soil Type Feature Engineering

The original dataset did not contain soil information.

To make the project more realistic, a synthetic soil type feature was generated based on crop suitability and agricultural domain knowledge.

### Soil Types Used

- Clay
- Loamy
- Sandy
- Black Soil
- Red Soil
- Alluvial Soil

---

# 💊 Fertilizer Recommendation System

A fertilizer recommendation feature was added using agricultural nutrient requirements.

Examples of fertilizers included:

- Urea
- DAP
- NPK 10-26-26
- NPK 20-20-20
- Potash
- Organic Compost

This makes the project more practical and industry-oriented.

---

# ⚙️ Project Workflow

```text
Data Collection
        ↓
Data Preprocessing
        ↓
Soil Type Generation
        ↓
Fertilizer Generation
        ↓
Feature Encoding
        ↓
Train-Test Split
        ↓
Model Training
        ↓
Model Comparison
        ↓
Best Model Selection
        ↓
Model Serialization
        ↓
Streamlit Deployment
```

---

# 🤖 Machine Learning Models Compared

The following models were trained and evaluated:

### 1. Decision Tree Classifier

### 2. Random Forest Classifier

### 3. XGBoost Classifier

### 4. LightGBM Classifier

### 5. CatBoost Classifier

---

# 📈 Model Performance

| Model | Accuracy |
|---------|---------|
| Random Forest | 100.00% |
| CatBoost | 100.00% |
| LightGBM | 100.00% |
| Decision Tree | 99.77% |
| XGBoost | 99.54% |

---

# 🏆 Best Performing Models

The following models achieved perfect accuracy:

- Random Forest
- CatBoost
- LightGBM

For deployment, Random Forest was selected because of:

- Fast Prediction Speed
- Stable Performance
- Easy Deployment
- Lower Computational Cost

---

# ⚠️ Note on Accuracy

The soil type and fertilizer features were generated using rule-based synthetic methods to simulate realistic agricultural conditions.

Due to the structured nature of the generated dataset, some machine learning models achieved very high accuracy.

The primary objective of this project is to demonstrate:

- Data Preprocessing
- Feature Engineering
- Model Comparison
- Model Deployment
- Agricultural Decision Support Systems

---

# 🛠 Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- LightGBM
- CatBoost
- Joblib
- Streamlit

---

# 🌟 Key Features

✅ Crop Recommendation

✅ Fertilizer Recommendation

✅ Soil Type Analysis

✅ Machine Learning Model Comparison

✅ Best Model Selection

✅ Interactive Streamlit Interface

✅ Manual User Inputs

✅ Real-Time Predictions

✅ PKL Model Deployment

✅ GitHub & Streamlit Ready

---

# 📁 Project Structure

```bash
Crop_Recommendation/
│
├── Crop_recommendation.csv
├── final_crop_data.csv
├── final_crop_fertilizer_data.csv
│
├── prepare_data.py
├── add_fertilizer.py
├── Train_model.py
├── fertilizer_model.py
│
├── model.pkl
├── fertilizer_model.pkl
├── label_encoder.pkl
├── soil_encoder.pkl
├── fertilizer_encoder.pkl
│
├── app.py
├── requirements.txt
│
└── README.md
```

---

# 🖥 Streamlit Application

The web application allows users to manually enter:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall
- Soil Type

The application instantly predicts:

🌱 Recommended Crop

💊 Recommended Fertilizer

---

# ▶️ How To Run Locally

### Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### Move Into Project Folder

```bash
cd Crop_Recommendation
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

# 🔮 Future Enhancements

- Crop Yield Prediction
- Plant Disease Detection
- Weather API Integration
- Fertilizer Quantity Recommendation
- Soil Health Monitoring
- Mobile Application Development
- Multi-language Support

---

# 🎓 Academic Relevance

This project demonstrates:

- Machine Learning Classification
- Feature Engineering
- Synthetic Data Generation
- Model Evaluation
- Model Comparison
- Streamlit Deployment
- End-to-End ML Pipeline Development

---

# 📬 Connect With Me

GitHub:[https://github.com/TANISHKAS00]

LinkedIn:[https://www.linkedin.com/in/tanishka-sharma-1198a7355/]

---

# ⭐ Support

If you found this project useful, consider giving this repository a Star ⭐ on GitHub.

---

© 2026 | Developed with ❤️ using Python, Machine Learning, and Streamlit

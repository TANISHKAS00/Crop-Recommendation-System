import pandas as pd
import numpy as np

df = pd.read_csv("crop_recommendation.csv")

soil_mapping = {
    "rice": "Clay",
    "maize": "Loamy",
    "chickpea": "Black",
    "kidneybeans": "Loamy",
    "pigeonpeas": "Red",
    "mothbeans": "Sandy",
    "mungbean": "Loamy",
    "blackgram": "Black",
    "lentil": "Loamy",
    "pomegranate": "Red",
    "banana": "Alluvial",
    "mango": "Laterite",
    "grapes": "Black",
    "watermelon": "Sandy",
    "muskmelon": "Sandy",
    "apple": "Loamy",
    "orange": "Red",
    "papaya": "Alluvial",
    "coconut": "Coastal",
    "cotton": "Black",
    "jute": "Alluvial",
    "coffee": "Laterite"
}

df["soil_type"] = df["label"].map(soil_mapping)

df.to_csv("final_crop_data.csv", index=False)

print("Dataset Created Successfully")
print(df.head())
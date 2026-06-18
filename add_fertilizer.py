import pandas as pd

df = pd.read_csv("final_crop_data.csv")

fertilizer_map = {

    "rice": "Urea",
    "maize": "NPK",
    "chickpea": "DAP",
    "kidneybeans": "Compost",
    "pigeonpeas": "DAP",
    "mothbeans": "Compost",
    "mungbean": "Urea",
    "blackgram": "NPK",
    "lentil": "DAP",
    "pomegranate": "Organic Manure",
    "banana": "Potash",
    "mango": "Organic Manure",
    "grapes": "NPK",
    "watermelon": "Potash",
    "muskmelon": "Potash",
    "apple": "Organic Manure",
    "orange": "NPK",
    "papaya": "Urea",
    "coconut": "Organic Manure",
    "cotton": "NPK",
    "jute": "Urea",
    "coffee": "Organic Manure"
}

df["fertilizer"] = df["label"].map(fertilizer_map)

df.to_csv("final_crop_fertilizer_data.csv", index=False)

print("Done")
print(df.head())
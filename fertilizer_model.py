import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("final_crop_fertilizer_data.csv")

print("Dataset Shape:", df.shape)

# Encode Soil Type
soil_encoder = LabelEncoder()
df["soil_type"] = soil_encoder.fit_transform(df["soil_type"])

# Encode Fertilizer
fert_encoder = LabelEncoder()
df["fertilizer"] = fert_encoder.fit_transform(df["fertilizer"])

# Features
X = df.drop("fertilizer", axis=1)

# Remove crop label if present
if "label" in X.columns:
    X = X.drop("label", axis=1)

y = df["fertilizer"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

acc = accuracy_score(y_test, pred)

print("Accuracy:", round(acc, 4))

# Save Model
pickle.dump(
    model,
    open("fertilizer_model.pkl", "wb")
)

pickle.dump(
    fert_encoder,
    open("fertilizer_encoder.pkl", "wb")
)

print("fertilizer_model.pkl saved")
print("fertilizer_encoder.pkl saved")
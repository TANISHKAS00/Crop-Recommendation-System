import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier

from sklearn.metrics import accuracy_score

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_csv("final_crop_data.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# ==========================
# ENCODE SOIL TYPE
# ==========================

soil_encoder = LabelEncoder()
df["soil_type"] = soil_encoder.fit_transform(df["soil_type"])

# ==========================
# ENCODE CROP LABEL
# ==========================

crop_encoder = LabelEncoder()
df["label"] = crop_encoder.fit_transform(df["label"])

# ==========================
# FEATURES & TARGET
# ==========================

X = df.drop("label", axis=1)
y = df["label"]

# ==========================
# TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)

# ==========================
# MODELS
# ==========================

models = {

    "Decision Tree":
        DecisionTreeClassifier(
            random_state=42
        ),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=200,
            random_state=42
        ),

    "XGBoost":
        XGBClassifier(
            n_estimators=200,
            max_depth=6,
            learning_rate=0.1,
            use_label_encoder=False,
            eval_metric="mlogloss",
            random_state=42
        ),

    "LightGBM":
        LGBMClassifier(
            n_estimators=200,
            random_state=42
        ),

    "CatBoost":
        CatBoostClassifier(
            iterations=200,
            verbose=0,
            random_state=42
        )
}

# ==========================
# TRAINING & COMPARISON
# ==========================

results = []

best_model = None
best_accuracy = 0
best_model_name = ""

print("\n==============================")
print("MODEL COMPARISON")
print("==============================\n")

for name, model in models.items():

    print(f"Training {name}...")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    results.append([name, accuracy])

    print(f"{name} Accuracy: {accuracy:.4f}")

    if accuracy > best_accuracy:

        best_accuracy = accuracy
        best_model = model
        best_model_name = name

# ==========================
# RESULTS TABLE
# ==========================

results_df = pd.DataFrame(
    results,
    columns=["Model", "Accuracy"]
)

results_df = results_df.sort_values(
    by="Accuracy",
    ascending=False
)

print("\n==============================")
print("FINAL RESULTS")
print("==============================")

print(results_df)

print("\n==============================")
print("BEST MODEL")
print("==============================")

print("Model :", best_model_name)
print("Accuracy :", round(best_accuracy, 4))




# ==========================
# SAVE BEST MODEL
# ==========================

joblib.dump(best_model, "model.pkl")

joblib.dump(
    crop_encoder,
    "label_encoder.pkl"
)

joblib.dump(
    soil_encoder,
    "soil_encoder.pkl"
)

print("\nModel Saved Successfully!")
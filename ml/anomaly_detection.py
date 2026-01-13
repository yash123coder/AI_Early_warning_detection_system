import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

MODEL_PATH = "models/saved_models/isolation_forest.pkl"

def train_anomaly_model():
    df = pd.read_csv("data/raw/business_data.csv")

    features = df.drop(columns=["failed"])

    model = IsolationForest(
        n_estimators=200,
        contamination=0.1,
        random_state=42
    )

    model.fit(features)

    os.makedirs("models/saved_models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print("Anomaly Detection model trained & saved")

if __name__ == "__main__":
    train_anomaly_model()

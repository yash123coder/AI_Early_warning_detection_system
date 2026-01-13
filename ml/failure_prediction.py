import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

MODEL_PATH = "models/saved_models/failure_model.pkl"

def train_failure_model():
    df = pd.read_csv("data/raw/business_data.csv")

    X = df.drop(columns=["failed"])
    y = df["failed"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = xgb.XGBClassifier(
        n_estimators=200,
        max_depth=5,
        learning_rate=0.05,
        eval_metric="logloss"
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print(classification_report(y_test, preds))

    os.makedirs("models/saved_models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print("Failure Prediction model trained & saved")

if __name__ == "__main__":
    train_failure_model()

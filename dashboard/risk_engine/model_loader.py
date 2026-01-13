# risk_engine/model_loader.py

import joblib

MODEL_PATH = "/home/ubuntu/Desktop/ai-early-warning-system/models/saved_models/failure_model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

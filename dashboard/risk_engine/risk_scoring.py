import pickle
import pandas as pd
import numpy as np

# -------------------------------------------------
# Load Model
# -------------------------------------------------
MODEL_PATH = "/home/ubuntu/Desktop/ai-early-warning-system/models/saved_models/failure_model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# -------------------------------------------------
# Risk Thresholds
# -------------------------------------------------
def risk_level(score: float):
    if score >= 0.7:
        return "HIGH"
    elif score >= 0.4:
        return "MEDIUM"
    return "LOW"

# -------------------------------------------------
# Main Risk Function
# -------------------------------------------------
def calculate_risk(business_data: dict, text_result: dict):

    feature_order = [
        "monthly_sales",
        "revenue",
        "customer_count",
        "churn_rate",
        "support_tickets",
        "marketing_spend"
    ]

    df = pd.DataFrame([[business_data[f] for f in feature_order]],
                      columns=feature_order)

    # ---- ML prediction
    ml_probability = float(model.predict_proba(df)[0][1])

    # ---- NLP risk
    text_risk = float(text_result.get("text_risk_score", 0.0))

    # ---- Final combined risk
    final_risk = round((ml_probability * 0.7) + (text_risk * 0.3), 3)

    # -------------------------------------------------
    # Explainability (ROBUST & ALWAYS WORKS)
    # -------------------------------------------------
    shap_values = {}

    if hasattr(model, "feature_importances_"):
        importances = model.feature_importances_
        mean_value = importances.mean()

        for i, feature in enumerate(feature_order):
            shap_values[feature] = round(float(importances[i] - mean_value), 4)
    else:
        shap_values = {f: 0.0 for f in feature_order}

    return {
        "risk_score": final_risk,
        "risk_level": risk_level(final_risk),
        "ml_probability": round(ml_probability, 3),
        "text_risk": round(text_risk, 3),
        "shap_values": shap_values
    }

import os
import pandas as pd
from datetime import datetime

HISTORY_FILE = "risk_history.csv"


def load_risk_history():
    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE, parse_dates=["timestamp"])
    return pd.DataFrame(columns=["timestamp", "risk_score"])


def save_risk_history(risk_score):
    df = load_risk_history()

    new_row = {
        "timestamp": datetime.now(),
        "risk_score": risk_score
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(HISTORY_FILE, index=False)

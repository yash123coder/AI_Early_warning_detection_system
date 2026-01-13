import os
import requests
from dotenv import load_dotenv

# -------------------------------------------------
# Load .env safely (works for Streamlit)
# -------------------------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ENV_PATH = os.path.join(BASE_DIR, ".env")

if os.path.exists(ENV_PATH):
    load_dotenv(ENV_PATH)
else:
    load_dotenv()  # fallback

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "meta-llama/llama-3-8b-instruct"

def ask_llama(question: str, context: dict) -> str:
    if not OPENROUTER_API_KEY:
        return "❌ OpenRouter API key not configured."

    system_prompt = f"""
You are a senior business consultant AI.

Business Context:
- Risk Level: {context.get("risk_level")}
- Profit: {context.get("profit")}
- Churn Rate: {context.get("churn")}
- Repeat Customers %: {context.get("repeat_pct")}
- Customer Sentiment: {context.get("sentiment")}

Give clear, practical, step-by-step advice.
"""

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        "temperature": 0.4,
        "max_tokens": 300
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=20)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        return f"⚠ AI service error: {str(e)}"

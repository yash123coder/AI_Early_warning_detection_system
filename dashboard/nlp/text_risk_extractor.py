from transformers import pipeline
import re

# -----------------------------
# Load Sentiment Model (CPU safe)
# -----------------------------
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# -----------------------------
# Topic Keywords
# -----------------------------
TOPIC_KEYWORDS = {
    "support": ["support", "response", "help", "service"],
    "quality": ["quality", "poor", "bad", "defect"],
    "price": ["price", "cost", "expensive", "cheap"],
    "delivery": ["delivery", "late", "delay", "shipping"],
    "refund": ["refund", "return", "money"]
}

# -----------------------------
# Extract Topics
# -----------------------------
def extract_topics(text: str):
    text = text.lower()
    topics = []

    for topic, keywords in TOPIC_KEYWORDS.items():
        for word in keywords:
            if re.search(rf"\b{word}\b", text):
                topics.append(topic)
                break

    return list(set(topics))



# -----------------------------
# Analyze Text
# -----------------------------
def analyze_text(text: str):
    if not text or not text.strip():
        return {
            "sentiment": "NEUTRAL",
            "confidence": 0.0,
            "text_risk_score": 0.0,
            "topics": []
        }

    sentiment = sentiment_pipeline(text)[0]
    topics = extract_topics(text)

    label = sentiment["label"].upper()
    score = sentiment["score"]

    text_risk_score = score if label == "NEGATIVE" else 0.0
    if len(topics) >= 2:
        text_risk_score += 0.2

    return {
        "sentiment": label,
        "confidence": round(score, 3),
        "text_risk_score": round(min(text_risk_score, 1.0), 3),
        "topics": topics
    }

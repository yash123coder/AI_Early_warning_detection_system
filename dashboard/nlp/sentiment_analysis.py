# from transformers import pipeline

# # Load once (heavy model)
# sentiment_pipeline = pipeline(
#     "sentiment-analysis",
#     model="distilbert-base-uncased-finetuned-sst-2-english"
# )

# def analyze_sentiment(text: str) -> dict:
#     result = sentiment_pipeline(text)[0]

#     label = result["label"]
#     confidence = result["score"]

#     # Convert sentiment to risk score
#     if label == "NEGATIVE":
#         risk = confidence
#     else:
#         risk = 1 - confidence

#     return {
#         "sentiment": label,
#         "confidence": round(confidence, 2),
#         "text_risk_score": round(risk, 2)
#     }


# if __name__ == "__main__":
#     test_text = "Support is very slow and service quality is bad"
#     print(analyze_sentiment(test_text))
# from transformers import pipeline

# # Load once (cached by HF)
# sentiment_pipeline = pipeline(
#     "sentiment-analysis",
#     model="distilbert-base-uncased-finetuned-sst-2-english"
# )

# def analyze_sentiment(text: str) -> dict:
#     """
#     Returns sentiment label and confidence score
#     """
#     if not text or len(text.strip()) == 0:
#         return {"label": "NEUTRAL", "score": 0.0}

#     result = sentiment_pipeline(text[:512])[0]

#     return {
#         "label": result["label"],   # POSITIVE / NEGATIVE
#         "score": round(result["score"] * 100, 2)
#     }
from transformers import pipeline

# Load once (important for Streamlit performance)
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text: str) -> dict:
    """
    Returns standardized sentiment output
    """

    if not text or len(text.strip()) == 0:
        return {
            "label": "NEUTRAL",
            "score": 0.0
        }

    result = sentiment_pipeline(text[:512])[0]

    label = result["label"].upper()
    score = round(result["score"] * 100, 2)

    return {
        "label": label,
        "score": score
    }

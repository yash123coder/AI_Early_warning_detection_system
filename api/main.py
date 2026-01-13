from fastapi import FastAPI
from api.routes.predict import router as predict_router
from dashboard.nlp.sentiment_analysis import analyze_sentiment
from dashboard.nlp.text_risk_extractor import analyze_text, extract_topics


app = FastAPI(
    title="AI Early Warning & Failure Prediction System",
    version="1.0.0"
)

# Include routes
app.include_router(predict_router)


@app.get("/health")
def health():
    return {"status": "OK"}

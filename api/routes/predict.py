from fastapi import APIRouter
from pydantic import BaseModel
from dashboard.risk_engine.risk_scoring import calculate_risk

router = APIRouter(
    prefix="/predict",
    tags=["Risk Prediction"]
)

# -----------------------------
# Request Schemas
# -----------------------------

class BusinessData(BaseModel):
    monthly_sales: int
    revenue: int
    customer_count: int
    churn_rate: float
    support_tickets: int
    marketing_spend: int


class RiskRequest(BaseModel):
    business_data: BusinessData
    feedback_text: str


# -----------------------------
# Risk Prediction Endpoint
# -----------------------------

@router.post("/risk")
def predict_risk(request: RiskRequest):
    """
    Predict early failure risk using ML + NLP
    """

    result = calculate_risk(
        business_data=request.business_data.dict(),
        feedback_text=request.feedback_text
    )

    return {
        "success": True,
        "data": result
    }

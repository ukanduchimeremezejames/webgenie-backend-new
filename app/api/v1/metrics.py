from fastapi import APIRouter
from app.services.metrics_engine import evaluate_predictions

router = APIRouter()

@router.get("/sample")
def sample():
    return evaluate_predictions([], [])

from fastapi import APIRouter, HTTPException
from app.models import EstimateRequest, EstimateResponse
from app.services.concrete import calculate_estimate

router = APIRouter()

@router.post("/", response_model=EstimateResponse, summary="Estimate concrete volume and mix guidance")
async def estimate_concrete(request: EstimateRequest):
    try:
        result = calculate_estimate(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

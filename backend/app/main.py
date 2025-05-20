from fastapi import FastAPI
from app.endpoints.estimate import router as estimate_router
from app.endpoints.weather import router as weather_router

app = FastAPI(
    title="Concrete Estimator API",
    version="0.1.0",
    description="API for calculating concrete volumes and mix recommendations for construction use."
)

app.include_router(estimate_router, prefix="/estimate", tags=["Estimate"])
app.include_router(weather_router, prefix="/weather", tags=["Weather"])

@app.get("/health", summary="Health Check")
async def health_check():
    return {"status": "ok"}

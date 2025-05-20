from fastapi import APIRouter, Depends
from app.dependencies import get_settings
import httpx

router = APIRouter()

@router.get("/current", summary="Fetch current weather by lat/lon")
async def get_current_weather(lat: float, lon: float, settings=Depends(get_settings)):
    """
    Returns basic weather data: temperature, humidity, rainfall.
    """
    api_key = settings.openweather_api_key
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&units=imperial&appid={api_key}"
    )
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()

    return {
        "temperature": data.get("main", {}).get("temp"),
        "humidity": data.get("main", {}).get("humidity"),
        "rain_last_1h": data.get("rain", {}).get("1h", 0)
    }

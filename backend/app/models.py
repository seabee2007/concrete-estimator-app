from pydantic import BaseModel, Field
from typing import Literal, Optional, List

class Dimension(BaseModel):
    length: float = Field(..., description="Length in feet")
    width: Optional[float] = Field(None, description="Width in feet (for rectangular shapes)")
    height: float = Field(..., description="Height or thickness in feet")
    diameter: Optional[float] = Field(None, description="Diameter in feet (for round shapes)")

class MixOptions(BaseModel):
    psi: int = Field(..., description="Compressive strength in PSI, e.g. 3000")
    air_entrained: bool = Field(..., description="Whether mix is air-entrained")
    placement: Literal['pump', 'chute'] = Field(..., description="Placement method")
    waste_factor: float = Field(0.05, description="Waste factor as decimal, default 5%")

class EnvironmentalConditions(BaseModel):
    ambient_temperature: float = Field(..., description="Ambient air temperature in °F")
    humidity: Optional[float] = Field(None, description="Relative humidity percentage")
    rain_last_24h: Optional[float] = Field(None, description="Rainfall in inches over last 24h")
    plant_distance_miles: Optional[float] = Field(None, description="Distance from batch plant in miles")

class EstimateRequest(BaseModel):
    shape: Literal['square_column', 'round_column', 'footer', 'slab', 'wall']
    dimensions: Dimension
    quantity: int = Field(1, description="Number of identical elements to estimate")
    mix: MixOptions
    conditions: EnvironmentalConditions

class EstimateResponse(BaseModel):
    volume_cubic_yards: float
    volume_including_waste: float
    admixture_recommendations: List[str]
    details: dict

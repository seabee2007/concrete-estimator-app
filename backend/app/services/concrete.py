import math
from app.models import EstimateRequest, EstimateResponse


def cubic_feet_to_cubic_yards(ft3: float) -> float:
    return ft3 / 27.0


def calculate_volume(request: EstimateRequest) -> float:
    dims = request.dimensions
    shape = request.shape
    if shape == 'square_column' or shape == 'footer' or shape == 'slab' or shape == 'wall':
        # width must be provided for rectangular shapes
        if dims.width is None:
            raise ValueError(f"Width is required for shape {shape}")
        ft3 = dims.length * dims.width * dims.height
    elif shape == 'round_column':
        if dims.diameter is None:
            raise ValueError("Diameter is required for round_column")
        radius = dims.diameter / 2.0
        area = math.pi * radius * radius
        ft3 = area * dims.height
    else:
        raise ValueError(f"Unsupported shape {shape}")
    return cubic_feet_to_cubic_yards(ft3) * request.quantity


def estimate_admixtures(request: EstimateRequest) -> list:
    recs = []
    temp = request.conditions.ambient_temperature
    placement = request.mix.placement
    if temp >= 85:
        recs.append("Add retarder for hot weather to delay set.")
    elif temp <= 40:
        recs.append("Add accelerator for cold weather to speed strength gain.")
    if placement == 'pump':
        recs.append("Use high-range water reducer for pumpability.")
    if request.mix.air_entrained:
        recs.append("Ensure 4-6% air entrainment for freeze-thaw durability.")
    # Distance logic
    dist = request.conditions.plant_distance_miles
    if dist and dist > 50:
        recs.append("Use hydration stabilizer for long haul times.")
    return recs


def calculate_estimate(request: EstimateRequest) -> EstimateResponse:
    # 1. Compute base volume
    base_vol = calculate_volume(request)
    # 2. Add waste factor
    waste_vol = base_vol * (1 + request.mix.waste_factor)
    # 3. Admixture recommendations
    admixtures = estimate_admixtures(request)
    # 4. Details for transparency
    details = {
        "base_volume_yd3": round(base_vol, 3),
        "waste_factor": request.mix.waste_factor,
        "volume_with_waste_yd3": round(waste_vol, 3)
    }
    return EstimateResponse(
        volume_cubic_yards=round(base_vol, 3),
        volume_including_waste=round(waste_vol, 3),
        admixture_recommendations=admixtures,
        details=details
    )

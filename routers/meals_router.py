from fastapi import APIRouter, HTTPException

from schemas.meals import MealsRequest
from services.meals import get_meals

router = APIRouter(prefix="/v1/meals", tags=["meals"])


@router.post("")
def post_meals(payload: MealsRequest):
    data = get_meals(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to retrieve meals from Eurostar upstream.",
        )

    
    
    if isinstance(data, list):
        return {"data": {"meals": data}}

    return data
from fastapi import APIRouter, HTTPException

from schemas.update_meals import UpdateMealsRequest
from services.update_meals import update_meals

router = APIRouter(prefix="/v1/update-meals", tags=["update-meals"])


@router.post("")
def post_update_meals(payload: UpdateMealsRequest):
    data = update_meals(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to update meals at Eurostar upstream.",
        )

    return data
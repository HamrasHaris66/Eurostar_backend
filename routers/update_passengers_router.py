from fastapi import APIRouter, HTTPException

from schemas.update_passengers import (
    UpdatePassengersRequest,
    UpdatePassengersResponse,
)
from services.update_passengers import update_passengers

router = APIRouter(prefix="/v1/update-passengers-and-confirm", tags=["update-passengers"])


@router.post("", response_model=UpdatePassengersResponse)
def post_update_passengers(payload: UpdatePassengersRequest):
    data = update_passengers(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to update passengers on booking at Eurostar upstream.",
        )

    return data
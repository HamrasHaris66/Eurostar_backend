from fastapi import APIRouter, HTTPException

from schemas.update_passenger_details import (
    UpdatePassengerDetailsRequest,
    UpdatePassengerDetailsResponse,
)
from services.update_passenger_details import update_passenger_details

router = APIRouter(
    prefix="/v1/update-passengers-details",
    tags=["update-passengers-details"],
)


@router.post("", response_model=UpdatePassengerDetailsResponse)
def post_update_passenger_details(payload: UpdatePassengerDetailsRequest):
    data = update_passenger_details(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to update passenger details at Eurostar upstream.",
        )

    return data
from fastapi import APIRouter, HTTPException

from schemas.booking import BookingRequest
from services.booking import get_booking

router = APIRouter(prefix="/v1/booking", tags=["booking"])


@router.post("", response_model=None)
def retrieve_booking(payload: BookingRequest):
    data = get_booking(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to retrieve booking from Eurostar upstream.",
        )

    return data
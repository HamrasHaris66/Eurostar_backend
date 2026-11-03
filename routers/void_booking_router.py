from fastapi import APIRouter, HTTPException

from schemas.void_booking import VoidBookingRequest
from services.void_booking import void_booking

router = APIRouter(prefix="/v1/void-booking", tags=["void-booking"])


@router.post("", response_model=None)
def post_void_booking(payload: VoidBookingRequest):
    data = void_booking(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to void booking at Eurostar upstream.",
        )

    return data
from fastapi import APIRouter, HTTPException

from schemas.confirm_booking import ConfirmBookingRequest
from services.confirm_booking import confirm_booking

router = APIRouter(prefix="/v1/confirm-booking", tags=["confirm-booking"])


@router.post("", response_model=None)
def post_confirm_booking(payload: ConfirmBookingRequest):
    data = confirm_booking(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to confirm booking at Eurostar upstream.",
        )

    return data
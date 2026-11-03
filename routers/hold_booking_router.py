from fastapi import APIRouter, HTTPException

from schemas.hold_booking import HoldBookingRequest, HoldBookingResponse
from services.hold_booking import hold_booking

router = APIRouter(prefix="/v1/hold-booking", tags=["hold-booking"])


@router.post("", response_model=HoldBookingResponse)
def post_hold_booking(payload: HoldBookingRequest):
    data = hold_booking(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to place booking on hold at Eurostar upstream.",
        )

    return data
from fastapi import APIRouter, HTTPException

from schemas.cancel_booking_items import CancelBookingItemsRequest
from services.cancel_booking_items import cancel_booking_items

router = APIRouter(prefix="/v1/cancel-booking-items", tags=["cancel-booking-items"])


@router.post("", response_model=None)
def post_cancel_booking_items(payload: CancelBookingItemsRequest):
    data = cancel_booking_items(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to cancel booking items at Eurostar upstream.",
        )

    return data
from fastapi import APIRouter, HTTPException

from schemas.confirm_cancel_booking import ConfirmCancelBookingRequest
from services.confirm_cancel_booking import confirm_cancel_booking

router = APIRouter(prefix="/v1/confirm-cancel-booking", tags=["confirm-cancel-booking"])


@router.post("", response_model=None)
def post_confirm_cancel_booking(payload: ConfirmCancelBookingRequest):
    data = confirm_cancel_booking(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to confirm cancellation at Eurostar upstream.",
        )

    return data
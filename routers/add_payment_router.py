from fastapi import APIRouter, HTTPException

from schemas.add_payment import AddPaymentRequest, AddPaymentResponse
from services.add_payment import add_payment

router = APIRouter(prefix="/v1/add-payment", tags=["add-payment"])


@router.post("", response_model=AddPaymentResponse)
def post_add_payment(payload: AddPaymentRequest):
    data = add_payment(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to add payment to booking at Eurostar upstream.",
        )

    return data
from fastapi import APIRouter, HTTPException

from schemas.update_voucher import UpdateVoucherRequest
from schemas.vouchers import Voucher
from services.update_voucher import update_voucher

router = APIRouter(prefix="/v1/vouchers", tags=["vouchers"])


@router.patch("", response_model=Voucher)
def update_existing_voucher(payload: UpdateVoucherRequest):
    """
    Update an existing voucher (activation, recipient email, sales period,
    or external reference dates). Returns the updated voucher state.
    """
    data = update_voucher(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to update voucher at Eurostar upstream.",
        )

    return data
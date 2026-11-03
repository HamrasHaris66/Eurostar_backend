from fastapi import APIRouter, HTTPException

from schemas.create_voucher import CreateVoucherRequest, CreateVoucherResponse
from schemas.vouchers import Voucher
from services.vouchers import create_voucher, get_voucher

router = APIRouter(prefix="/v1/vouchers", tags=["vouchers"])


@router.post("", response_model=CreateVoucherResponse)
def create_new_voucher(payload: CreateVoucherRequest):
    data = create_voucher(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to create voucher at Eurostar upstream.",
        )

    return data


@router.get("/{voucher_code}", response_model=Voucher)
def retrieve_voucher(voucher_code: str):
    data = get_voucher(voucher_code)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to retrieve voucher from Eurostar upstream.",
        )

    return data
from fastapi import APIRouter, HTTPException

from schemas.create_booking import CreateBookingRequest, CreateBookingResponse
from services.create_booking import create_booking

router = APIRouter(prefix="/v1/create-booking", tags=["create-booking"])


@router.post("", response_model=CreateBookingResponse)
def post_create_booking(payload: CreateBookingRequest):
    data = create_booking(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to create booking on Eurostar upstream.",
        )

    return data
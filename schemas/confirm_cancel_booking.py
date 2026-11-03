from pydantic import BaseModel, Field


class ConfirmCancelBookingRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)
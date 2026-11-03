from pydantic import BaseModel, Field


class HoldBookingRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)


class HoldBookingResponse(BaseModel):
    reference: str
    expiryTimestamp: str
from pydantic import BaseModel, Field


class VoidBookingRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)
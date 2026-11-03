from typing import Optional

from pydantic import BaseModel, Field


class ConfirmBookingRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)


class ConfirmBookingResponse(BaseModel):
    reference: str
    status: Optional[str] = None
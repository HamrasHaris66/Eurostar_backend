from pydantic import BaseModel, Field


class BookingRequest(BaseModel):
    reference: str = Field(..., min_length=1)
    lastName: str = Field(
        ...,
        min_length=1,
        description="Any traveller (passenger) name within the booking",
    )
from pydantic import BaseModel, Field


class RevertChangesRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)
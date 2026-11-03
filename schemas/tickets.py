from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class TicketLanguage(str, Enum):
    en = "en"
    fr = "fr"
    nl = "nl"
    de = "de"


class TicketsRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)
    lastName: str = Field(
        ...,
        min_length=1,
        description="Any passenger lastName within the booking",
    )
    language: Optional[TicketLanguage] = Field(
        None,
        description="Ticket document language. Defaults to English.",
    )
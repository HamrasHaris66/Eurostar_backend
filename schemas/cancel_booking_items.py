from typing import List, Optional

from pydantic import BaseModel, Field


class CancelBookingItemsRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)
    itemRefs: Optional[List[str]] = Field(
        None,
        description=(
            "Specific item refs to cancel. Omit to cancel ALL active items."
        ),
    )
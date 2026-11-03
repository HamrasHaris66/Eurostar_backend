from typing import List

from pydantic import BaseModel, Field


class MealsRequest(BaseModel):
    reference: str = Field(..., min_length=1, description="Booking reference")
    segmentId: str = Field(
        ...,
        min_length=1,
        description='Segment ID, e.g. "segment_1"',
    )


class Meal(BaseModel):
    code: str
    name: str
    available: bool


class MealsData(BaseModel):
    meals: List[Meal]


class MealsResponse(BaseModel):
    data: MealsData
from typing import List, Optional

from pydantic import BaseModel, Field


class MealSelection(BaseModel):
    mealCode: str = Field(..., description='e.g. "MOML", "VGML", "CHML"')
    passengerId: str = Field(..., description="e.g. passenger_1")


class UpdateMealsRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)
    outbound: Optional[List[MealSelection]] = None
    inbound: Optional[List[MealSelection]] = None


class MealPassengerRef(BaseModel):
    id: str


class MealAssignment(BaseModel):
    code: str
    name: str
    passenger: MealPassengerRef


class MealSegment(BaseModel):
    meals: List[MealAssignment]


class UpdateMealsData(BaseModel):
    reference: str
    outbound: Optional[List[MealSegment]] = None
    inbound: Optional[List[MealSegment]] = None


class UpdateMealsEnvelope(BaseModel):
    updateMeals: UpdateMealsData


class UpdateMealsResponse(BaseModel):
    data: UpdateMealsEnvelope
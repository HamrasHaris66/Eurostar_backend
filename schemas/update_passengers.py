import re
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator

_NAME_PATTERN = re.compile(r"^[-'A-Za-zÀ-ÿ]*$")



class DiscountCard(BaseModel):
    code: Optional[str] = None
    identifier: Optional[str] = None
    name: Optional[str] = None
    requiresPassengerIdentifier: Optional[bool] = None


class UnformattedPhoneNumber(BaseModel):
    countryCode: str
    number: str


class Infant(BaseModel):
    firstName: str
    lastName: str

    @field_validator("firstName", "lastName")
    @classmethod
    def _check_name(cls, v: str) -> str:
        if not _NAME_PATTERN.match(v):
            raise ValueError(
                "Name may only contain letters, hyphens, apostrophes, and spaces"
            )
        return v


class PassengerDetail(BaseModel):
    id: Optional[str] = None
    type: str = Field(..., description='"AD", "CH", "SN", "YT" etc.')
    disabilityType: Optional[str] = None
    firstName: str
    lastName: str
    birthDate: Optional[str] = Field(None, description="YYYY-MM-DD")
    email: Optional[str] = None
    phoneNumber: Optional[str] = None          
    unformattedPhoneNumber: Optional[UnformattedPhoneNumber] = None
    discountCards: Optional[List[DiscountCard]] = None
    infant: Optional[Infant] = None

    

    @field_validator("firstName", "lastName")
    @classmethod
    def _check_name(cls, v: str) -> str:
        if not _NAME_PATTERN.match(v):
            raise ValueError(
                "Name may only contain letters, hyphens, apostrophes, and spaces"
            )
        return v

    @field_validator("discountCards", mode="before")
    @classmethod
    def _normalize_discount_cards(cls, v):
        
        if v is None:
            return []
        if isinstance(v, dict):
            return [v]
        return v

    @field_validator("email")
    @classmethod
    def _check_email(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        if "@" not in v or "." not in v.split("@")[-1]:
            raise ValueError("email must be a valid email address")
        if any(c.isspace() for c in v):
            raise ValueError("email must not contain whitespace")
        return v


class UpdatePassengersRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)
    passengers: List[PassengerDetail] = Field(..., min_length=1)



class ResponsePassengerItem(BaseModel):
    id: str
    type: str
    firstName: str
    lastName: str


class UpdatePassengersData(BaseModel):
    reference: str
    passengers: List[ResponsePassengerItem]


class UpdatePassengersEnvelope(BaseModel):
    updatePassengersAndConfirm: UpdatePassengersData


class UpdatePassengersResponse(BaseModel):
    """
    Eurostar returns two shapes:
      - 1-passenger:  {"reference": ..., "passengers": [...]}
      - 2+ passengers: {"data": {"updatePassengersAndConfirm": {"reference": ..., "passengers": [...]}}}
    Both are accepted here; `data` is optional.
    """
    reference: Optional[str] = None
    passengers: Optional[List[ResponsePassengerItem]] = None
    data: Optional[UpdatePassengersEnvelope] = None
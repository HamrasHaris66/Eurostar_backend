import re
from typing import Optional

from pydantic import BaseModel, Field, field_validator

# Eurostar rejects special characters and whitespace in names.
# Accepts letters, hyphens, apostrophes, spaces only.
_NAME_PATTERN = re.compile(r"^[-'A-Za-zÀ-ÿ]*$")


class Customer(BaseModel):
    firstName: Optional[str] = Field(None, max_length=50)
    lastName: Optional[str] = Field(None, max_length=50)
    email: str = Field(..., description="Customer email address")
    phoneNumber: Optional[str] = Field(
        None,
        min_length=7,
        max_length=16,
        description="7-16 characters, digits only recommended",
    )

    @field_validator("firstName", "lastName")
    @classmethod
    def _check_name(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        if not _NAME_PATTERN.match(v):
            raise ValueError(
                "Name may only contain letters, hyphens, apostrophes, and spaces"
            )
        return v

    @field_validator("email")
    @classmethod
    def _check_email(cls, v: str) -> str:
        # minimal shape check; pydantic EmailStr would need email-validator dep
        if "@" not in v or "." not in v.split("@")[-1]:
            raise ValueError("email must be a valid email address")
        if any(c.isspace() for c in v):
            raise ValueError("email must not contain whitespace")
        return v


class AddCustomerRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)
    customer: Customer


class AddCustomerResponse(BaseModel):
    reference: str
    customer: Customer
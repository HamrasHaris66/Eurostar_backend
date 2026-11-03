from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class VoucherLanguage(str, Enum):
    EN = "EN"
    FR = "FR"
    NL = "NL"
    DE = "DE"


class VoucherCurrency(str, Enum):
    GBP = "GBP"
    EUR = "EUR"
    USD = "USD"


class CreateVoucherRequest(BaseModel):
    amount: float = Field(..., gt=0, description="Monetary value, positive")
    title: Optional[str] = Field(None, description='e.g. "Mr", "Ms"')
    firstName: str = Field(..., min_length=1)
    lastName: str = Field(..., min_length=1)
    recipientEmail: str = Field(..., min_length=3)
    currency: VoucherCurrency
    language: VoucherLanguage


class CreateVoucherResponse(BaseModel):
    reference: str
    alias: str
    type: str
    amount: float
    currency: str
    validUntil: str
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class VoucherValueType(str, Enum):
    AMOUNT = "AMOUNT"
    PERCENTAGE = "PERCENTAGE"


class VoucherType(str, Enum):
    GEV = "GEV"


class VoucherStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    EXPIRED = "EXPIRED"
    REDEEMED = "REDEEMED"


class Voucher(BaseModel):
    reference: Optional[str] = None
    valueType: Optional[VoucherValueType] = None
    value: Optional[float] = None
    type: Optional[VoucherType] = None
    alias: Optional[str] = None
    validUntil: Optional[str] = None
    balance: Optional[float] = None
    isActive: Optional[bool] = None
    currency: Optional[str] = None
    customerEmail: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    status: Optional[VoucherStatus] = None
    travelDays: Optional[str] = Field(None, description="Comma-separated 0/1 per weekday")
    travelPeriodStart: Optional[str] = None
    travelPeriodEnd: Optional[str] = None
    salesPeriodStart: Optional[str] = None
    salesPeriodEnd: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    activatedAt: Optional[str] = None
    inactivatedAt: Optional[str] = None
    language: Optional[str] = None
    description: Optional[str] = None
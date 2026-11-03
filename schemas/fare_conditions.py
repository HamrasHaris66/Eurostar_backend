from typing import Dict, List

from pydantic import BaseModel


class FareConditionLanguage(BaseModel):
    lines: List[str] = []
    commercialName: str | None = None


class FareCondition(BaseModel):
    category: int
    showPrices: bool
    languages: Dict[str, FareConditionLanguage] = {}
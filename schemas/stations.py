from typing import List

from pydantic import BaseModel


class Station(BaseModel):
    uic: str
    shortCode: str
    name: str


class StationListResponse(BaseModel):
    stations: List[Station]
    count: int
from fastapi import APIRouter, HTTPException

from schemas.stations import Station, StationListResponse
from services.stations import fetch_stations

router = APIRouter(prefix="/v1/stations", tags=["stations"])


@router.get("", response_model=StationListResponse)
def get_stations():
    raw = fetch_stations()

    if not raw:
        raise HTTPException(
            status_code=502,
            detail="Failed to retrieve stations from Eurostar upstream.",
        )

    stations = [Station(**s) for s in raw]
    return StationListResponse(stations=stations, count=len(stations))
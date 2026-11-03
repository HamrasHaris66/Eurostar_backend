from fastapi import APIRouter, HTTPException

from services.fare_conditions import get_fare_conditions

router = APIRouter(prefix="/v1/fare-conditions", tags=["fare-conditions"])


@router.get("", response_model=None)
def list_fare_conditions():
    data = get_fare_conditions()

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to retrieve fare conditions from Eurostar upstream.",
        )

    return data
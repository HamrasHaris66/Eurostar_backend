from fastapi import APIRouter, HTTPException

from schemas.fare_conditions import FareCondition
from services.fare_condition_by_tariff import get_fare_condition_by_tariff

router = APIRouter(prefix="/v1/fare-conditions", tags=["fare-conditions"])


@router.get("/{tariff_code}", response_model=FareCondition)
def get_fare_condition(tariff_code: str):
    """
    Retrieve fare conditions for a specific tariff code.
    """
    data, error_kind = get_fare_condition_by_tariff(tariff_code)

    if error_kind == "not_found":
        raise HTTPException(
            status_code=404,
            detail=f"Tariff code '{tariff_code}' not found.",
        )

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to retrieve fare condition from Eurostar upstream.",
        )

    return data
from schemas.journey_search import JourneySearchRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def search_journeys(payload: JourneySearchRequest) -> dict | None:
    """
    Call Eurostar POST /journey-search.
    Returns the raw parsed dict on success, or None on upstream failure.

    Strips None fields so one-way searches don't send `"inboundDate": null`,
    which Eurostar's validator rejects.
    """
    body = payload.model_dump()
    body = {k: v for k, v in body.items() if v is not None}

    try:
        data = eurostar_post("/journey-search", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data
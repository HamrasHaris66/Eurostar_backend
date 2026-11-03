from schemas.ready_to_travel import ReadyToTravelRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def ready_to_travel(payload: ReadyToTravelRequest) -> dict | list | None:
    body = payload.model_dump()

    try:
        data = eurostar_post("/ready-to-travel", payload=body)
    except EurostarHTTPError:
        return None

    if isinstance(data, (dict, list)):
        return data

    return None
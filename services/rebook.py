from schemas.rebook import RebookRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def rebook(payload: RebookRequest) -> dict | None:
    body = payload.model_dump()

    try:
        data = eurostar_post("/rebook", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data
from schemas.revert_changes import RevertChangesRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def revert_changes(payload: RevertChangesRequest) -> dict | None:
    body = payload.model_dump()

    try:
        data = eurostar_post("/revert-change", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data
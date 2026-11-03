from schemas.update_passengers import UpdatePassengersRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def update_passengers(payload: UpdatePassengersRequest) -> dict | None:
    body = payload.model_dump()

    # Eurostar's validator rejects null and empty values for these optional
    # fields, but accepts the field being omitted entirely.
    for p in body.get("passengers", []):
        for key in list(p.keys()):
            if key in ("id", "type", "firstName", "lastName"):
                continue  
            if p[key] is None or p[key] == "" or p[key] == []:
                p.pop(key, None)

    try:
        data = eurostar_post("/update-passengers-and-confirm", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data
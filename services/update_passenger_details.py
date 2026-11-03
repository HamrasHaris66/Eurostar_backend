from schemas.update_passenger_details import UpdatePassengerDetailsRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def update_passenger_details(payload: UpdatePassengerDetailsRequest) -> dict | None:
    body = payload.model_dump()

    for p in body.get("passengers", []):
        if p.get("infant") is None:
            p.pop("infant", None)
        for key in list(p.keys()):
            if p[key] is None or p[key] == "":
                p.pop(key, None)

    try:
        data = eurostar_post("/update-passengers-details", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data
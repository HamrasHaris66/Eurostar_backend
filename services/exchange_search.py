from schemas.exchange_search import ExchangeSearchRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def exchange_search(payload: ExchangeSearchRequest) -> dict | None:
    body = payload.model_dump()

    
    for key in list(body.keys()):
        value = body[key]
        if value is None or value == "":
            body.pop(key, None)

    try:
        data = eurostar_post("/exchange-search", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data
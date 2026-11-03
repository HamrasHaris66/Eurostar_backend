from schemas.meals import MealsRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def get_meals(payload: MealsRequest) -> dict | list | None:
    body = payload.model_dump()

    try:
        data = eurostar_post("/meals", payload=body)
    except EurostarHTTPError:
        return None

    if isinstance(data, (dict, list)):
        return data

    return None
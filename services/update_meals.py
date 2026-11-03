from schemas.update_meals import UpdateMealsRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def update_meals(payload: UpdateMealsRequest) -> dict | None:
    body = payload.model_dump()

    
    for key in list(body.keys()):
        value = body[key]
        if value is None or value == []:
            body.pop(key, None)

    try:
        data = eurostar_post("/update-meals", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data
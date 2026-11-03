from schemas.submit_travel_documents import SubmitTravelDocumentsRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def submit_travel_documents(payload: SubmitTravelDocumentsRequest) -> bool:
    body = payload.model_dump()

    try:
        eurostar_post("/submit-travel-docs", payload=body)
    except EurostarHTTPError:
        return False

    return True
from fastapi import APIRouter, HTTPException

from schemas.revert_changes import RevertChangesRequest
from services.revert_changes import revert_changes

router = APIRouter(prefix="/v1/revert-change", tags=["revert-change"])


@router.post("", response_model=None)
def post_revert_changes(payload: RevertChangesRequest):
    data = revert_changes(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to revert changes at Eurostar upstream.",
        )

    return data
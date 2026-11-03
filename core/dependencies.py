from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

from core.config import get_settings

api_key_header = APIKeyHeader(
    name="X-API-Key",
    scheme_name="X-API-Key",
    description="Include a valid API key in the X-API-Key header.",
    auto_error=False,
)


async def verify_api_key(api_key: str = Security(api_key_header)) -> str:
    settings = get_settings()
    valid_keys = [k.strip() for k in settings.API_KEYS.split(",") if k.strip()]
    if not api_key or api_key not in valid_keys:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing X-API-Key header.",
        )
    return api_key
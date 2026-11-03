import json
import re
from datetime import datetime
from pathlib import Path

import requests

from core.config import (
    APP_ROOT,
    EUROSTAR_MARKET,
    EUROSTAR_USER_AGENT,
    get_settings,
)


_ILLEGAL_FS_CHARS = re.compile(r'[<>:"/\\|?*]')


class EurostarHTTPError(Exception):
    def __init__(self, status_code: int, body, url: str):
        self.status_code = status_code
        self.body = body
        self.url = url
        super().__init__(f"Eurostar {status_code} on {url}")


def _sanitize_dirname(name: str) -> str:
    """Make a string safe to use as a directory name on Windows."""
    cleaned = _ILLEGAL_FS_CHARS.sub("_", name)
    cleaned = cleaned.strip().strip(".")
    return cleaned or "root"


def _log_call(endpoint: str, method: str, payload, response_data) -> None:
    raw_name = endpoint.replace("\\", "/").split("/")[-1].split(".")[0] or "root"
    api_name = _sanitize_dirname(raw_name)

    date_str = datetime.now().strftime("%Y-%m-%d")

    log_dir = APP_ROOT / "logs" / api_name / date_str / method.lower()
    log_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")

    (log_dir / f"{timestamp}_req.json").write_text(
        json.dumps(payload, indent=2, default=str), encoding="utf-8"
    )
    (log_dir / f"{timestamp}_res.json").write_text(
        json.dumps(response_data, indent=2, default=str), encoding="utf-8"
    )


def _build_url(endpoint: str) -> str:
    settings = get_settings()
    if endpoint.startswith("http"):
        return endpoint
    return f"{settings.base_url.rstrip('/')}/{endpoint.lstrip('/')}"


def _build_headers(extra: dict | None = None) -> dict:
    settings = get_settings()
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip",
        "x-api-key": settings.x_api_key,
        "x-market": EUROSTAR_MARKET,
        "user-agent": EUROSTAR_USER_AGENT,
    }
    if extra:
        headers.update(extra)
    return headers


def _normalize_payload(payload):
    if payload is None:
        return None
    if hasattr(payload, "model_dump"):
        return payload.model_dump()
    if hasattr(payload, "dict"):
        return payload.dict()
    return payload


def _parse_body(response: requests.Response):
    try:
        return response.json()
    except Exception:
        return response.text


def _request(method: str, endpoint: str, payload=None, params=None, headers=None):
    settings = get_settings()
    url = _build_url(endpoint)
    merged_headers = _build_headers(headers)
    body = _normalize_payload(payload)

    response = requests.request(
        method=method.upper(),
        url=url,
        json=body,
        params=params,
        headers=merged_headers,
        timeout=30,
    )

    data = _parse_body(response)

    _log_call(
        endpoint=endpoint,
        method=method,
        payload={
            "url": url,
            "method": method.upper(),
            "params": params,
            "body": body,
            "env": settings.ACTIVE_ENV,
        },
        response_data={"http_status": response.status_code, "body": data},
    )

    if not response.ok:
        raise EurostarHTTPError(response.status_code, data, url)

    return data


def eurostar_get(endpoint: str, params: dict | None = None, headers: dict | None = None):
    return _request("GET", endpoint, params=params, headers=headers)


def eurostar_post(endpoint: str, payload=None, params: dict | None = None, headers: dict | None = None):
    return _request("POST", endpoint, payload=payload, params=params, headers=headers)


def eurostar_put(endpoint: str, payload=None, params: dict | None = None, headers: dict | None = None):
    return _request("PUT", endpoint, payload=payload, params=params, headers=headers)


def eurostar_patch(endpoint: str, payload=None, params: dict | None = None, headers: dict | None = None):
    return _request("PATCH", endpoint, payload=payload, params=params, headers=headers)


def eurostar_delete(endpoint: str, params: dict | None = None, headers: dict | None = None):
    return _request("DELETE", endpoint, params=params, headers=headers)
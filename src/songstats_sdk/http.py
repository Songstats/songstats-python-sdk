from __future__ import annotations

import time
from typing import Any, Mapping

import httpx

from .exceptions import SongstatsAPIError, SongstatsTransportError
from .version import VERSION

DEFAULT_BASE_URL = "https://data.songstats.com"
DEFAULT_TIMEOUT_SECONDS = 30.0
RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}


class SongstatsHTTPClient:
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        max_retries: int = 2,
        user_agent: str | None = None,
        httpx_client: httpx.Client | None = None,
    ) -> None:
        if not api_key:
            raise ValueError("api_key is required")
        if max_retries < 0:
            raise ValueError("max_retries must be >= 0")

        self.base_url = base_url.rstrip("/")
        self.max_retries = max_retries
        self._owns_client = httpx_client is None
        self._client = httpx_client or httpx.Client(
            base_url=self.base_url,
            timeout=timeout,
            headers={
                "apikey": api_key,
                "accept": "application/json",
                "user-agent": user_agent or f"songstats-python-sdk/{VERSION}",
            },
        )

    def close(self) -> None:
        if self._owns_client:
            self._client.close()

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Mapping[str, Any] | None = None,
    ) -> Any:
        endpoint = f"/enterprise/v1/{path.lstrip('/')}"
        last_transport_error: Exception | None = None

        for attempt in range(self.max_retries + 1):
            try:
                response = self._client.request(method=method, url=endpoint, params=params, json=json)
            except httpx.RequestError as exc:
                last_transport_error = exc
                if attempt < self.max_retries:
                    time.sleep(0.2 * (2**attempt))
                    continue
                raise SongstatsTransportError(str(exc)) from exc

            if response.status_code in RETRYABLE_STATUS_CODES and attempt < self.max_retries:
                time.sleep(0.2 * (2**attempt))
                continue

            if response.is_success:
                return _decode_json_response(response)

            raise _build_api_error(response)

        if last_transport_error is not None:
            raise SongstatsTransportError(str(last_transport_error)) from last_transport_error

        raise SongstatsTransportError("Request failed without response")


def _decode_json_response(response: httpx.Response) -> Any:
    if not response.text:
        return None
    try:
        return response.json()
    except ValueError:
        return {"raw": response.text}


def _build_api_error(response: httpx.Response) -> SongstatsAPIError:
    payload: Any
    message = response.reason_phrase

    try:
        payload = response.json()
    except ValueError:
        payload = {"raw": response.text}
    else:
        if isinstance(payload, dict):
            message = str(payload.get("message") or payload.get("error") or message)

    return SongstatsAPIError(message=message, status_code=response.status_code, payload=payload)

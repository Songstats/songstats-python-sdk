from __future__ import annotations

from typing import Any, Iterable, Mapping

from ..http import SongstatsHTTPClient


class ResourceAPI:
    def __init__(self, http_client: SongstatsHTTPClient) -> None:
        self._http = http_client

    def _get(self, path: str, *, params: Mapping[str, Any] | None = None) -> Any:
        return self._http.request("GET", path, params=_normalize_params(params))

    def _post(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Mapping[str, Any] | None = None,
    ) -> Any:
        clean_params = _normalize_params(params)
        clean_json = _normalize_params(json)
        return self._http.request("POST", path, params=clean_params, json=clean_json)

    def _delete(self, path: str, *, params: Mapping[str, Any] | None = None) -> Any:
        return self._http.request("DELETE", path, params=_normalize_params(params))


def _normalize_params(params: Mapping[str, Any] | None) -> dict[str, Any] | None:
    if not params:
        return None

    normalized: dict[str, Any] = {}
    for key, value in params.items():
        if value is None:
            continue
        if isinstance(value, bool):
            normalized[key] = "true" if value else "false"
            continue
        if isinstance(value, (list, tuple, set)):
            normalized[key] = ",".join(str(item) for item in value)
            continue
        normalized[key] = value

    return normalized or None


def require_any_identifier(params: Mapping[str, Any], identifier_keys: Iterable[str]) -> None:
    if any(params.get(key) not in (None, "") for key in identifier_keys):
        return
    joined = ", ".join(identifier_keys)
    raise ValueError(f"One identifier is required. Supported keys: {joined}")

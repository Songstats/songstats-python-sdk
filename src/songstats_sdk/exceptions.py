from __future__ import annotations

from typing import Any


class SongstatsError(Exception):
    """Base exception for SDK failures."""


class SongstatsTransportError(SongstatsError):
    """Raised for network/transport failures before an HTTP response is received."""


class SongstatsAPIError(SongstatsError):
    """Raised when the Songstats API responds with a non-2xx status code."""

    def __init__(self, message: str, status_code: int, payload: Any = None) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def __str__(self) -> str:
        return f"Songstats API error ({self.status_code}): {self.message}"

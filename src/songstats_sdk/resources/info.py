from __future__ import annotations

from typing import Any

from .base import ResourceAPI


class InfoAPI(ResourceAPI):
    def sources(self) -> Any:
        return self._get("sources")

    def status(self) -> Any:
        return self._get("status")

    def uptime_check(self) -> Any:
        return self._get("uptime_check")

    def definitions(self) -> Any:
        return self._get("definitions")

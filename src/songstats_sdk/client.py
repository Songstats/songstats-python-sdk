from __future__ import annotations

import httpx

from .http import SongstatsHTTPClient
from .resources import (
    ArtistsAPI,
    CollaboratorsAPI,
    InfoAPI,
    LabelsAPI,
    TracksAPI,
)


class SongstatsClient:
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = "https://data.songstats.com",
        timeout: float = 30.0,
        max_retries: int = 2,
        user_agent: str | None = None,
        httpx_client: httpx.Client | None = None,
    ) -> None:
        self._http = SongstatsHTTPClient(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            user_agent=user_agent,
            httpx_client=httpx_client,
        )

        self.info = InfoAPI(self._http)
        self.tracks = TracksAPI(self._http)
        self.artists = ArtistsAPI(self._http)
        self.collaborators = CollaboratorsAPI(self._http)
        self.labels = LabelsAPI(self._http)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "SongstatsClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

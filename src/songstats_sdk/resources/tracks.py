from __future__ import annotations

from typing import Any

from .base import ResourceAPI, require_any_identifier

_TRACK_IDENTIFIER_KEYS = (
    "songstats_track_id",
    "spotify_track_id",
    "apple_music_track_id",
    "isrc",
)


class TracksAPI(ResourceAPI):
    def info(self, **params: Any) -> Any:
        query = _require_track_identifier(params)
        return self._get("tracks/info", params=query)

    def stats(self, **params: Any) -> Any:
        query = _require_track_identifier(params)
        return self._get("tracks/stats", params=query)

    def historic_stats(self, **params: Any) -> Any:
        query = _require_track_identifier(params)
        return self._get("tracks/historic_stats", params=query)

    def activities(self, **params: Any) -> Any:
        query = _require_track_identifier(params)
        return self._get("tracks/activities", params=query)

    def comments(self, **params: Any) -> Any:
        query = _require_track_identifier(params)
        return self._get("tracks/comments", params=query)

    def songshare(self, **params: Any) -> Any:
        query = _require_track_identifier(params)
        return self._get("tracks/songshare", params=query)

    def locations(self, **params: Any) -> Any:
        query = _require_track_identifier(params)
        return self._get("tracks/locations", params=query)

    def search(self, *, q: str, **params: Any) -> Any:
        if not q:
            raise ValueError("q is required")

        query = {"q": q}
        query.update(params)
        return self._get("tracks/search", params=query)

    def add_link_request(self, *, link: str, **params: Any) -> Any:
        if not link:
            raise ValueError("link is required")

        query = _require_track_identifier(params)
        query["link"] = link
        return self._post("tracks/link_request", params=query)

    def remove_link_request(self, *, link: str, **params: Any) -> Any:
        if not link:
            raise ValueError("link is required")

        query = _require_track_identifier(params)
        query["link"] = link
        return self._delete("tracks/link_request", params=query)

    def add_to_member_relevant_list(self, **params: Any) -> Any:
        query = _require_track_identifier(params)
        return self._post("tracks/add_to_member_relevant_list", params=query)

    def remove_from_member_relevant_list(self, **params: Any) -> Any:
        query = _require_track_identifier(params)
        return self._delete("tracks/remove_from_member_relevant_list", params=query)


def _require_track_identifier(params: dict[str, Any]) -> dict[str, Any]:
    query = dict(params)
    require_any_identifier(query, _TRACK_IDENTIFIER_KEYS)
    return query

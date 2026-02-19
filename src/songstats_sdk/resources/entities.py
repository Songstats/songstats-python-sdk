from __future__ import annotations

from typing import Any

from .base import ResourceAPI, require_any_identifier


class EntityAPI(ResourceAPI):
    def __init__(self, http_client, *, resource: str, identifier_keys: tuple[str, ...]) -> None:
        super().__init__(http_client)
        self._resource = resource
        self._identifier_keys = identifier_keys

    def info(self, **params: Any) -> Any:
        return self._get(f"{self._resource}/info", params=self._with_identifier(params))

    def stats(self, **params: Any) -> Any:
        return self._get(f"{self._resource}/stats", params=self._with_identifier(params))

    def historic_stats(self, **params: Any) -> Any:
        return self._get(f"{self._resource}/historic_stats", params=self._with_identifier(params))

    def audience(self, **params: Any) -> Any:
        return self._get(f"{self._resource}/audience", params=self._with_identifier(params))

    def audience_details(self, *, country_code: str, **params: Any) -> Any:
        if not country_code:
            raise ValueError("country_code is required")

        query = self._with_identifier(params)
        query["country_code"] = country_code
        return self._get(f"{self._resource}/audience/details", params=query)

    def catalog(self, **params: Any) -> Any:
        return self._get(f"{self._resource}/catalog", params=self._with_identifier(params))

    def search(self, *, q: str, **params: Any) -> Any:
        if not q:
            raise ValueError("q is required")

        query = {"q": q}
        query.update(params)
        return self._get(f"{self._resource}/search", params=query)

    def activities(self, **params: Any) -> Any:
        return self._get(f"{self._resource}/activities", params=self._with_identifier(params))

    def songshare(self, **params: Any) -> Any:
        return self._get(f"{self._resource}/songshare", params=self._with_identifier(params))

    def top_tracks(self, **params: Any) -> Any:
        return self._get(f"{self._resource}/top_tracks", params=self._with_identifier(params))

    def top_playlists(self, **params: Any) -> Any:
        return self._get(f"{self._resource}/top_playlists", params=self._with_identifier(params))

    def top_curators(self, **params: Any) -> Any:
        return self._get(f"{self._resource}/top_curators", params=self._with_identifier(params))

    def top_commentors(self, **params: Any) -> Any:
        return self._get(f"{self._resource}/top_commentors", params=self._with_identifier(params))

    def add_link_request(self, *, link: str, **params: Any) -> Any:
        if not link:
            raise ValueError("link is required")

        query = self._with_identifier(params)
        query["link"] = link
        return self._post(f"{self._resource}/link_request", params=query)

    def remove_link_request(self, *, link: str, **params: Any) -> Any:
        if not link:
            raise ValueError("link is required")

        query = self._with_identifier(params)
        query["link"] = link
        return self._delete(f"{self._resource}/link_request", params=query)

    def add_track_request(
        self,
        *,
        link: str | None = None,
        spotify_track_id: str | None = None,
        isrc: str | None = None,
        **params: Any,
    ) -> Any:
        if not any([link, spotify_track_id, isrc]):
            raise ValueError("One of link, spotify_track_id, or isrc is required")

        query = self._with_identifier(params)
        query.update({
            "link": link,
            "spotify_track_id": spotify_track_id,
            "isrc": isrc,
        })
        return self._post(f"{self._resource}/track_request", params=query)

    def remove_track_request(
        self,
        *,
        songstats_track_id: str | None = None,
        spotify_track_id: str | None = None,
        **params: Any,
    ) -> Any:
        if not songstats_track_id and not spotify_track_id:
            raise ValueError("songstats_track_id or spotify_track_id is required")

        query = self._with_identifier(params)
        query.update({
            "songstats_track_id": songstats_track_id,
            "spotify_track_id": spotify_track_id,
        })
        return self._delete(f"{self._resource}/track_request", params=query)

    def add_to_member_relevant_list(self, **params: Any) -> Any:
        return self._post(
            f"{self._resource}/add_to_member_relevant_list",
            params=self._with_identifier(params),
        )

    def remove_from_member_relevant_list(self, **params: Any) -> Any:
        return self._delete(
            f"{self._resource}/remove_from_member_relevant_list",
            params=self._with_identifier(params),
        )

    def _with_identifier(self, params: dict[str, Any]) -> dict[str, Any]:
        query = dict(params)
        require_any_identifier(query, self._identifier_keys)
        return query


class ArtistsAPI(EntityAPI):
    def __init__(self, http_client) -> None:
        super().__init__(
            http_client,
            resource="artists",
            identifier_keys=("songstats_artist_id", "spotify_artist_id", "apple_music_artist_id"),
        )


class CollaboratorsAPI(EntityAPI):
    def __init__(self, http_client) -> None:
        super().__init__(
            http_client,
            resource="collaborators",
            identifier_keys=(
                "songstats_collaborator_id",
                "spotify_artist_id",
                "apple_music_artist_id",
                "tidal_artist_id",
            ),
        )


class LabelsAPI(EntityAPI):
    def __init__(self, http_client) -> None:
        super().__init__(
            http_client,
            resource="labels",
            identifier_keys=("songstats_label_id", "beatport_label_id"),
        )

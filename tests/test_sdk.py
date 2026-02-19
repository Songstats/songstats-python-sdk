from __future__ import annotations

import httpx
import pytest
import respx

from songstats_sdk import SongstatsAPIError, SongstatsClient


@respx.mock
def test_info_status_sends_apikey_header() -> None:
    route = respx.get("https://data.songstats.com/enterprise/v1/status").mock(
        return_value=httpx.Response(200, json={"result": "success"})
    )

    client = SongstatsClient(api_key="test_key")
    data = client.info.status()

    assert data["result"] == "success"
    assert route.called
    assert route.calls.last.request.headers["apikey"] == "test_key"


@respx.mock
def test_info_sources_and_definitions_routes() -> None:
    sources = respx.get("https://data.songstats.com/enterprise/v1/sources").mock(
        return_value=httpx.Response(200, json={"result": "success", "sources": []})
    )
    definitions = respx.get("https://data.songstats.com/enterprise/v1/definitions").mock(
        return_value=httpx.Response(200, json={"result": "success", "definitions": {}})
    )

    client = SongstatsClient(api_key="test_key")
    client.info.sources()
    client.info.definitions()

    assert sources.called
    assert definitions.called


@respx.mock
def test_tracks_info_hits_expected_route_and_params() -> None:
    route = respx.get("https://data.songstats.com/enterprise/v1/tracks/info").mock(
        return_value=httpx.Response(200, json={"result": "success"})
    )

    client = SongstatsClient(api_key="test_key")
    client.tracks.info(songstats_track_id="abcd1234", with_links=True)

    request = route.calls.last.request
    assert request.url.params["songstats_track_id"] == "abcd1234"
    assert request.url.params["with_links"] == "true"


@respx.mock
def test_collaborators_top_curators_is_mapped() -> None:
    route = respx.get("https://data.songstats.com/enterprise/v1/collaborators/top_curators").mock(
        return_value=httpx.Response(200, json={"result": "success"})
    )

    client = SongstatsClient(api_key="test_key")
    client.collaborators.top_curators(songstats_collaborator_id="collab1234", source="spotify")

    request = route.calls.last.request
    assert request.url.params["songstats_collaborator_id"] == "collab1234"
    assert request.url.params["source"] == "spotify"


@respx.mock
def test_api_error_raises_songstats_api_error() -> None:
    respx.get("https://data.songstats.com/enterprise/v1/status").mock(
        return_value=httpx.Response(401, json={"result": "error", "message": "Invalid Api Key"})
    )

    client = SongstatsClient(api_key="bad_key")

    with pytest.raises(SongstatsAPIError) as exc:
        client.info.status()

    assert exc.value.status_code == 401
    assert "Invalid Api Key" in str(exc.value)


def test_identifier_validation() -> None:
    client = SongstatsClient(api_key="test_key")

    with pytest.raises(ValueError):
        client.labels.info()


@respx.mock
def test_artists_search_route() -> None:
    route = respx.get("https://data.songstats.com/enterprise/v1/artists/search").mock(
        return_value=httpx.Response(200, json={"result": "success", "results": []})
    )

    client = SongstatsClient(api_key="test_key")
    client.artists.search(q="fred again", limit=10)

    request = route.calls.last.request
    assert request.url.params["q"] == "fred again"
    assert request.url.params["limit"] == "10"

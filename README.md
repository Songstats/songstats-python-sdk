# Songstats Python SDK

Official Python client for the **Songstats Enterprise API**.

📚 API Documentation: https://developers.stats.company/songstats<br>
🔑 API Key Access: Please contact api@songstats.com

---

## Requirements

- Python >= 3.10

---

## Installation

Install from PyPI:

    pip install songstats-sdk

For local development:

    pip install -e ".[dev]"

---

## Quick Start

```python
from songstats_sdk import SongstatsClient

client = SongstatsClient(api_key="YOUR_API_KEY")

# API status
status = client.info.status()

# Track information
track = client.tracks.info(songstats_track_id="abcd1234")

# Artist statistics
artist_stats = client.artists.stats(
    songstats_artist_id="abcd1234",
    source="spotify",
)
```

---

## Authentication

All requests include your API key in the `apikey` header. The SDK applies its
`base_url`, `timeout`, `api_key`, and `user_agent` settings to each request, including
when you supply an `httpx_client`. Other client settings remain available, and
closing the SDK does not close a client you supplied. Redirects are not followed;
configure the final API base URL.

`max_retries` applies only to GET and HEAD requests. Write requests are attempted
once because a transport failure or server error can occur after a write has
already succeeded. Check the resulting state before retrying a write.

You can generate an API key in your Songstats Enterprise dashboard.

We recommend storing your key securely in environment variables:

    export SONGSTATS_API_KEY=your_key_here

---

## Available Resource Clients

- `client.info`
- `client.tracks`
- `client.artists`
- `client.collaborators`
- `client.labels`

Info endpoints:
- `client.info.sources()` -> `/sources`
- `client.info.status()` -> `/status`
- `client.info.definitions()` -> `/definitions`

---

## Error Handling

```python
from songstats_sdk import SongstatsAPIError, SongstatsTransportError

try:
    client.tracks.info(songstats_track_id="invalid")
except SongstatsAPIError as exc:
    print(f"API error: {exc}")
except SongstatsTransportError as exc:
    print(f"Transport error: {exc}")
```

---

## Development

To work on the SDK locally:

    git clone https://github.com/songstats/songstats-python-sdk.git
    cd songstats-python-sdk
    pip install -e ".[dev]"
    pytest

---

## Versioning

This SDK follows Semantic Versioning (SemVer).

---

## License

MIT

# Changelog

All notable changes to this project are documented in this file.

## [0.1.0] - 2026-02-19

### Added

- Initial standalone Python SDK repo for Songstats Enterprise API (`/enterprise/v1`)
- Full resource coverage:
  - `info`
  - `tracks`
  - `artists`
  - `collaborators`
  - `labels`
- Shared HTTP client with:
  - `apikey` header auth
  - JSON response decoding
  - retry/backoff on transport errors and retryable status codes
- Structured exception types for API and transport failures
- Route coverage audit doc mapping Rails routes to SDK methods
- Test suite covering route mapping, header auth, validation, and error handling

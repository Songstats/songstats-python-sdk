# Enterprise Routes Audit (Songstats Rails -> Python SDK)

Audited against:

- `/Users/Oskar/1001tl/config/routes.rb`
- `/Users/Oskar/1001tl/app/controllers/enterprise/v1/*.rb`
- `/Users/Oskar/1001tl/app/helpers/enterprise_helper.rb`

Authentication observed in Rails: `apikey` request header.

## `/enterprise/v1/info`

| HTTP | Route           | SDK Method                   |
| ---- | --------------- | ---------------------------- |
| GET  | `/sources`      | `client.info.sources()`      |
| GET  | `/status`       | `client.info.status()`       |
| GET  | `/uptime_check` | `client.info.uptime_check()` |
| GET  | `/definitions`  | `client.info.definitions()`  |

## `/enterprise/v1/tracks`

| HTTP   | Route                               | SDK Method                                              |
| ------ | ----------------------------------- | ------------------------------------------------------- |
| GET    | `/info`                             | `client.tracks.info(...)`                               |
| GET    | `/stats`                            | `client.tracks.stats(...)`                              |
| GET    | `/historic_stats`                   | `client.tracks.historic_stats(...)`                     |
| GET    | `/search`                           | `client.tracks.search(q=..., ...)`                      |
| GET    | `/activities`                       | `client.tracks.activities(...)`                         |
| GET    | `/comments`                         | `client.tracks.comments(...)`                           |
| GET    | `/songshare`                        | `client.tracks.songshare(...)`                          |
| GET    | `/locations`                        | `client.tracks.locations(...)`                          |
| POST   | `/link_request`                     | `client.tracks.add_link_request(link=..., ...)`         |
| DELETE | `/link_request`                     | `client.tracks.remove_link_request(link=..., ...)`      |
| POST   | `/add_to_member_relevant_list`      | `client.tracks.add_to_member_relevant_list(...)`        |
| DELETE | `/remove_from_member_relevant_list` | `client.tracks.remove_from_member_relevant_list(...)`   |

## `/enterprise/v1/artists`

| HTTP   | Route                               | SDK Method                                                  |
| ------ | ----------------------------------- | ----------------------------------------------------------- |
| GET    | `/info`                             | `client.artists.info(...)`                                  |
| GET    | `/stats`                            | `client.artists.stats(...)`                                 |
| GET    | `/historic_stats`                   | `client.artists.historic_stats(...)`                        |
| GET    | `/audience`                         | `client.artists.audience(...)`                              |
| GET    | `/audience/details`                 | `client.artists.audience_details(country_code=..., ...)`    |
| GET    | `/catalog`                          | `client.artists.catalog(...)`                               |
| GET    | `/search`                           | `client.artists.search(q=..., ...)`                         |
| GET    | `/activities`                       | `client.artists.activities(...)`                            |
| GET    | `/songshare`                        | `client.artists.songshare(...)`                             |
| GET    | `/top_tracks`                       | `client.artists.top_tracks(...)`                            |
| GET    | `/top_playlists`                    | `client.artists.top_playlists(...)`                         |
| GET    | `/top_curators`                     | `client.artists.top_curators(...)`                          |
| GET    | `/top_commentors`                   | `client.artists.top_commentors(...)`                        |
| POST   | `/link_request`                     | `client.artists.add_link_request(link=..., ...)`            |
| DELETE | `/link_request`                     | `client.artists.remove_link_request(link=..., ...)`         |
| POST   | `/track_request`                    | `client.artists.add_track_request(...)`                     |
| DELETE | `/track_request`                    | `client.artists.remove_track_request(...)`                  |
| POST   | `/add_to_member_relevant_list`      | `client.artists.add_to_member_relevant_list(...)`           |
| DELETE | `/remove_from_member_relevant_list` | `client.artists.remove_from_member_relevant_list(...)`      |

## `/enterprise/v1/collaborators`

| HTTP   | Route                               | SDK Method                                                        |
| ------ | ----------------------------------- | ----------------------------------------------------------------- |
| GET    | `/info`                             | `client.collaborators.info(...)`                                  |
| GET    | `/stats`                            | `client.collaborators.stats(...)`                                 |
| GET    | `/historic_stats`                   | `client.collaborators.historic_stats(...)`                        |
| GET    | `/audience`                         | `client.collaborators.audience(...)`                              |
| GET    | `/audience/details`                 | `client.collaborators.audience_details(country_code=..., ...)`    |
| GET    | `/catalog`                          | `client.collaborators.catalog(...)`                               |
| GET    | `/search`                           | `client.collaborators.search(q=..., ...)`                         |
| GET    | `/activities`                       | `client.collaborators.activities(...)`                            |
| GET    | `/songshare`                        | `client.collaborators.songshare(...)`                             |
| GET    | `/top_tracks`                       | `client.collaborators.top_tracks(...)`                            |
| GET    | `/top_playlists`                    | `client.collaborators.top_playlists(...)`                         |
| GET    | `/top_curators`                     | `client.collaborators.top_curators(...)`                          |
| GET    | `/top_commentors`                   | `client.collaborators.top_commentors(...)`                        |
| POST   | `/link_request`                     | `client.collaborators.add_link_request(link=..., ...)`            |
| DELETE | `/link_request`                     | `client.collaborators.remove_link_request(link=..., ...)`         |
| POST   | `/track_request`                    | `client.collaborators.add_track_request(...)`                     |
| DELETE | `/track_request`                    | `client.collaborators.remove_track_request(...)`                  |
| POST   | `/add_to_member_relevant_list`      | `client.collaborators.add_to_member_relevant_list(...)`           |
| DELETE | `/remove_from_member_relevant_list` | `client.collaborators.remove_from_member_relevant_list(...)`      |

## `/enterprise/v1/labels`

| HTTP   | Route                               | SDK Method                                                 |
| ------ | ----------------------------------- | ---------------------------------------------------------- |
| GET    | `/info`                             | `client.labels.info(...)`                                  |
| GET    | `/stats`                            | `client.labels.stats(...)`                                 |
| GET    | `/historic_stats`                   | `client.labels.historic_stats(...)`                        |
| GET    | `/audience`                         | `client.labels.audience(...)`                              |
| GET    | `/audience/details`                 | `client.labels.audience_details(country_code=..., ...)`    |
| GET    | `/catalog`                          | `client.labels.catalog(...)`                               |
| GET    | `/search`                           | `client.labels.search(q=..., ...)`                         |
| GET    | `/activities`                       | `client.labels.activities(...)`                            |
| GET    | `/songshare`                        | `client.labels.songshare(...)`                             |
| GET    | `/top_tracks`                       | `client.labels.top_tracks(...)`                            |
| GET    | `/top_playlists`                    | `client.labels.top_playlists(...)`                         |
| GET    | `/top_curators`                     | `client.labels.top_curators(...)`                          |
| GET    | `/top_commentors`                   | `client.labels.top_commentors(...)`                        |
| POST   | `/link_request`                     | `client.labels.add_link_request(link=..., ...)`            |
| DELETE | `/link_request`                     | `client.labels.remove_link_request(link=..., ...)`         |
| POST   | `/track_request`                    | `client.labels.add_track_request(...)`                     |
| DELETE | `/track_request`                    | `client.labels.remove_track_request(...)`                  |
| POST   | `/add_to_member_relevant_list`      | `client.labels.add_to_member_relevant_list(...)`           |
| DELETE | `/remove_from_member_relevant_list` | `client.labels.remove_from_member_relevant_list(...)`      |

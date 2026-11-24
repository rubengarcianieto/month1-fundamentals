# month1-fundamentals

Practice projects from month 1 of an 8-month study plan on AI orchestration:
HTTP, JSON, pydantic, async and testing. They are the technical groundwork
for [SNAIL](https://github.com/rubengarcianieto/snail).

## Contents

- `day2_*.py`: HTTP requests and the `requests` response object.
- `day3_*.py`: pydantic models and validation errors.
- `day4_async.py`: async vs sync requests, with a benchmark
  (see [BENCHMARK.md](docs/BENCHMARK.md)).
- `day5_weather_client.py`: async weather client with retries, pydantic
  validation and offline tests (`day5_weather_test.py`).

## Setup

Requires Python 3.14 and [uv](https://docs.astral.sh/uv/).

    uv sync

## Run the tests

    uv run pytest -v

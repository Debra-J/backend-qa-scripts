
# backend-qa-scripts

A collection of Python scripts and utilities for backend QA work — API validation, data filtering, and test helpers.

## What's in this repo

### `qa_data_filters.py`

Practice scripts for filtering common backend QA data:

- **`check_claims()`** — filters a list of claim IDs above a threshold value
- **`check_status_codes()`** — identifies HTTP status codes that indicate an error (4xx and 5xx)
- **`check_slow_responses()`** — identifies API response times above a slow threshold (500ms)

The file also includes examples of working with Python dictionaries — the same structure JSON API responses use — including a single member dictionary and a list of member dictionaries iterated with a for loop.

## How to run

Open the file in any Python 3 environment and run it. No external dependencies required.

## About

I'm a QA professional actively building hands-on Python skills with a focus on backend testing scenarios. This repo holds the practice scripts I'm writing as I learn — filtering data, working with API-shaped responses, and building reusable functions.

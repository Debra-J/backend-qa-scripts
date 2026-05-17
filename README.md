# backend-qa-scripts

Python practice scripts for backend QA work. Two files: one for data filtering, one for testing public web pages.

## What's in this repo

### qa_data_filters.py

Filter functions for common backend QA data:

- `check_claims()` - takes a list of claim IDs, prints the ones above a threshold (>102)
- `check_status_codes()` - takes a list of HTTP status codes, prints any that are errors (>= 400, so 4xx and 5xx)
- `check_slow_responses()` - takes a list of response times in milliseconds, prints any over 500ms

Also has a couple of examples showing how to work with Python dictionaries (the same shape JSON API responses use) - one single member dict, and a list of member dicts looped through with a for loop.

### test_judi_public_pages.py

Four health checks for the public judi.health pages, written using the requests library:

- `test_homepage_is_up()` - sends a GET to the homepage, asserts the status code is 200
- `test_homepage_response_time()` - times how long the homepage takes to respond, flags anything over 3 seconds
- `test_homepage_contains_expected_content()` - checks that "Judi" is in the homepage HTML (catches a deploy that returned wrong content)
- `test_key_pages_return_200()` - hits three public pages in a loop, prints whether each returned 200 or not

Same patterns I'd use for backend API testing, just pointed at internal URLs instead.

## How to run

Both files run in any Python 3 environment.

`test_judi_public_pages.py` needs the requests library. Google Colab has it pre-installed. To run locally: `pip install requests`.

## About

I am a Senior QA analyst with 15+ years across healthcare and enterprise platforms. Expanding into backend Python and API testing - this repo holds the practice work.

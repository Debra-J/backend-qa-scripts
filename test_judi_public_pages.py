"""
test_judi_public_pages.py
Basic QA health checks for judi.health public pages.
"""

import requests
import time


def test_homepage_is_up():
    # uptime check
    response = requests.get("https://www.judi.health/")
    assert response.status_code == 200
    print(f"PASS: judi.health homepage returned {response.status_code}")


def test_homepage_response_time():
    # time the request, flag if slow
    start = time.time()
    response = requests.get("https://www.judi.health/")
    elapsed = time.time() - start

    assert response.status_code == 200
    print(f"Response time: {elapsed:.2f}s")

    if elapsed > 3.0:
        print(f"WARNING: Homepage is slow ({elapsed:.2f}s)")
    else:
        print(f"PASS: Response time is acceptable")


def test_homepage_contains_expected_content():
    # make sure brand name is on the page
    response = requests.get("https://www.judi.health/")
    assert response.status_code == 200
    assert "Judi" in response.text
    print("PASS: Homepage contains expected brand content")


def test_key_pages_return_200():
    # sweep key pages, flag any that aren't 200
    public_pages = [
        "https://www.judi.health/",
        "https://www.judi.health/about",
        "https://www.judi.health/about/careers",
    ]

    for url in public_pages:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"BROKEN: {url} returned {response.status_code}")
        else:
            print(f"PASS: {url} returned {response.status_code}")


if __name__ == "__main__":
    print("Running public page health checks for judi.health...\n")

    test_homepage_is_up()
    print()

    test_homepage_response_time()
    print()

    test_homepage_contains_expected_content()
    print()

    test_key_pages_return_200()

    print("\nAll checks complete.")

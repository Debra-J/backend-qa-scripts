# QA Data Filtering Scripts
# Python practice scripts for filtering common backend QA data:
# claim IDs, HTTP status codes, response times, and member records.


def check_claims():
    claims = [101, 102, 103, 104, 105]
    for claim_id in claims:
        if claim_id > 102:
            print(claim_id)


def check_status_codes():
    status_codes = [200, 201, 404, 500, 200, 400]
    for code in status_codes:
        if code >= 400:
            print(code)


def check_slow_responses():
    response_times = [120, 350, 750, 200, 1200, 80]
    for response in response_times:
        if response > 500:
            print(response)


member = {"name": "Debra", "id": 123, "status": "active"}
print(member["name"])
print(member["id"])
print(member["status"])


members = [
    {"name": "Debra", "id": 123, "status": "active"},
    {"name": "Sawyer", "id": 124, "status": "inactive"},
    {"name": "Mads", "id": 125, "status": "active"}
]

for m in members:
    print(m["name"], m["status"])


check_slow_responses()
check_claims()
check_status_codes()

import os
import random
import string

import redis
from flask import Flask

app = Flask(__name__)
os.getenv("")

redis_url = os.getenv("REDIS_URL", "redis://redis:6379?decode_responses=True")
redis_connection = redis.from_url(redis_url)


@app.get("/")
def alive():
    count: int = redis_connection.incr("alive")
    return f"It's alive my friend {count} times!"


@app.get("/api/<path:random_path>/")
def api_group(random_path):
    counter = redis_connection.incr(random_path, 1)

    return f"Path: {random_path} was hit {counter} times."


@app.get("/stats/")
def stats():
    random_paths = redis_connection.keys("*")
    stats = {key: redis_connection.get(key) for key in random_paths}

    return {"urls": stats}


def generate_random_segment():
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(3))

    return result_str


def create_one_random_url(number_of_segments, pool_of_segments):
    url = ""

    for _ in range(number_of_segments):
        random.randint(1, 3)
        pool_of_segments_as_list = list(pool_of_segments)
        random_element = random.choice(pool_of_segments_as_list)
        url += f"/{random_element}"

    return f"{url}/"


def generate_random_urls(number_of_urls):
    """Function to generate random urls"""
    pool_of_segments = set()
    pool_size = 3
    random_urls = []

    while len(pool_of_segments) < pool_size:
        pool_of_segments.add(generate_random_segment())

    for url in range(number_of_urls):
        number_of_segments = random.randint(1, 6)
        random_urls.append(create_one_random_url(number_of_segments, pool_of_segments))

    return random_urls


@app.post("/test/<int:number_of_requests>")
def test(number_of_requests):
    random_urls = generate_random_urls(number_of_requests)
    requests_made = []
    client = app.test_client()

    for url in random_urls:
        response = client.get(f"/api{url}")
        # Assuming here that may the requests can fail
        if response.status_code == 200:
            requests_made.append(url)

    return {
        "number of requests": number_of_requests,
        "requests": requests_made,
    }

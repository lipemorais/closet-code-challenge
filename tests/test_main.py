from unittest import mock
from unittest.mock import ANY

from src.main import (
    app,
    generate_random_segment,
    create_one_random_url,
    generate_random_urls,
)

test_client = app.test_client()


@mock.patch("src.main.redis_connection")
def test_root(redis_connection):
    redis_connection.incr.return_value = 15
    response = test_client.get("/")

    assert response.text == "It's alive my friend 15 times!"


@mock.patch("src.main.redis_connection")
def test_api_endpoint(redis_connection):
    redis_connection.incr.return_value = 15
    api_random_url = "/api/some/random/path/"
    response = test_client.get(api_random_url)

    assert response.text == "Path: some/random/path was hit 15 times."


@mock.patch("src.main.redis_connection")
def test_stats_endpoint(redis_connection):
    redis_connection.keys.return_value = ["/abc/"]
    redis_connection.get.return_value = 1

    test_client.post("/test/1d")
    response = test_client.get("/stats/")

    assert response.json == {"urls": {"/abc/": 1}}


@mock.patch("src.main.redis_connection")
def test_test_endpoint(redis_connection):
    redis_connection.incr.return_value = 15
    number_of_requests = 2
    response = test_client.post(f"/test/{number_of_requests}")

    assert redis_connection.incr.call_count == number_of_requests
    assert response.json == {
        "number of requests": number_of_requests,
        "requests": [ANY, ANY],
    }


def test_random_segment_generator():
    segment = generate_random_segment()

    assert len(segment) == 3
    assert type(segment) is str


def test_create_one_random_url():
    url = create_one_random_url(2, {"123", "456", "789"})

    assert type(url) == str
    assert url.count("/") == 3


def test_generate_random_urls():
    urls = generate_random_urls(6)

    assert len(urls) == 6

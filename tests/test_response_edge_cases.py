"""Deterministic API edge-case tests."""

import pytest
import requests
import responses

from api.client import DummyJsonClient


@responses.activate
def test_empty_success_response_body_is_handled(api_client):
    responses.add(
        responses.GET,
        "https://dummyjson.com/products/empty",
        body="",
        status=200,
        content_type="application/json",
    )

    response = api_client.get("/products/empty")

    assert response.status_code == 200

    with pytest.raises(requests.exceptions.JSONDecodeError):
        response.json()


def test_request_timeout_is_propagated():
    client = DummyJsonClient(timeout=0.01)

    def simulate_timeout(*args, **kwargs):
        raise requests.exceptions.Timeout("Simulated API timeout")

    client.session.get = simulate_timeout

    try:
        with pytest.raises(requests.exceptions.Timeout, match="Simulated API timeout"):
            client.get("/products/1")
    finally:
        client.close()

"""Shared test fixtures."""

import pytest
from playwright.sync_api import sync_playwright

from api.client import DummyJsonClient


@pytest.fixture
def api_client():
    client = DummyJsonClient()
    yield client
    client.close()


@pytest.fixture
def playwright():
    with sync_playwright() as playwright_instance:
        yield playwright_instance

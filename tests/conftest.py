"""Shared test fixtures."""

import pytest
from playwright.sync_api import sync_playwright

from api.client import DummyJsonClient


@pytest.fixture
def api_client():
    client = DummyJsonClient()
    yield client
    client.close()



@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as playwright_instance:
        yield playwright_instance


@pytest.fixture
def browser(playwright):
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=1000
    )
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

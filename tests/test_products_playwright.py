"""Product API test using Playwright APIRequestContext."""

import pytest


@pytest.mark.playwright_api
def test_product_endpoint_with_playwright_api_request(playwright):
    request_context = playwright.request.new_context(
        base_url="https://dummyjson.com",
        extra_http_headers={"Accept": "application/json"},
        timeout=10_000,
    )

    try:
        response = request_context.get("/products/1")

        assert response.status == 200

        product = response.json()
        assert product["id"] == 1
        assert isinstance(product["title"], str)
        assert product["title"].strip() != ""
    finally:
        request_context.dispose()

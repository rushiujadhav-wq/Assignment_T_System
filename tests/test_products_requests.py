"""Product API tests using Requests."""

import pytest


@pytest.mark.api
def test_get_product_by_valid_id_returns_expected_response(api_client):
    response = api_client.get("/products/1")

    assert response.status_code == 200

    product = response.json()
    assert product["id"] == 1
    assert isinstance(product["title"], str)
    assert product["title"].strip()


@pytest.mark.api
def test_get_products_returns_product_collection(api_client):
    response = api_client.get("/products")

    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload["products"], list)
    assert len(payload["products"]) > 0
    assert isinstance(payload["total"], int)


@pytest.mark.api
def test_product_data_types_and_constraints(api_client):
    response = api_client.get("/products/1")

    assert response.status_code == 200
    product = response.json()

    assert isinstance(product["id"], int)
    assert product["id"] > 0
    assert isinstance(product["title"], str)
    assert product["title"].strip() != ""
    assert isinstance(product["price"], (int, float))
    assert product["price"] > 0


@pytest.mark.api
def test_nonexistent_product_returns_not_found(api_client):
    response = api_client.get("/products/999999")

    assert response.status_code == 404


@pytest.mark.api
def test_product_search_returns_valid_collection(api_client):
    response = api_client.get("/products/search", params={"q": "phone"})

    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload["products"], list)
    assert isinstance(payload["total"], int)

@pytest.mark.api
def test_invalid_product_id_returns_not_found(api_client):
    response = api_client.get("/products/invalid")

    assert response.status_code == 404


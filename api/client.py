"""Reusable HTTP client for DummyJSON API requests."""

import os

import requests


class DummyJsonClient:
    """Provides a shared Requests session and common request configuration."""

    def __init__(self, base_url=None, timeout=10.0):
        self.base_url = (
            base_url or os.getenv("API_BASE_URL", "https://dummyjson.com")
        ).rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, endpoint, **kwargs):
        """Send a GET request to the configured API."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        timeout = kwargs.pop("timeout", self.timeout)
        return self.session.get(url, timeout=timeout, **kwargs)

    def close(self):
        """Close the underlying HTTP session."""
        self.session.close()

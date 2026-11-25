# QA Automation and DevOps Assignment

## Overview

This repository contains an API automation suite and a Docker-based execution environment.

### Technology stack

- Python
- Pytest
- Requests
- Playwright APIRequestContext
- Docker
- Docker Compose

## Repository structure

```text
assignment_T_system/
├── api/
│   ├── __init__.py
│   └── client.py
├── tests/
│   ├── conftest.py
│   ├── test_products_requests.py
│   ├── test_products_playwright.py
│   └── test_response_edge_cases.py
├── config/
│   └── README.md
├── docker/
│   └── Dockerfile
├── test-results/
│   └── .gitkeep
├── logs/
│   └── .gitkeep
├── .env.example
├── .gitignore
├── compose.yaml
├── pytest.ini
└── requirements.txt
```

## API automation

### Test coverage

| Area | Coverage |
|---|---|
| Successful response | Retrieve a product and product collection |
| Response validation | HTTP status, JSON structure and expected fields |
| Data types | Product ID, title and price |
| Constraints | Positive product ID and price; non-empty title |
| Negative scenario | Request a product ID that does not exist |
| Search | Search products and validate the returned collection |
| Empty response | Verify handling of an empty response body |
| Timeout | Verify handling of a simulated request timeout |
| Playwright API | Retrieve and validate a product using APIRequestContext |

### Local setup

Python 3.11 or later is recommended.

Create and activate a virtual environment.

**Windows PowerShell**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux / macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Install the Playwright browser:

```bash
playwright install chromium
```

Run the test suite:

```bash
pytest -v
```

Run the Requests-based tests:

```bash
pytest -v tests/test_products_requests.py tests/test_response_edge_cases.py
```

Run the Playwright API test:

```bash
pytest -v tests/test_products_playwright.py
```

Generate HTML and JUnit reports:

```bash
pytest -v --html=test-results/report.html --self-contained-html --junitxml=test-results/junit.xml
```

## Docker environment

### Proxy configuration

Copy `.env.example` to `.env` and replace the placeholder values with the proxy address and port supplied by the infrastructure team.

**Windows PowerShell**
```powershell
Copy-Item .env.example .env
```

**Linux**
```bash
cp .env.example .env
```

The proxy configuration is supplied through environment variables. Do not commit credentials or sensitive proxy information.

### Build and start

```bash
docker compose up -d --build
```

### Execute tests inside the container

```bash
docker compose exec playwright pytest -v --html=test-results/report.html --self-contained-html --junitxml=test-results/junit.xml
```

### Administrative commands

| Operation | Command |
|---|---|
| Start and build services | `docker compose up -d --build` |
| Check service status | `docker compose ps` |
| View service logs | `docker compose logs -f playwright` |
| Execute tests | `docker compose exec playwright pytest -v --html=test-results/report.html --self-contained-html --junitxml=test-results/junit.xml` |
| Stop services | `docker compose stop` |
| Start stopped services | `docker compose start` |
| Remove containers and network | `docker compose down` |

## Persistence and restart behavior

The `test-results` and `logs` directories are mounted from the host into the container. Reports and logs therefore remain available on the host when the container is restarted or recreated.

The service uses `restart: unless-stopped`. Docker restarts the container after a host reboot unless the service was explicitly stopped. Docker Engine must also be configured to start automatically with the host operating system.

## Proxy considerations

- HTTP and HTTPS proxy variables are passed into the container.
- Docker build arguments make proxy settings available during dependency installation.
- Docker Engine may require its own proxy configuration to pull the base image from the registry.
- The `NO_PROXY` variable identifies hosts that should bypass the proxy.
- The proxy IP and port in `.env.example` are placeholders and must be replaced with the values provided for the target environment.

## Design decisions

1. A reusable API client centralizes the base URL, session and request timeout.
2. Pytest fixtures manage API client setup and teardown.
3. Requests is used for the primary API suite, while Playwright APIRequestContext is used for a separate API test.
4. Mocked timeout and empty-response scenarios provide deterministic edge-case coverage.
5. The Playwright Python dependency and official Playwright container image use the same pinned release.
6. Host bind mounts preserve reports and logs outside the container lifecycle.
7. Proxy settings are externalized from application code.
8. The Compose service structure supports adding independent services such as Prometheus and Grafana.

## Future expansion

Additional services can be defined under `services` in `compose.yaml`. Service-specific configuration can be maintained under `config/`, with persistent data directories added as required.

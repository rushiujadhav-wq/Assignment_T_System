FROM mcr.microsoft.com/playwright/python:v1.56.0-noble

WORKDIR /app
ENV PYTHONPATH=/app

ARG HTTP_PROXY
ARG HTTPS_PROXY
ARG NO_PROXY

COPY requirements.txt .

RUN HTTP_PROXY="${HTTP_PROXY}" \
    HTTPS_PROXY="${HTTPS_PROXY}" \
    NO_PROXY="${NO_PROXY}" \
    pip install --no-cache-dir -r requirements.txt

COPY api/ ./api/
COPY tests/ ./tests/
COPY pytest.ini .

CMD ["pytest", "-v"]

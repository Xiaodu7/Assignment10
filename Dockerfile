FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --only-upgrade zlib1g && \
    rm -rf /var/lib/apt/lists/*


ENV PYTHONDONTWRITEBYTECODE=1 \
   PYTHONUNBUFFERED=1

WORKDIR /app


RUN python -m pip install --upgrade pip 'setuptools>=78.1.1' wheel && \
    groupadd -r appgroup && \
    useradd -r -g appgroup appuser


COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt && \
    python -m pip uninstall -y pip


COPY . .
RUN chown -R appuser:appgroup /app

USER appuser

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/', timeout=3)" || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

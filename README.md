
# IS601 Module 10 Assignment

## Secure User Model and CI/CD Pipeline

This project is for Module 10 of IS601.

I used FastAPI, PostgreSQL, SQLAlchemy, and Docker to build and test a web application with a secure user model.

## Technologies Used

- Python 3.12
- FastAPI and Pydantic
- PostgreSQL 17
- SQLAlchemy
- bcrypt Password Hashing
- JWT Authentication
- pytest and Playwright
- Docker and GitHub Actions
- Trivy Security Scanner

## Features

- User registration and authentication
- Password hashing instead of plain-text storage
- User data validation using Pydantic
- PostgreSQL database integration
- Unit, integration, and E2E testing
- Automated CI/CD pipeline
- Docker image security scanning

## Setup

Create a Python environment:

```bash
uv python install 3.12
uv venv --python 3.12 venv
source venv/bin/activate
uv pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

Open http://localhost:8000

## Testing

Run all tests:

```bash
python -m pytest tests/ -v
```

Local test results:

- 77 passed
- 1 skipped
- 98% code coverage

## Docker

Build the image:

```bash
docker build -t assignment10:local .
```

Run the published image:

```bash
docker run --rm -p 8001:8000 xdu7/assignment10:latest
```

## CI/CD Pipeline

GitHub Actions automatically performs:

1. Python testing with PostgreSQL
2. Docker security scanning using Trivy
3. Docker image deployment to Docker Hub

All three jobs completed successfully.

## Project Links

GitHub Repository:
https://github.com/Xiaodu7/Assignment10

Docker Hub:
https://hub.docker.com/r/xdu7/assignment10

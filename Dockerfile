# Use the specified Python base image
FROM python:3.11-slim-bullseye

# Set environment variables
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y postgresql-client vim curl python3-opencv poppler-utils libreoffice build-essential \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get autoremove -y && apt-get clean

# Add poetry to PATH
ENV PATH="${PATH}:/root/.local/bin"

# Set the work directory in docker and copy project to work directory
WORKDIR /ai_implementation

# Copy the content of the local src directory to the working directory
COPY pyproject.toml poetry.lock* /ai_implementation/

RUN poetry config installer.max-workers 10
# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the content of the local src directory to the working directory
COPY . /ai_implementation/

# Download nltk packages
RUN python3 /ai_implementation/data/download_nltk_packages.py

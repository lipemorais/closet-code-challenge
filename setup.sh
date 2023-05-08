#!/bin/bash

# Install dependencies
poetry install

# Run pytest
poetry run pytest

# Activate the virtual environment
poetry shell


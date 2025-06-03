#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Collect static files (crucial for CSS/JS/images in production)
python manage.py collectstatic --no-input

# Apply database migrations (CRITICAL for creating tables like auth_user)
python manage.py migrate
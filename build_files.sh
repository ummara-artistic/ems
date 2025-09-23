#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Apply migrations
echo "Applying database migrations..."
python3 manage.py migrate --noinput

# Collect static files into the folder Vercel expects
echo "Collecting static files..."
# Ensure STATIC_ROOT is defined in settings.py as staticfiles_build
python3 manage.py collectstatic --noinput --clear

echo "Build completed successfully."

#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -o errexit

echo "=== Starting Neon PostgreSQL Deployment ==="

# 1. Install Python dependencies from requirements.txt
python3 -m pip install -r requirements.txt

# 2. Run Django migrations (FORCEFULLY for Neon PostgreSQL)
echo "Running database migrations..."
python3 manage.py migrate --no-input

# 3. If migrations fail, try with fake migrations
if [ $? -ne 0 ]; then
    echo "First migration attempt failed, trying with fake migrations..."
    python3 manage.py migrate --fake
    python3 manage.py migrate --no-input
fi

# 4. Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --no-input

echo "=== Neon PostgreSQL Deployment Completed ==="

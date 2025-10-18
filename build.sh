#!/bin/bash

# Exit on error
set -o errexit

# Install SQLite3 dependencies
apt-get update && apt-get install -y sqlite3 libsqlite3-dev

# Install Python dependencies from requirements.txt
python3 -m pip install -r requirements.txt

# Run Django commands
python3 manage.py collectstatic --no-input
python3 manage.py migrate

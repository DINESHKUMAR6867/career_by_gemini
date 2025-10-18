#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -o errexit

# 1. Install SQLite native dependencies using Vercel's available package manager (apk)
# This fixes the "ModuleNotFoundError: No module named '_sqlite3'"
apk update
apk add sqlite sqlite-dev

# 2. Install Python dependencies from requirements.txt
python3 -m pip install -r requirements.txt

# 3. Run Django commands
python3 manage.py collectstatic --no-input
python3 manage.py migrate

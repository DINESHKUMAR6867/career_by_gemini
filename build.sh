#!/bin/bash

# Exit on error
set -o errexit

# 1. Install SQLite native dependencies using the available package manager (apk)
apk update
apk add sqlite sqlite-dev

# 2. Install Python dependencies
python3 -m pip install -r requirements.txt

# 3. Force SQLite Python module to re-compile against the new system libraries (optional but safe)
python3 -m pip install --upgrade --force-reinstall "Django==4.2.7"

# 4. Run Django commands
python3 manage.py collectstatic --no-input
python3 manage.py migrate

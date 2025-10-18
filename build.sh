#!/bin/bash

# Exit on error
set -o errexit

# Install Python
apt-get update && apt-get install -y python3 python3-pip

# Install required Python packages
python3 -m pip install -r requirements.txt

# Run Django commands
python3 manage.py collectstatic --no-input
python3 manage.py migrate

#!/bin/bash

# Exit on error
set -o errexit

# These commands will run as part of the Vercel "installCommand"
# after the Python environment is set up and requirements are installed.

# Run Django commands
python3 manage.py collectstatic --no-input
python3 manage.py migrate

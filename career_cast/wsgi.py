# import os
# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "career_cast.settings")

# # Vercel expects this name
# app = get_wsgi_application()

# try:
#     from django.core.management import call_command
#     call_command("migrate", interactive=False, verbosity=0)
# except Exception as e:
#     print("Migrations skipped:", e)

import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'career_cast.settings')

# Import Django after setting the environment
import django
from django.core.management import execute_from_command_line

# Configure Django
django.setup()

# Run migrations automatically
try:
    print("Attempting to run migrations...")
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'migrate', '--noinput'])
    print("Migrations completed successfully!")
except Exception as e:
    print(f"Migration error (may be normal if already run): {e}")

# Get the WSGI application
app = get_wsgi_application()



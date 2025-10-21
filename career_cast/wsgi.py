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

# Add project directory to Python path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'career_cast.settings')

# Try to run migrations on startup (silent fail if already run)
try:
    import django
    django.setup()
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'migrate', '--noinput'])
except:
    pass  # Migrations may have already run

app = get_wsgi_application()

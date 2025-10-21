import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "career_cast.settings")

# Vercel expects this name
app = get_wsgi_application()

try:
    from django.core.management import call_command
    call_command("migrate", interactive=False, verbosity=0)
except Exception as e:
    print("Migrations skipped:", e)

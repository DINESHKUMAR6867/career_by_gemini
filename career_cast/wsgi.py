import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "career_cast.settings")

# Vercel expects this name
app = get_wsgi_application()

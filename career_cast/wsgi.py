import os
from django.core.wsgi import get_wsgi_application
from vercel import Vercel  # If you're deploying on Vercel

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'career_cast.settings')

application = get_wsgi_application()

if __name__ == "__main__":
    Vercel(application)  # For local testing with Vercel

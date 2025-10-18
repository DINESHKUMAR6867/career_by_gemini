import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-development-key')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'
# career_cast/settings.py

# ... other settings

ALLOWED_HOSTS = [
    # The Vercel subdomain for your current preview deployment:
    'career-by-gemini-dj36rh528-tunguturidineshkumar-6538s-projects.vercel.app',
    # Include the general Vercel wildcard for future deployments:
    '.vercel.app',
    # Include localhost/127.0.0.1 for local development (optional, but good practice)
    '127.0.0.1',
    'localhost',
]


INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_app',
    # 'crispy_forms',
    # 'crispy_bootstrap5',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

X_FRAME_OPTIONS = 'SAMEORIGIN'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default Django backend (used for other cases)
    'main_app.backends.EmailBackend',  # Custom backend for email login
]

AUTH_USER_MODEL = 'main_app.CustomUser'

ROOT_URLCONF = 'career_cast.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'career_cast.wsgi.application'

# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'Applywizz@123',
#         'HOST': 'db.jittzzsretkoldpyyvjy.supabase.co',
#         'PORT': '5432',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use SQLite as the default database
        'NAME': BASE_DIR / 'db.sqlite3',  # SQLite database file
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_DIRS = [os.path.join(BASE_DIR / 'main_app/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# This is where `collectstatic` will collect files to.
STATIC_ROOT = BASE_DIR / "staticfiles"
# This is where Django will look for additional static files.
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (user-uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Custom App Configurations ---
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# Outlook Email Configuration
OUTLOOK_TENANT_ID = os.getenv('OUTLOOK_TENANT_ID')
OUTLOOK_CLIENT_ID = os.getenv('OUTLOOK_CLIENT_ID')
OUTLOOK_CLIENT_SECRET = os.getenv('OUTLOOK_CLIENT_SECRET')
OUTLOOK_SENDER_EMAIL = os.getenv('OUTLOOK_SENDER_EMAIL')

# Gemini AI Configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Supabase Configuration
# SUPABASE_URL = os.getenv('SUPABASE_URL', 'https://jittzzsretkoldpyyvjy.supabase.co')
# SUPABASE_KEY = os.getenv('SUPABASE_ANON_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImppdHR6enNyZXRrb2xkcHl5dmp5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjAzNTYwODEsImV4cCI6MjA3NTkzMjA4MX0.8BEWr9vs21yRk45W0DIfYshpE-0ThNtz9pnEkkKiZz0')

# Authentication URLs
LOGIN_URL = '/auth/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# Sendfile configuration (for development only)

SENDFILE_BACKEND = 'sendfile.backends.development'




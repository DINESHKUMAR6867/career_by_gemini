import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ─── SECURITY ─────────────────────────────────────────────
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-development-key")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    ".vercel.app",
    "127.0.0.1",
    "localhost",
]

# ─── APPS ────────────────────────────────────────────────
INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main_app",
]
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Ensure this is set


# ─── MIDDLEWARE ──────────────────────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "career_cast.urls"

# ─── TEMPLATES ───────────────────────────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "career_cast.wsgi.application"

# ─── DATABASE ────────────────────────────────────────────
# ─── DATABASE (Supabase PostgreSQL + IPv4 + SSL) ──────────────
import socket, os

import dj_database_url
import os

import os
import dj_database_url

import os
import dj_database_url

# ─── DATABASE ────────────────────────────────────────────
# ─── DATABASE ────────────────────────────────────────────
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': 'ep-holy-base-ad624cg0-pooler.c-2.us-east-1.aws.neon.tech',  # NeonDB host
#         'NAME': 'neondb',
#         'USER': 'neondb_owner',
#         'PASSWORD': 'npg_twcB6gjO3Dmv',
#         'PORT': '5432',
#         'OPTIONS': {'sslmode': 'require'},
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',  # This is the database name
#         'USER': 'postgres',  # Your Supabase PostgreSQL username
#         'PASSWORD': 'Dinesh@123',  # Your password
#         'HOST': 'db.frdgrrfguukmqhmymott.supabase.co',  # The host from your URL
#         'PORT': '5432',  # Default PostgreSQL port
#     }
# }

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),  # Make sure DATABASE_URL is set in your environment variables
        conn_max_age=600,  # For better performance in production
        ssl_require=True  # This forces SSL connection to the database
    )
}




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'Dinesh@123',  # Keep as is in direct config
#         'HOST': 'db.wdklgycbyzrefhutkydw.supabase.co',
#         'PORT': '5432',
#         'OPTIONS': {
#             'sslmode': 'require',  # Crucial for Supabase
#         },
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'neondb',
#         'USER': 'neondb_owner',
#         'PASSWORD': 'npg_twcB6gjO3Dmv',
#         'HOST': 'ep-holy-base-ad624cg0-pooler.c-2.us-east-1.aws.neon.tech',
#         'PORT': '5432',
#         'OPTIONS': {
#             'sslmode': 'require',
#         },
#     }
# }

# import os
# from pathlib import Path
# import shutil

# BASE_DIR = Path(__file__).resolve().parent.parent

# # Writable copy in /tmp
# TMP_DB = Path("/tmp/db.sqlite3")

# # Path to bundled (read-only) copy in repo
# REPO_DB = BASE_DIR / "db.sqlite3"

# # On cold start, copy bundled DB to writable /tmp
# try:
#     if REPO_DB.exists() and not TMP_DB.exists():
#         shutil.copy(REPO_DB, TMP_DB)
# except Exception as e:
#     print("Failed to copy DB template:", e)

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": str(TMP_DB),
#     }
# }







# Force IPv4 connection (avoids “Network is unreachable”)
# try:
#     os.environ["PGHOSTADDR"] = socket.gethostbyname("db.wvfieqpcmzvvkoysckwv.supabase.co")
# except Exception as e:
#     print("Warning: Could not resolve IPv4 address:", e)

# try to commit






# ─── PASSWORD VALIDATION ─────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ─── INTERNATIONALIZATION ────────────────────────────────
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ─── STATIC & MEDIA ──────────────────────────────────────
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Make sure static is created if it doesn't exist
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
# Use /tmp directory which is writable on Vercel
MEDIA_ROOT = '/tmp/media'

# Or use in-memory file storage
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB - keep files in memory
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB
# MEDIA_ROOT = BASE_DIR / "media"

# ─── AUTHENTICATION ──────────────────────────────────────
AUTH_USER_MODEL = "main_app.CustomUser"
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "main_app.backends.EmailBackend",
]

# import os
# from pathlib import Path
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# BASE_DIR = Path(__file__).resolve().parent.parent

# # ─── SECURITY ─────────────────────────────────────────────
# SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-development-key")
# DEBUG = False  # Always False for production

# ALLOWED_HOSTS = [
#     ".vercel.app",
#     "127.0.0.1", 
#     "localhost",
#     "career-by-gemini.vercel.app",
#     "*.vercel.app"
# ]

# # ─── APPS ────────────────────────────────────────────────
# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     "main_app",
# ]

# # ─── MIDDLEWARE ──────────────────────────────────────────
# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "whitenoise.middleware.WhiteNoiseMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

# ROOT_URLCONF = "career_cast.urls"

# # ─── TEMPLATES ───────────────────────────────────────────
# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = "career_cast.wsgi.application"

# # ─── DATABASE ────────────────────────────────────────────
# # NEON POSTGRESQL CONFIGURATION
# # ─── DATABASE ────────────────────────────────────────────
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'neondb',
#         'USER': 'neondb_owner',
#         'PASSWORD': 'npg_twcB6gjO3Dmv',
#         'HOST': 'ep-holy-base-ad624cg0-pooler.c-2.us-east-1.aws.neon.tech',
#         'PORT': '5432',
#         'OPTIONS': {
#             'sslmode': 'require',
#         },
#         'CONN_MAX_AGE': 0,
#     }
# }

# # ─── PASSWORD VALIDATION ─────────────────────────────────
# AUTH_PASSWORD_VALIDATORS = [
#     {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
#     {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
#     {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
#     {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
# ]

# # ─── INTERNATIONALIZATION ────────────────────────────────
# LANGUAGE_CODE = "en-us"
# TIME_ZONE = "UTC"
# USE_I18N = True
# USE_TZ = True

# # ─── STATIC FILES ────────────────────────────────────────
# STATIC_URL = "/static/"
# STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# # ─── AUTHENTICATION ──────────────────────────────────────
# AUTH_USER_MODEL = "main_app.CustomUser"
# AUTHENTICATION_BACKENDS = [
#     "django.contrib.auth.backends.ModelBackend",
#     "main_app.backends.EmailBackend",
# ]
# LOGIN_URL = "/auth/"
# LOGIN_REDIRECT_URL = "/dashboard/"
# LOGOUT_REDIRECT_URL = "/"

# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# # ─── EXTERNAL API KEYS ───────────────────────────────────

# LOGIN_URL = "/auth/"
# LOGIN_REDIRECT_URL = "/dashboard/"
# LOGOUT_REDIRECT_URL = "/"

# ─── HEADERS & SECURITY ──────────────────────────────────
X_FRAME_OPTIONS = "SAMEORIGIN"

# ─── EXTERNAL SERVICES / KEYS ────────────────────────────
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OUTLOOK_TENANT_ID = os.getenv("OUTLOOK_TENANT_ID")
OUTLOOK_CLIENT_ID = os.getenv("OUTLOOK_CLIENT_ID")
OUTLOOK_CLIENT_SECRET = os.getenv("OUTLOOK_CLIENT_SECRET")
OUTLOOK_SENDER_EMAIL = os.getenv("OUTLOOK_SENDER_EMAIL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ─── DEFAULT PRIMARY KEY ─────────────────────────────────
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"






































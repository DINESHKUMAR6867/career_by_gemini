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

# --- DATABASE CONFIGURATION ---
DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}



# Force IPv4 connection (avoids “Network is unreachable”)
try:
    os.environ["PGHOSTADDR"] = socket.gethostbyname("db.wvfieqpcmzvvkoysckwv.supabase.co")
except Exception as e:
    print("Warning: Could not resolve IPv4 address:", e)

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
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ─── AUTHENTICATION ──────────────────────────────────────
AUTH_USER_MODEL = "main_app.CustomUser"
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "main_app.backends.EmailBackend",
]
LOGIN_URL = "/auth/"
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/"

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













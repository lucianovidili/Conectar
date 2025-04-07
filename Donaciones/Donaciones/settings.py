import os
from pathlib import Path
from pillow_heif import register_heif_opener

register_heif_opener()


# from Donaciones.OUT_oauth2_setup import obtener_credenciales

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-9!^v3yj$+(c_@b%(i7cqc94jqjvx+_hnpd&3$id+t7f!-!%%(u"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "AppDonaciones",
    "AppUsuarios",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Donaciones.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "Donaciones.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# SQLite3
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# PostgreSQL
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "donaciones",
#         "USER": "postgres",
#         "PASSWORD": "Chanipa",  # La misma con la qeu creaste en PsgreSQL Manager
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "es-ES"  # o 'es'

USE_L10N = True

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "AppDonaciones/static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "/usuarios/login"  # EL PATH no EL NOMBRE

MEDIA_URL = ""

MEDIA_ROOT = os.path.join(BASE_DIR, "AppDonaciones/static")

DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10 MB


# Cargar variables de entorno desde .env
# env = environ.Env()
# environ.Env.read_env()

# CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.json")

# settings.py
# desse hasta acá borré cuando andaba en localmailgun

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.mailgun.org"  # Servidor SMTP de Mailgun
# EMAIL_PORT = 587  # Puerto para conexiones TLS
# EMAIL_USE_TLS = True  # Usar TLS para seguridad
# EMAIL_HOST_USER = (
#     "postmaster@sandboxe3931eba496247ed946fb878f07ab861.mailgun.org"  # Usuario SMTP
# )
# EMAIL_HOST_PASSWORD = (
#     "d5c201f5a6b7d5ddcb3a2aede3735b83-f6202374-c108acfc"  # Contraseña SMTP
# )
# DEFAULT_FROM_EMAIL = (
#     "Luciano Vidili <postmaster@sandboxe3931eba496247ed946fb878f07ab861.mailgun.org>"
# )

# Configuración de Mailgun con Anymail
# INSTALLED_APPS += ["anymail"]

# ANYMAIL = {
#     # "MAILGUN_API_KEY": "bf33477cbfdd461880f1486946f152b6-24bda9c7-c4167fed",
#     "MAILGUN_API_KEY": "24bda9c7-c4167fed",
#     "MAILGUN_SENDER_DOMAIN": "mail.somosconcectar.org",
# }

# EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
# DEFAULT_FROM_EMAIL = "info@somosconectar.org"

# def get_access_token():
#     creds = None
#     if os.path.exists(CREDENTIALS_FILE):
#         creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE)
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())  # Refresca el token si ha expirado
#             with open(CREDENTIALS_FILE, "w") as token:
#                 token.write(creds.to_json())  # Guarda el token actualizado
#     if not creds or not creds.valid:
#         raise Exception("No se pudo obtener un Access Token válido.")
#     return creds.token


# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = "lucianovidili@gmail.com"  # Reemplaza con tu correo de Gmail
# EMAIL_HOST_PASSWORD = obtener_credenciales().token

# Configuración OAuth2
# EMAIL_HOST_CLIENT_ID = env("EMAIL_HOST_CLIENT_ID")
# EMAIL_HOST_CLIENT_SECRET = env("EMAIL_HOST_CLIENT_SECRET")
# EMAIL_HOST_REFRESH_TOKEN = env("EMAIL_HOST_REFRESH_TOKEN")


# Inicializa environ y carga el archivo .env
# Inicializa `environ`
# env = environ.Env()

# # Cargar variables del archivo .env
# environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# # Configuración del email
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = env("EMAIL_HOST")  # mail.somosconectar.org
# EMAIL_PORT = env.int("EMAIL_PORT", default=465)
# EMAIL_USE_SSL = env.bool("EMAIL_USE_TLS", default=True)
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")  # info@somosconectar.org
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")  # info@somosconectar.org

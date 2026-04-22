import os
from pathlib import Path

from .env import env_bool, env_list, env_str

BASE_DIR = Path(__file__).resolve().parent.parent

APP_ENV = env_str("APP_ENV", "development")
IS_PRODUCTION = APP_ENV == "production"

SECRET_KEY = env_str("DJANGO_SECRET_KEY", required=IS_PRODUCTION, default="unsafe-dev-secret-key")
DEBUG = env_bool("DJANGO_DEBUG", default=not IS_PRODUCTION)

if IS_PRODUCTION and DEBUG:
    raise RuntimeError("DJANGO_DEBUG cannot be enabled in production")

ALLOWED_HOSTS = env_list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])
if IS_PRODUCTION and not ALLOWED_HOSTS:
    raise RuntimeError("DJANGO_ALLOWED_HOSTS cannot be empty in production")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_filters',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'registry',
    'plot',
    'analysis',
    'django_filters',
    'accounts',
    'channels'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'flapjack_api.urls'

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

WSGI_APPLICATION = 'flapjack_api.wsgi.application'

DB_ENGINE = env_str("DB_ENGINE", "django.db.backends.postgresql")
DB_NAME = env_str("DB_NAME", "registry")
DB_USER = env_str("DB_USER", "postgres")
DB_PASSWORD = env_str("DB_PASSWORD", default="", required=IS_PRODUCTION)
DB_HOST = env_str("DB_HOST", "db")
DB_PORT = env_str("DB_PORT", "5432")

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

CORS_ORIGIN_ALLOW_ALL = env_bool("DJANGO_CORS_ALLOW_ALL", default=not IS_PRODUCTION)
CORS_ALLOWED_ORIGINS = env_list("DJANGO_CORS_ALLOWED_ORIGINS", default=[])
if IS_PRODUCTION and CORS_ORIGIN_ALLOW_ALL:
    raise RuntimeError("DJANGO_CORS_ALLOW_ALL cannot be enabled in production")

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework_filters.backends.RestFrameworkFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework_simplejwt.authentication.JWTAuthentication'],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
}

REDIS_HOST = env_str("REDIS_HOST", "redis")
REDIS_PORT = int(env_str("REDIS_PORT", "6379"))

ASGI_APPLICATION = "flapjack_api.routing.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(REDIS_HOST, REDIS_PORT)],
        },
    },
}

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

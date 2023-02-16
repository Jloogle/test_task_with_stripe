from pathlib import Path

import environ


env = environ.Env(
    SECRET_KEY=(str, '*'),
    ALLOWED_HOSTS=(list, []),
    DB_ENGINE=str,
    DB_NAME=str,
    POSTGRES_USER=str,
    POSTGRES_PASSWORD=str,
    DB_HOST=str,
    DB_PORT=int,
)
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env()
SECRET_KEY = env('SECRET_KEY', default='secret_key_123321')

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'payments',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'task_with_stripe.urls'

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

WSGI_APPLICATION = 'task_with_stripe.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE', default='django.db.backends.postgresql'),
        'NAME': env('DB_NAME', default='postgres'),
        'USER': env('POSTGRES_USER', default='postgres'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='postgres'),
        'HOST': env('DB_HOST', default='db'),
        'PORT': env('DB_PORT', default='5432'),
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



LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

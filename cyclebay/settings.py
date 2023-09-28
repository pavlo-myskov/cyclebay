"""
Django settings for cyclebay project.

Generated by 'django-admin startproject' using Django 3.2.21.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

DEVELOPMENT = os.getenv("DEVELOPMENT", False) == "True"
if DEVELOPMENT:
    print("Development mode is ON.")
else:
    print("Development mode is OFF.")

DEBUG = os.getenv("DEBUG", False) == "True"
if DEBUG:
    print("Debug mode is ON.")
else:
    print("Debug mode is OFF.")

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "cyclebay-bc1e75ddbf8e.herokuapp.com",
]

# Clickjacking protection. Means that you can
# only embed your site in an iframe on your own domain.
X_FRAME_OPTIONS = "SAMEORIGIN"

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    # Allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # Local apps
    "users",
    "home",
    "products",
    "bag",
    "checkout",
    "profiles",
    "wishlist",
    "invetorize",

    # Other apps
    "crispy_forms",
    "crispy_bootstrap4",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "cyclebay.urls"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "templates", "allauth"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # allows access the no image file in media folder
                # if there is no image for a product
                'django.template.context_processors.media',
                # Custom context processor for bag contents
                "bag.contexts.bag_contents",
                # Custom context processor for all categories
                "products.contexts.all_categories",
            ],
            "builtins": [
                # Allows us to use the 'crispy' template tag
                # in our templates without having to load it
                # in every template.
                "crispy_forms.templatetags.crispy_forms_tags",
                "crispy_forms.templatetags.crispy_forms_field",
            ],
        },
    },
]

WSGI_APPLICATION = "cyclebay.wsgi.application"

# Set custom user model as default
AUTH_USER_MODEL = "users.User"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa: E501
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
# Dir where static files will be collected using
# python manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ___Allauth settings___
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of allauth
    'django.contrib.auth.backends.ModelBackend',
    # allauth specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# Specifies the URL that the user will be redirected
# to after a successful login or logout.
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = 'accounts/login/'

# Removes the username field from the signup form.
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# Requires the user to enter a unique e-mail address during signup.
ACCOUNT_EMAIL_REQUIRED = True
# Removes the username field from the signup form.
ACCOUNT_USERNAME_REQUIRED = False
# Allows the user to log in using their e-mail address and password.
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# Prevents multiple signups with the same e-mail address.
ACCOUNT_UNIQUE_EMAIL = True
# asks the user to Remember Me at login to keep the user logged in
# even after closing the browser.
ACCOUNT_SESSION_REMEMBER = None
# User gets blocked from logging back in until a timeout.
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5

# email confirmation
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Logs the user in after confirming the email address.
# Works only when user signs up
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# Allows avoiding the need to confirm the email address
# on page form and can be done only by clicking the link
ACCOUNT_CONFIRM_EMAIL_ON_GET = True


# Email SMTP settings
if DEVELOPMENT:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'cyclebay@email.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'  # for gmail
    EMAIL_PORT = 587
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    # password must be generated from gmail account,
    # called App Passwords, not the same as account password
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
    EMAIL_USE_TLS = True

# Stripe settings
FREE_DELIVERY_THRESHOLD = 100
STANDARD_DELIVERY_PERCENTAGE = 10

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
STRIPE_CURRENCY = 'eur'


# Celery settings
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')

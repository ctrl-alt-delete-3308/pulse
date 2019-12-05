"""
Django prod settings for pulse_project project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os
import dj_database_url
from .defaults import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'csci-3308-pulse-stage.herokuapp.com', 'csci-3308-pulse.herokuapp.com', '127.0.0.1'
]

ADMINS = (
  ('Ryan Drew', 'learnitall0@gmail.com'),
  ('Rhett Hanscom', 'rhha1623@colorado.edu'),
  ('Michael Carter', 'mica6085@colorado.edu')
)

MANAGERS = ADMINS

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

# Security Settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

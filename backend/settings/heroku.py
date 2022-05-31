import environ

from backend.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

# ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

ALLOWED_HOSTS = ['quiet-forest-14873.herokuapp.com']

DATABASES = {
    "default": env.db(),
}

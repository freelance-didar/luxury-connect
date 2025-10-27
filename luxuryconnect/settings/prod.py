from .base import *  # noqa

# Production-specific overrides — ensure DEBUG is False in prod env
DEBUG = False
# Security hardening recommended: set SECURE_SSL_REDIRECT, SESSION_COOKIE_SECURE, etc.
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

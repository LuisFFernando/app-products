import os

API_VERSION = "v0.0.1"

SENTRY_DSN = os.environ.get('SENTRY_DSN', '')

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'staging')

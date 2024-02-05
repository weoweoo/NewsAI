import logging

from django_template.settings.default import *  # noqa: F401,F403

try:
    from django_template.settings.local import *  # noqa: F401,F403
except ImportError:
    pass

if ENABLE_SENTRY:  # noqa: F405
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.logging import LoggingIntegration

    sentry_logging = LoggingIntegration(
        level=logging.INFO,  # Capture info and above as breadcrumbs
        event_level=logging.INFO,  # Send info as events
    )

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration(), sentry_logging],
        release=VERSION,
        environment=SENTRY_ENV,
        traces_sample_rate=0.1,  # Do not touch, best practice is not 100%.
        send_default_pii=True,
    )

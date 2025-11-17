import os

# Try environment indicator first
_setting = os.environ.get("DJANGO_SETTINGS", None)

# If not set, try to parse DJANGO_SETTINGS_MODULE (ex: config.settings.dev)
if not _setting:
    dj = os.environ.get("DJANGO_SETTINGS_MODULE", "")
    if dj.startswith("config.settings."):
        _setting = dj.split(".")[-1]

# Default to dev
if not _setting:
    _setting = "dev"

if _setting == "prod":
    from .prod import *  # noqa
else:
    from .dev import *   # noqa

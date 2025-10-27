#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from typing import NoReturn


def main() -> NoReturn:
    """Run administrative tasks."""
    settings_env = "luxuryconnect.settings.dev"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_env)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH?"
        ) from exc
    execute_from_command_line(sys.argv)
    sys.exit(0)


if __name__ == "__main__":
    main()

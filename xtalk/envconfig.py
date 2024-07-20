import os

from django.core.exceptions import ImproperlyConfigured

_env_required = object()


def get_str(name: str, default=_env_required) -> str:
    value = os.environ.get(name, default)
    if value is _env_required:
        raise ImproperlyConfigured(f"Environment variable {name!r} is not set")
    assert isinstance(value, str)
    return value


def get_bool(name, default=_env_required) -> bool:
    return get_str(name, default).lower() in ["yes", "true", "on", "1"]

import json
import os


def env_str(name, default=None, required=False):
    value = os.getenv(name, default)
    if required and (value is None or str(value).strip() == ""):
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def env_bool(name, default=False):
    raw = os.getenv(name)
    if raw is None:
        return default
    return str(raw).strip().lower() in {"1", "true", "yes", "on"}


def env_list(name, default=None):
    raw = os.getenv(name)
    if raw is None:
        return default or []

    value = raw.strip()
    if value == "":
        return []

    if value.startswith("["):
        try:
            parsed = json.loads(value)
            return [str(item).strip() for item in parsed if str(item).strip()]
        except json.JSONDecodeError:
            pass

    return [item.strip() for item in value.split(",") if item.strip()]

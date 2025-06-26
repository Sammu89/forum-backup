from __future__ import annotations

from pathlib import Path

import yaml

# Globals to be populated by init()
BACKUP_ROOT: Path | None = None
BASE_URL: str = ""
BASE_DOMAIN: str = ""
USER_AGENT: str = "ForumMirror/1.0"
workers: int = 4
base_delay: float = 0.5
min_delay: float = 0.1
max_delay: float = 10.0
retry_limit: int = 3

FOLDER_MAPPING: dict[str, str] = {}
IGNORED_PREFIXES: tuple[str, ...] = ()
BLACKLIST_PARAMS: set[str] = set()
AD_HOSTS: set[str] = set()
TRACKER_PATTERNS: list[str] = []
AD_SOURCES: list[dict] = []
MAX_ASSET_KB: int | None = None
SLUG_MAX_LEN: int = 120


def _load_yaml(path: Path) -> dict:
    """
    Load YAML from the given path, return empty dict if missing or invalid.
    """
    try:
        text = path.read_text(encoding="utf-8")
        return yaml.safe_load(text) or {}
    except Exception:
        return {}


def init(backup_root: Path, user_yaml: Path | None = None, forum_url: str = "") -> None:
    """
    Initialize configuration by loading defaults and per-forum overrides.

    - Sets BACKUP_ROOT, BASE_URL, BASE_DOMAIN based on user input.
    - Reads `defaults.yaml` and merges with `user_yaml` if provided.

    Args:
        backup_root: Path to the forum's output folder.
        user_yaml:   Optional Path to a forum-specific YAML file.
        forum_url:   Base URL provided by the user at startup.
    """
    global BACKUP_ROOT, BASE_URL, BASE_DOMAIN, USER_AGENT
    BACKUP_ROOT = backup_root

    # 1. Set BASE_URL and BASE_DOMAIN from CLI input
    from urllib.parse import urlparse

    BASE_URL = forum_url
    BASE_DOMAIN = urlparse(forum_url).netloc.lower()

    # 2. Load defaults and overrides
    defaults_path = Path(__file__).with_name("defaults.yaml")
    defaults = _load_yaml(defaults_path)
    overrides = _load_yaml(Path(user_yaml)) if user_yaml else {}
    cfg = {**defaults, **overrides}

    # 3. Other config values
    fm = cfg.get("folder_mapping", {})
    ip = tuple(cfg.get("ignored_prefixes", []))
    bp = set(cfg.get("blacklist_params", []))
    ah = set(cfg.get("ad_hosts", []))
    tp = cfg.get("tracker_patterns", [])
    srcs = cfg.get("ad_sources", [])
    mb = cfg.get("max_asset_kb")
    sl = cfg.get("slug_max_len", SLUG_MAX_LEN)

    # 4. Update module globals
    globals().update(
        BACKUP_ROOT=BACKUP_ROOT,
        BASE_URL=BASE_URL,
        BASE_DOMAIN=BASE_DOMAIN,
        FOLDER_MAPPING=fm,
        IGNORED_PREFIXES=ip,
        BLACKLIST_PARAMS=bp,
        AD_HOSTS=ah,
        TRACKER_PATTERNS=tp,
        AD_SOURCES=srcs,
        MAX_ASSET_KB=mb,
        SLUG_MAX_LEN=sl,
    )

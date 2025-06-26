from __future__ import annotations
from pathlib import Path
import yaml, os

# Globals to be populated by init()
FOLDER_MAPPING: dict[str, str] = {}
IGNORED_PREFIXES: tuple[str, ...] = ()
BLACKLIST_PARAMS: set[str] = set()
AD_HOSTS: set[str] = set()
TRACKER_PATTERNS: list[str] = []
AD_SOURCES: list[dict] = []
MAX_ASSET_KB: int | None = None
SLUG_MAX_LEN: int = 120
BACKUP_ROOT: Path  # set at runtime

def _load_yaml(path: Path) -> dict:
    """
    Load YAML from the given path, return empty dict if missing or invalid.
    """
    try:
        text = path.read_text(encoding="utf-8")
        return yaml.safe_load(text) or {}
    except Exception:
        return {}

def init(backup_root: Path, user_yaml: Path | None = None) -> None:
    """
    Initialize configuration by loading defaults and per-forum overrides.

    - Reads `defaults.yaml` in this directory.
    - If `user_yaml` is provided, merges overrides on top of defaults.
    - Populates module-level globals accordingly.

    Args:
        backup_root: Path to the forum's output folder (sets BACKUP_ROOT).
        user_yaml: Optional Path to a forum-specific YAML file.
    """
    global BACKUP_ROOT
    BACKUP_ROOT = backup_root
    # 1. load defaults
    defaults_path = Path(__file__).with_name("defaults.yaml")
    defaults = _load_yaml(defaults_path)
    # 2. load forum-specific overrides
    overrides = _load_yaml(Path(user_yaml)) if user_yaml else {}
    # 3. merge
    cfg = {**defaults, **overrides}
    # 4. populate globals
    fm   = cfg.get("folder_mapping", {})
    ip   = tuple(cfg.get("ignored_prefixes", []))
    bp   = set(cfg.get("blacklist_params", []))
    ah   = set(cfg.get("ad_hosts", []))
    tp   = cfg.get("tracker_patterns", [])
    srcs = cfg.get("ad_sources", [])
    mb   = cfg.get("max_asset_kb")
    sl   = cfg.get("slug_max_len", SLUG_MAX_LEN)

    globals().update(
        FOLDER_MAPPING=fm,
        IGNORED_PREFIXES=ip,
        BLACKLIST_PARAMS=bp,
        AD_HOSTS=ah,
        TRACKER_PATTERNS=tp,
        AD_SOURCES=srcs,
        MAX_ASSET_KB=mb,
        SLUG_MAX_LEN=sl,
    )
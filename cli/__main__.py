#!/usr/bin/env python3
"""
Entry-point for Forum-Mirror CLI.
Usage: python -m cli
"""
from __future__ import annotations
import argparse, asyncio, sys, shutil, os, platform, subprocess
from pathlib import Path

# Setup logging early if desired
# from utils.logging import setup
# setup("INFO")

# Local imports (once config is initialized)
import config.settings as settings
from config.settings import init as init_settings
from cli.auth import handle_authentication
from core.fetcher import Fetcher
from core.throttle import ThrottleController
from core.state import State
from crawler.scheduler import run_discovery_phase, run_download_phase
from core.adblock import update_hosts

# ─────────────────────────────────────────────────────────────
# UI Helpers
# ─────────────────────────────────────────────────────────────
def prompt_forum_and_folder(last_url: str | None = None) -> tuple[str, Path]:
    default_url = last_url or "https://sm-portugal.forumeiros.com/"
    forum = input(f"🎯 Target Forum: (default {default_url}): ").strip() or default_url
    if not forum.startswith(("http://","https://")):
        forum = "https://" + forum.lstrip("/")
    forum = forum.rstrip("/")

    domain = forum.split("//",1)[1].split("/",1)[0]
    slug = domain.split(".")[0]
    desktop = Path.home() / "Desktop"
    default_dir = desktop / slug
    out = input(f"📁 Backup Folder: (default {default_dir}): ").strip()
    backup_root = Path(out).expanduser() if out else default_dir
    backup_root.mkdir(parents=True, exist_ok=True)
    return forum, backup_root

# ─────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────
async def main():
    # 1) Prompt for forum URL and backup folder
    forum_url, backup_root = prompt_forum_and_folder()

    # 2) Load config + per-forum settings
    yaml_path = backup_root / "settings.yaml"
    if not yaml_path.exists():
        # create from defaults
        src = Path(__file__).parents[1] / "config" / "defaults.yaml"
        shutil.copy(src, yaml_path)
        print(f"📝 Created settings file at {yaml_path}. Edit as needed.")
        if input("Open it now? (y/N): ").lower() == "y":
            editor = os.environ.get("EDITOR") or ("notepad" if platform.system()=="Windows" else "nano")
            subprocess.call([editor, str(yaml_path)])
    # lock to prevent mid-run edits
    (backup_root / "settings.yaml.lock").write_text("")

    init_settings(backup_root, yaml_path)

    # 3) Load adblock hosts
    await update_hosts(backup_root)

    # 4) Authenticate
    cookies, logged_in = await handle_authentication()
    if not logged_in:
        print("⚠️  Continuing as anonymous user.")

    # 5) Initialize state
    state_file = backup_root / "crawl_state.json"
    cache_file = backup_root / "assets_cache.json"
    state = State(settings, str(state_file), str(cache_file))
    await state.load()

    # 6) Handle resume, reset, status prompts (could add flags later)
    if not state.urls:
        state.add_url("/", "index.html")

    # 7) Setup fetcher & throttle
    throttle = ThrottleController(settings)
    fetcher = Fetcher(settings, throttle, cookies)

    # 8) Run phases
    await run_discovery_phase(settings, state, fetcher)
    await run_download_phase(settings, state, fetcher)

    # 9) Finalize
    await state.save()
    await fetcher.close()
    shutil.copy(state_file, backup_root / "crawl_state_final.json")
    print("🎉 Backup complete! Open index.html in the backup folder to browse offline.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user. Saving state...")
        sys.exit(1)
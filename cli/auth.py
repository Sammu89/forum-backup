"""
Cookie-based authentication flow.
"""

import json
from pathlib import Path
from urllib.parse import urljoin, urlparse

import aiohttp
from bs4 import BeautifulSoup

from utils.files import safe_file_write


async def load_cookies(cookies_file: Path) -> dict:
    """
    Load cookies from the given file path.
    """
    if cookies_file.exists():
        return json.loads(cookies_file.read_text("utf-8"))
    return {}


async def is_logged_in(session: aiohttp.ClientSession, forum_url: str) -> bool:
    """
    Check if the current session is authenticated by looking for a '/profile' link in the path.
    """
    r = await session.get(forum_url)
    html = await r.text()
    soup = BeautifulSoup(html, "html.parser")

    for a in soup.find_all("a", href=True):
        href = urljoin(forum_url, a["href"])
        parsed = urlparse(href)
        # if the path begins with '/profile', we assume we're logged in
        if parsed.path.lower().startswith("/profile"):
            return True

    return False


async def handle_authentication(backup_root: Path, forum_url: str) -> tuple[dict, bool]:
    """
    Returns (cookies, logged_in_flag).
    Uses backup_root to store cookies.json and prompts user to re-enter cookies if not authenticated.

    Args:
        backup_root: Path to the backup folder where cookies.json is stored.
        forum_url:   Base URL of the forum to check authentication.
    """
    cookies_file = backup_root / "cookies.json"
    cookies = await load_cookies(cookies_file)

    async with aiohttp.ClientSession(cookies=cookies) as s:
        ok = await is_logged_in(s, forum_url)
        if ok:
            print("✅ [Cookies] Logged in")
            # save cookies to file in case they've been modified
            await safe_file_write(cookies_file, json.dumps(cookies, indent=2), mode="w")
            return cookies, True

    ans = input("Reconfigure cookies? (y/N): ").strip().lower()
    if ans != "y":
        return cookies, False

    # Cookie wizard
    domain = forum_url.split("//", 1)[1].split("/", 1)[0]
    ck1 = f"fa_{domain.replace('.', '_')}_data"
    ck2 = f"fa_{domain.replace('.', '_')}_sid"
    print("Paste cookie values:")
    new_cookies = {
        ck1: input(f"{ck1}: ").strip(),
        ck2: input(f"{ck2}: ").strip(),
    }
    # save new cookies
    await safe_file_write(cookies_file, json.dumps(new_cookies, indent=2), mode="w")
    return new_cookies, True

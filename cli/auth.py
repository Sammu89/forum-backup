"""
Cookie-based authentication flow.
"""

import json, aiohttp
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup

from utils.files     import safe_file_write
from config.settings import BACKUP_ROOT

COOKIES_FILE = BACKUP_ROOT / "cookies.json"  # overwritten later at runtime

async def load_cookies() -> dict:
    if COOKIES_FILE.exists():
        return json.loads(COOKIES_FILE.read_text("utf-8"))
    return {}

async def is_logged_in(session: aiohttp.ClientSession, forum_url: str) -> bool:
    r = await session.get(forum_url)
    html = await r.text()
    soup = BeautifulSoup(html, "html.parser")
    return any(urljoin(forum_url, a["href"]).split("/",3)[3].startswith("profile")
               for a in soup.find_all("a", href=True))

async def handle_authentication() -> tuple[dict,bool]:
    """
    Returns (cookies, logged_in_flag).
    Prompts user to re-enter cookies if not authenticated.
    """
    import aiohttp, asyncio
    cookies = await load_cookies()
    async with aiohttp.ClientSession(cookies=cookies) as s:
        ok = await is_logged_in(s, BACKUP_ROOT.meta["forum_url"])
        if ok:
            print("✅ [Cookies] Logged in")
            return cookies, True

    ans = input("Reconfigure cookies? (y/N): ").lower()
    if ans != "y":
        return cookies, False

    # wizard
    domain = BACKUP_ROOT.meta["domain"]
    ck1 = f"fa_{domain.replace('.','_')}_data"
    ck2 = f"fa_{domain.replace('.','_')}_sid"
    print("Paste cookie values:")
    cookies = {ck1: input(f"{ck1}: ").strip(),
               ck2: input(f"{ck2}: ").strip()}
    await safe_file_write(COOKIES_FILE, json.dumps(cookies, indent=2), "w")
    return cookies, True

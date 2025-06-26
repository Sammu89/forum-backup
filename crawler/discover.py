"""
Phase-1: discover links and save raw HTML.
"""

from __future__ import annotations
import asyncio, traceback
from urllib.parse import urljoin, urlparse, parse_qsl
from bs4 import BeautifulSoup

from core.pathutils   import url_to_local_path
from core.redirects   import redirects
from core.state       import State, REL, REDIR, STA, RETRY, ERR
from config.settings  import BASE_URL, BASE_DOMAIN, IGNORED_PREFIXES, BLACKLIST_PARAMS
from utils.files      import safe_file_write

def _strip_fragment(url: str) -> str:
    return url.split("#", 1)[0]

def _is_valid_link(href: str) -> bool:
    if href.startswith(("mailto:", "javascript:", "#")):
        return False
    abs_url = urljoin(BASE_URL, href)
    p = urlparse(_strip_fragment(abs_url))
    if p.netloc and p.netloc != BASE_DOMAIN:
        return False
    if any(p.path.startswith(pref) for pref in IGNORED_PREFIXES):
        return False
    if p.query:
        keys = {k for k, _ in parse_qsl(p.query)}
        if keys & BLACKLIST_PARAMS:
            return False
    return True

def _path_plus_query(url: str) -> str:
    p = urlparse(url)
    return p.path + (f"?{p.query}" if p.query else "")

async def handle_redirect(worker_id: int, src_url: str, dst_url: str, state: State) -> bool:
    """
    Record an internal redirect and enqueue the destination.
    """
    src = _path_plus_query(src_url)
    dst = _path_plus_query(dst_url)
    if src == dst:
        return False
    if urlparse(dst_url).netloc and urlparse(dst_url).netloc != BASE_DOMAIN:
        return False
    await redirects.add(src, dst)
    state.mark_redirect_source(src)
    rel = url_to_local_path(dst)
    state.add_url(dst, rel)
    print(f"[Redirect] {src} → {dst}")
    return True

class LinkDiscoverer:
    """
    Worker to fetch raw HTML, save it, discover links.
    """

    def __init__(self, cfg, state: State, fetcher, worker_id: int = 1):
        self.cfg = cfg
        self.state = state
        self.fetcher = fetcher
        self.id = worker_id

    async def run(self):
        idle = 0
        while True:
            path = await self.state.get_next("discover")
            if not path:
                idle += 1
                if idle > 15:
                    break
                await asyncio.sleep(0.5)
                continue
            idle = 0
            await self._process(path)

    async def _process(self, path: str):
        url = urljoin(BASE_URL, path)
        try:
            status, html, final = await self.fetcher.fetch_text(url, allow_redirects=False)
            if status in (301, 302) and await handle_redirect(self.id, url, final, self.state):
                return

            if status != 200 or not html:
                self.state.update_after_fetch(path, False, f"HTTP {status}")
                return

            rel_path = url_to_local_path(path)
            await safe_file_write(rel_path, html)

            count = await self._parse_links(html)
            self.state.mark_discovered(path)
            print(f"[D{self.id}] {path} → +{count} links")

        except Exception:
            traceback.print_exc()
            self.state.update_after_fetch(path, False, "discover error")

    async def _parse_links(self, html: str) -> int:
        soup = BeautifulSoup(html, "html.parser")
        added = 0
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if not _is_valid_link(href):
                continue
            abs_url = urljoin(BASE_URL, href)
            key = _path_plus_query(abs_url)
            rel = url_to_local_path(key)
            self.state.add_url(key, rel)
            added += 1
        return added

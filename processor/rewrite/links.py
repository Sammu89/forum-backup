"""
Rewrite every internal <a href> so it points to the correct local file.
"""

import os
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from config.settings import BASE_DOMAIN, BASE_URL
from core.redirects import redirects
from core.state import REL, State  # index 0 in the compact record


def rewrite_links(soup: BeautifulSoup, cur_file: str, state: State):
    cur_dir = os.path.dirname(cur_file)

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith(("mailto:", "javascript:", "#")):
            continue

        abs_url = urljoin(BASE_URL, href)
        base, *frag = abs_url.split("#", 1)
        netloc = urlparse(base).netloc
        if netloc and netloc != BASE_DOMAIN:
            # external link: leave unchanged
            continue

        key = urlparse(base).path + (
            f"?{urlparse(base).query}" if urlparse(base).query else ""
        )
        key = redirects.resolve(key)

        rec = state.urls.get(key)
        if not rec:
            continue
        target_file = rec[REL]
        rel_link = os.path.relpath(target_file, cur_dir).replace(os.sep, "/")
        if rel_link.endswith("/index.html"):
            rel_link = rel_link[: -len("index.html")] or "./"
        if frag:
            rel_link += "#" + frag[0]
        a["href"] = rel_link

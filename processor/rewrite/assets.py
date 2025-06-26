"""
Download & rewrite <head> and <body>‐level external resources.

Public coroutines
-----------------
* _rewrite_head(soup, page_url, asset_mgr)
* _rewrite_body_assets(soup, page_url, asset_mgr)

Both modify the BeautifulSoup object **in-place** and never return HTML text.
"""

from __future__ import annotations

import asyncio
import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from config.settings import BASE_URL
from core.adblock import is_blocked_host
from downloader.assets import AssetManager

# ───────────────────────── helpers ──────────────────────────
CSS_URL_RE = re.compile(r"url\\(['\\\"]?(.*?)['\\\"]?\\)")
IMG_TAGS = ("img", "input")  # tags that normally carry 'src'


async def _download_and_replace(tag, attr, mgr: AssetManager):
    url = urljoin(BASE_URL, tag[attr])
    rep = await mgr.fetch(url, "images")
    if rep:
        tag[attr] = rep


# ───────────────────────── <head> ───────────────────────────
async def _rewrite_head(soup: BeautifulSoup, page_url: str, mgr: AssetManager):
    """
    Rewrite <head> resources: stylesheets, icons, scripts, inline styles.
    Delegates to helper functions for clarity and testability.
    """
    head = soup.head
    if not head:
        return

    await _handle_link_tags(head, mgr)
    await _handle_head_scripts(head, mgr)
    await _handle_inline_styles(head, page_url, mgr)


async def _handle_link_tags(head: BeautifulSoup, mgr: AssetManager):
    """
    Process <link> tags in <head>: stylesheets, preload/prefetch, icons.
    """
    for link in head.find_all("link", href=True):
        rels = {r.lower() for r in link.get("rel", [])}
        href = urljoin(BASE_URL, link["href"])
        host = urlparse(href).netloc.lower()
        if is_blocked_host(host):
            link.decompose()
            continue

        if "stylesheet" in rels:
            repl = await mgr.fetch(href, "css")
            if repl:
                link["href"] = repl

        elif rels & {"preload", "prefetch"}:
            repl = await mgr.fetch(href, "misc")
            if repl:
                link["href"] = repl

        elif "icon" in rels:
            repl = await mgr.fetch(href, "images")
            if repl:
                link["href"] = repl


async def _handle_head_scripts(head: BeautifulSoup, mgr: AssetManager):
    """
    Process <script src="…"> tags in <head>.
    """
    for script in head.find_all("script", src=True):
        src_abs = urljoin(BASE_URL, script["src"])
        if is_blocked_host(urlparse(src_abs).netloc.lower()):
            script.decompose()
            continue
        repl = await mgr.fetch(src_abs, "js")
        if repl:
            script["src"] = repl


async def _handle_inline_styles(head: BeautifulSoup, page_url: str, mgr: AssetManager):
    """
    Process inline <style> tags: find font URLs and download them.
    """
    for style in head.find_all("style"):
        if not style.string:
            continue
        css = style.string
        for orig in CSS_URL_RE.findall(css):
            abs_u = urljoin(page_url, orig)
            repl = await mgr.fetch(abs_u, "fonts")
            if repl:
                css = css.replace(orig, repl)
        style.string.replace_with(css)


# ────────────────────── <body> & inline ─────────────────────
async def _rewrite_body_assets(soup: BeautifulSoup, page_url: str, mgr: AssetManager):
    # <img>, <input type="image">
    await asyncio.gather(
        *[
            _download_and_replace(tag, "src", mgr)
            for tag in soup.find_all(IMG_TAGS, src=True)
        ]
    )

    # <script src> inside body
    await asyncio.gather(
        *[
            _download_and_replace(script, "src", mgr)
            for script in soup.find_all("script", src=True)
        ]
    )

    # <source srcset="a.jpg 1x, b.jpg 2x">
    for src in soup.find_all("source", srcset=True):
        newset = []
        for part in src["srcset"].split(","):
            url = part.split()[0]
            repl = await mgr.fetch(urljoin(BASE_URL, url), "images")
            if repl:
                newset.append(part.replace(url, repl))
        if newset:
            src["srcset"] = ",".join(newset)

    # inline style="background:url(...)"
    for tag in soup.find_all(style=True):
        style = tag["style"]
        for orig in CSS_URL_RE.findall(style):
            repl = await mgr.fetch(urljoin(page_url, orig), "images")
            if repl:
                style = style.replace(orig, repl)
        tag["style"] = style

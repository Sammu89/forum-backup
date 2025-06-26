"""
AssetManager: download, dedupe & classify assets.
"""

from __future__ import annotations
import hashlib, mimetypes, os
from pathlib import Path
from urllib.parse import urlparse
from config.settings import BACKUP_ROOT, AD_HOSTS, MAX_ASSET_KB
from utils.files       import safe_file_write
from core.state        import State

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico"}

class AssetManager:
    def __init__(self, fetcher, state: State):
        self.fetcher = fetcher
        self.state = state
        self.dst_img = Path(BACKUP_ROOT)/"assets"/"imagens"/"internal"
        self.dst_file= Path(BACKUP_ROOT)/"assets"/"files"/"internal"
        self.dst_ext = Path(BACKUP_ROOT)/"external_files"
        for p in (self.dst_img, self.dst_file, self.dst_ext):
            p.mkdir(parents=True, exist_ok=True)

    async def fetch(self, url: str, kind_hint: str="") -> str | None:
        host = urlparse(url).netloc.lower()
        if host in AD_HOSTS:
            return None
        cached = self.state.get_asset(url)
        if cached:
            return cached
        status, data = await self.fetcher.fetch_bytes(url)
        if status != 200 or data is None:
            return None
        if MAX_ASSET_KB and len(data) > MAX_ASSET_KB * 1024:
            return None
        ext = self._choose_ext(url, kind_hint)
        sub = self.dst_img if ext in IMAGE_EXTS else self.dst_file
        name = hashlib.md5(url.encode()).hexdigest() + ext
        full = sub / name
        await safe_file_write(full, data, mode="wb")
        rel = os.path.relpath(full, BACKUP_ROOT).replace(os.sep, "/")
        self.state.add_asset(url, rel)
        return rel

    def _choose_ext(self, url: str, kind_hint: str) -> str:
        ext = Path(urlparse(url).path).suffix.lower()
        if ext:
            return ext
        if kind_hint == "fonts":
            return ".woff"
        # fallback to mime sniff
        return mimetypes.guess_extension(kind_hint) or ".bin"

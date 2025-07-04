import asyncio
import json
import os
import tempfile

# record indices
REL, REDIR, STA, RETRY, ERR = 0, 1, 2, 3, 4
DEFAULT_REC = ["", 0, "l", 0, ""]


class State:
    """
    Manages two JSON stores:
      - crawl_state.json: mapping URL->compact record
      - assets_cache.json: mapping assetURL->relPath
    Thread-safe via asyncio.Lock.
    """

    def __init__(self, cfg, state_path: str, cache_path: str):
        self.cfg = cfg
        self.state_path = state_path
        self.cache_path = cache_path
        self.urls: dict[str, list] = {}
        self.assets: dict[str, str] = {}
        self._lock = asyncio.Lock()

    async def load(self):
        # load URLs
        try:
            with open(self.state_path, "r", encoding="utf-8") as f:
                self.urls = json.load(f)
        except (json.JSONDecodeError, IOError):
            self.urls = {}
        if not os.path.exists(self.state_path):
            await self.save()
        # load assets
        try:
            with open(self.cache_path, "r", encoding="utf-8") as f:
                self.assets = json.load(f)
        except (json.JSONDecodeError, IOError):
            self.assets = {}
        if not os.path.exists(self.state_path):
            await self.save()

    async def save(self):
        async with self._lock:
            # atomic write of state
            fd, tmp = tempfile.mkstemp(dir=os.path.dirname(self.state_path))
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(self.urls, f, separators=(",", ":"))
            os.replace(tmp, self.state_path)
            # atomic write of assets
            fd2, tmp2 = tempfile.mkstemp(dir=os.path.dirname(self.cache_path))
            with os.fdopen(fd2, "w", encoding="utf-8") as f2:
                json.dump(self.assets, f2, separators=(",", ":"))
            os.replace(tmp2, self.cache_path)

    # ----- URL queue operations -----
    def add_url(self, path: str, rel: str):
        if path in self.urls:
            return
        self.urls[path] = [rel, 0, "l", 0, ""]
        import asyncio

        asyncio.create_task(self.save())

    async def get_next(self, phase: str) -> str | None:
        """
        Reserva e devolve uma URL:
          - discover → 'l' → muda para 'd'
          - download  → 'd' → muda para 'p'
        """
        want = "l" if phase == "discover" else "d"
        async with self._lock:
            for path, rec in self.urls.items():
                if rec[STA] == want:
                    # reserva imediatamente
                    rec[STA] = "d" if phase == "discover" else "p"
                    await self.save()
                    return path
        return None

    def pending_count(self) -> int:
        return sum(1 for v in self.urls.values() if v[STA] in ("l", "d"))

    def mark_discovered(self, path: str):
        rec = self.urls[path]
        rec[STA] = "d"

    def mark_downloaded(self, path: str):
        rec = self.urls[path]
        rec[STA] = "p"

    def mark_redirect_source(self, path: str):
        rec = self.urls[path]
        rec[REDIR] = 1
        rec[STA] = "e"

    def update_after_fetch(self, path: str, success: bool, err: str = ""):
        rec = self.urls[path]
        if success:
            rec[STA] = "d"
        else:
            rec[RETRY] += 1
            rec[ERR] = err
            rec[STA] = "l" if rec[RETRY] < self.cfg.retry_limit else "e"

    # ----- asset cache ops -----
    def get_asset(self, url: str) -> str | None:
        return self.assets.get(url)

    def add_asset(self, url: str, rel: str):
        self.assets[url] = rel

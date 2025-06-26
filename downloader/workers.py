"""
Phase-2: fetch HTML, rewrite via processor, save final.
"""

import asyncio, traceback
from urllib.parse        import urljoin
from core.pathutils      import url_to_local_path
from core.redirects      import redirects
from utils.files         import safe_file_write
from core.state          import State
from processor.orchestrator import process_html
from crawler.discover    import handle_redirect

class DownloadWorker:
    def __init__(self, cfg, state: State, fetcher, wid=1, progress=None):
        self.cfg = cfg
        self.state = state
        self.fetcher = fetcher
        self.id = wid
        self.progress = progress

    async def run(self):
        while True:
            path = await self.state.get_next("download")
            if not path:
                break
            await self._process(path)

    async def _process(self, path: str):
        url = urljoin(self.cfg.base_url, path)
        try:
            status, html, final = await self.fetcher.fetch_text(url)
            if final != url and await handle_redirect(self.id, url, final, self.state):
                return
            if status != 200 or not html:
                self.state.update_after_fetch(path, False, f"HTTP {status}")
                return
            result = await process_html(final, html, self.fetcher, self.state)
            out = url_to_local_path(final)
            await safe_file_write(out, result)
            self.state.mark_downloaded(path)
            if self.progress:
                self.progress.update(1)
        except Exception:
            traceback.print_exc()
            self.state.update_after_fetch(path, False, "download error")

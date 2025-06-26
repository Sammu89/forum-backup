from typing import Optional, Tuple

import aiohttp
from aiohttp import ClientTimeout, TCPConnector


class Fetcher:
    """
    Re-usable aiohttp session with adaptive throttle-awareness and cookies.
    Methods:
      fetch_text(url, allow_redirects=True) -> (status, text|None, final_url)
      fetch_bytes(url)                     -> (status, bytes|None)
      close()                              -> closes session
    """

    def __init__(self, cfg, throttle, cookies: dict):
        self.cfg = cfg
        self.throttle = throttle
        self.cookies = cookies
        self.session: Optional[aiohttp.ClientSession] = None

    async def _ensure_session(self):
        if self.session is None:
            timeout = ClientTimeout(total=30)
            connector = TCPConnector(
                limit=self.cfg.workers * 2,
                limit_per_host=4,
            )
            headers = {"User-Agent": self.cfg.USER_AGENT}
            self.session = aiohttp.ClientSession(
                timeout=timeout,
                connector=connector,
                headers=headers,
                cookies=self.cookies,
            )
            assert self.session is not None

    async def fetch_text(
        self, url: str, allow_redirects: bool = True
    ) -> Tuple[int, Optional[str], str]:
        """
        Fetch text content from URL. Returns (status, text, final_url).
        """
        await self._ensure_session()
        import logging
        logging.info("→ [FETCH-TEXT] %s", url)
        await self.throttle.before_request()
        try:
            async with self.session.get(url, allow_redirects=allow_redirects) as resp:
                status = resp.status
                final = str(resp.url)
                text = await resp.text(errors="ignore")

                # Debug info, to delete
                logging.debug(
                    "GET  %s  -> %s %s  (UA:%s)",
                    url,
                    status,
                    resp.reason,
                    self.session.headers.get("User-Agent"),
                )
                if status >= 400:
                    logging.debug("Response headers: %s", dict(resp.headers))

        except Exception:
            status, text, final = 500, None, url
        finally:
            self.throttle.after_response(status)
        return status, text, final

    async def fetch_bytes(self, url: str) -> Tuple[int, Optional[bytes]]:
        """
        Fetch binary content. Returns (status, data).
        """
        await self._ensure_session()
        import logging
        logging.info("→ [FETCH-TEXT] %s", url)
        await self.throttle.before_request()
        try:
            async with self.session.get(url, allow_redirects=True) as resp:
                status = resp.status
                data = await resp.read()
        except Exception:
            status, data = 500, None
        finally:
            self.throttle.after_response(status)
        return status, data

    async def close(self):
        """Close the aiohttp session."""
        if self.session and not self.session.closed:
            await self.session.close()

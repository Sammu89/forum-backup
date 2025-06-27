from typing import Optional, Tuple

import aiohttp
from aiohttp import ClientTimeout, TCPConnector

# Create module-level #logger
# logger = logging.get#logger(__name__)


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
        # logger.info(f"Fetcher initialized with cookies: {list(cookies.keys())}")
        # logger.info(f"User-Agent available: {hasattr(cfg, 'USER_AGENT')}")
        # if hasattr(cfg, "USER_AGENT"):
        # logger.info(f"User-Agent: {cfg.USER_AGENT}")

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
            # logger.info("aiohttp session created")
            # logger.debug(f"Session headers: {dict(self.session.headers)}")
            # logger.debug("Session cookies:")
            # for cookie in self.session.cookie_jar:
            # logger.debug("  %s = %s", cookie.key, cookie.value)

    async def fetch_text(
        self, url: str, allow_redirects: bool = True
    ) -> Tuple[int, Optional[str], str]:
        """
        Fetch text content from URL. Returns (status, text, final_url).
        """
        await self._ensure_session()

        # logger.info(f"→ [FETCH-TEXT] {url}")
        # logger.debug(f"Request headers: {dict(self.session.headers)}")
        # logger.debug("Request cookies:")
        # for cookie in self.session.cookie_jar:
        # logger.debug("  %s = %s", cookie.key, cookie.value)

        # logger.debug(f"Allow redirects: {allow_redirects}")

        await self.throttle.before_request()

        status = 500  # Default error status
        text = None
        final = url

        try:
            async with self.session.get(url, allow_redirects=allow_redirects) as resp:
                status = resp.status
                final = str(resp.url)

                # logger.info(f"Response: {status} {resp.reason} for {url}")
                # logger.debug(f"Final URL: {final}")
                # logger.debug(f"Response headers: {dict(resp.headers)}")

                if status == 200:
                    text = await resp.text(errors="ignore")
                    # print(f"Response text length: {len(text) if text else 0}")
                    # if text and len(text) < 500:  # Log short responses completely
                    # print(f"Response body: {text}")
                    # elif text:
                    # print(f"Response body preview: {text[:200]}...")
                else:
                    # For non-200 responses, try to get error details
                    error_text = await resp.text(errors="ignore")
                    print(f"HTTP {status} error for {url}")
                    # print(f"Error response headers: {dict(resp.headers)}")
                    # if error_text:
                    # print(f"Error response body: {error_text[:1000]}")

        except aiohttp.ClientError as exc:
            print(f"aiohttp ClientError for {url}: {type(exc).__name__}: {exc}")
            print(f"Exception details: {exc}")
            status, text, final = 500, None, url

        except Exception as exc:
            print(f"Unexpected error fetching {url}: {type(exc).__name__}: {exc}")
            print(f"Exception details: {exc}")
            import traceback

            print(f"Traceback: {traceback.format_exc()}")
            status, text, final = 500, None, url

        finally:
            self.throttle.after_response(status)
            # logger.debug(f"Request completed: {url} -> {status}")

        return status, text, final

    async def fetch_bytes(self, url: str) -> Tuple[int, Optional[bytes]]:
        """
        Fetch binary content. Returns (status, data).
        """
        await self._ensure_session()

        # logger.info(f"→ [FETCH-BYTES] {url}")
        await self.throttle.before_request()

        status = 500
        data = None

        try:
            async with self.session.get(url, allow_redirects=True) as resp:
                status = resp.status
                # logger.info(f"Binary response: {status} {resp.reason} for {url}")

                if status == 200:
                    data = await resp.read()
                    # logger.debug(f"Binary data length: {len(data) if data else 0}")
                else:
                    print(f"HTTP {status} error for binary fetch: {url}")
                    print(f"Response headers: {dict(resp.headers)}")

        except Exception as exc:
            print(f"Error fetching binary {url}: {type(exc).__name__}: {exc}")
            import traceback

            print(f"Traceback: {traceback.format_exc()}")
            status, data = 500, None

        finally:
            self.throttle.after_response(status)

        return status, data

    async def close(self):
        """Close the aiohttp session."""
        if self.session and not self.session.closed:
            await self.session.close()
            # logger.info("aiohttp session closed")

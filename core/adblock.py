import aiohttp, asyncio, time, re
from pathlib import Path
from urllib.parse import urlparse
from config.settings import AD_SOURCES, AD_HOSTS

HOSTLINE_RE = re.compile(r"^[0-9.]+\\s+([^#\\s]+)")

async def _fetch_and_cache(src: dict, cache_file: Path):
    max_age = src.get("cache_days",7) * 86400
    if cache_file.exists() and time.time() - cache_file.stat().st_mtime < max_age:
        return cache_file.read_text("utf-8").splitlines()
    async with aiohttp.ClientSession() as s:
        async with s.get(src["url"]) as r:
            txt = await r.text()
    cache_file.write_text(txt, "utf-8")
    return txt.splitlines()

async def update_hosts(backup_root: Path):
    """
    Download or use cached host files, parse out hostnames,
    merge into AD_HOSTS.
    """
    ad_hosts = set()
    for src in AD_SOURCES:
        fname = "hosts_" + Path(src["url"]).stem + ".txt"
        cache = Path(backup_root) / fname
        lines = await _fetch_and_cache(src, cache)
        for ln in lines:
            m = HOSTLINE_RE.match(ln)
            if m:
                ad_hosts.add(m.group(1).lower())
    AD_HOSTS.update(ad_hosts)

def is_blocked_host(host: str) -> bool:
    return host.lower() in AD_HOSTS

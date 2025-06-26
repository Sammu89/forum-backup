"""
Coordinate HTML rewriting: assets, links, future optimizations.
"""

import asyncio, pathlib
from bs4 import BeautifulSoup

from downloader.assets      import AssetManager
from processor.rewrite.links    import rewrite_links
from processor.rewrite.assets   import _rewrite_head, _rewrite_body_assets
from core.pathutils         import url_to_local_path
from core.state             import State

async def process_html(page_url: str, html: str, fetcher, state: State) -> str:
    """
    • Parse HTML with BeautifulSoup
    • Localise head assets, body assets
    • Rewrite internal anchors
    • (Future) Pass through optimiser hook
    """

    soup = BeautifulSoup(html, "html.parser")
    mgr = AssetManager(fetcher, state)
    # rewrite head
    await _rewrite_head(soup, page_url, mgr)
    # rewrite body
    await _rewrite_body_assets(soup, page_url, mgr)
    # rewrite links
    out_path = pathlib.Path(url_to_local_path(page_url))
    rewrite_links(soup, str(out_path), state)
    # future hook
    from processor.optimize.htmlmin import run as _opt_run
    return _opt_run(str(soup))

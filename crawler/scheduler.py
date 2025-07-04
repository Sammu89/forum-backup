"""
Orchestrate discovery and download phases.
"""

import asyncio


async def run_discovery_phase(cfg, state, fetcher):
    # Import inside the function to avoid circular import
    from crawler.discover import LinkDiscoverer

    tasks = [asyncio.create_task(LinkDiscoverer(cfg, state, fetcher, 1).run())]
    while not tasks[0].done():
        await asyncio.sleep(1)
        if state.pending_count() >= 20 and len(tasks) < cfg.workers:
            n = len(tasks) + 1
            tasks.append(
                asyncio.create_task(LinkDiscoverer(cfg, state, fetcher, n).run())
            )
    await asyncio.gather(*tasks)


async def run_download_phase(cfg, state, fetcher):
    # Import inside the function to avoid circular import
    from downloader.workers import DownloadWorker  # Fixed import path

    workers = [
        DownloadWorker(cfg, state, fetcher, wid=i + 1) for i in range(cfg.workers)
    ]
    await asyncio.gather(*(asyncio.create_task(w.run()) for w in workers))

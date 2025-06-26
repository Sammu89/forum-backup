import asyncio


class ThrottleController:
    """
    Adaptive delay & worker governor.
      - base_delay: start from cfg.base_delay
      - min/max_delay: clamp
      - workers: current parallel worker count
    API:
      before_request()  -> async sleep(current delay)
      after_response(status) -> adjust delay/workers
    """

    def __init__(self, cfg):
        self.cfg = cfg
        self.delay = cfg.base_delay
        self.min = cfg.min_delay
        self.max = cfg.max_delay
        self.workers = cfg.workers
        self._success_count = 0
        self._rtt = self.delay

    async def before_request(self):
        await asyncio.sleep(self.delay)

    def after_response(self, status: int):
        # measure rough RTT adaptation
        # success case
        if 200 <= status < 300:
            self._success_count += 1
            if self._success_count >= 30:
                self.delay = max(self.min, self.delay - 0.1)
                self.workers = min(self.cfg.workers, self.workers + 1)
                self._success_count = 0
        # failure or throttle
        elif status == 429 or status >= 500:
            self.delay = min(self.max, self.delay * 2)
            self.workers = max(1, self.workers // 2)
            self._success_count = 0

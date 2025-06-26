import os, json, asyncio
from typing import Dict, Optional

class RedirectMap:
    """
    Persisted map of src_path->dst_path (redirects.json).
    Thread-safe. resolve() follows chains (visited + depth≤16).
    """

    def __init__(self, filename: str = "redirects.json"):
        self.path = os.path.join(os.getcwd(), filename)
        self.map: Dict[str,str] = {}
        self._lock = asyncio.Lock()
        self._load()

    def _load(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self.map = data
        except:
            self.map = {}

    async def add(self, src: str, dst: str):
        if not src or not dst or src==dst or self.map.get(src)==dst:
            return
        async with self._lock:
            self.map[src] = dst
            await asyncio.to_thread(self._persist)

    def _persist(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.map, f, ensure_ascii=False, indent=2, sort_keys=True)

    def resolve(self, path: str) -> str:
        visited = set()
        cur = path
        depth = 0
        while cur in self.map and cur not in visited and depth<16:
            visited.add(cur)
            cur = self.map[cur]
            depth += 1
        return cur

redirects = RedirectMap()

"""
Atomic file I/O helpers.
"""

from __future__ import annotations
import asyncio, os, tempfile
from pathlib import Path

async def safe_file_write(path: str | Path, data: str | bytes, mode: str = "w") -> bool:
    try:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=p.parent, suffix=".tmp")
        with os.fdopen(fd, mode, encoding=None if "b" in mode else "utf-8") as fh:
            fh.write(data)
        os.replace(tmp, p)
        return True
    except Exception as e:
        print(f"[FileWrite] {e}")
        return False

async def safe_file_read(path: str | Path, mode: str = "r"):
    try:
        return await asyncio.to_thread(Path(path).read_text if "b" not in mode else Path(path).read_bytes)
    except Exception:
        return None
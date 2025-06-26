from pathlib import Path
from urllib.parse import urlparse

from slugify import slugify

from config.settings import BACKUP_ROOT, FOLDER_MAPPING, SLUG_MAX_LEN


def url_to_local_path(url: str) -> str:
    """
    Map a forum path to a local HTML file path under BACKUP_ROOT.
    - lowercase
    - slugify each segment (max SLUG_MAX_LEN)
    - choose folder via FOLDER_MAPPING, fallback to 'misc'
    - on name collision append -dupN
    """
    parsed = urlparse(url)
    route = parsed.path.lstrip("/").lower()
    if not route:
        return str((Path(BACKUP_ROOT) / "index.html").resolve())

    # slugify segments
    segments = route.split("/")
    slugged = [slugify(seg, max_length=SLUG_MAX_LEN) for seg in segments]
    slug = "_".join(slugged)
    if parsed.query:
        q = parsed.query.replace("=", "-").replace("&", "_")
        slug += "_" + slug + q

    # choose folder
    key = segments[0]
    folder = FOLDER_MAPPING.get(key[0] if key else "", "misc")
    out_dir = Path(BACKUP_ROOT) / folder
    out_dir.mkdir(parents=True, exist_ok=True)

    filename = slug + ".html"
    path = out_dir / filename
    # handle collisions
    dup = 1
    while path.exists():
        path = out_dir / f"{slug}-dup{dup}.html"
        dup += 1
    return str(path)

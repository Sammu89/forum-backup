# 🧠 AI-Friendly Code Structure Analysis

*Generated for AI model comprehension and code modification assistance*

## 🌲 Project Structure & Complexity Map

```text
📊 Legend:
🟢 Low Complexity (≤10)  🟡 Medium (11-20)  🔴 High (>20)
📃 Small (<100 lines)   📄 Medium (100-500)  📚 Large (>500)
🏛️ Class  ⚙️ Function  ⚡ Async  🔶 Abstract  📁 Directory

PROJECT_ROOT/
├── 📄 Docstrings.py 🟢 (116 lines, complexity: 0)
│   └── ⚙️ extract_docstrings_from_file 🟢 (line 8, complexity: 5)
│   └── ⚙️ scan_project 🟢 (line 41, complexity: 5)
│   └── ⚙️ generate_markdown 🟡 (line 58, complexity: 6)
│   └── ⚙️ main 🟢 (line 78, complexity: 2)
├── 📁 cli
│   ├── 📄 __main__.py 🟢 (115 lines, complexity: 0)
│   │   └── ⚙️ prompt_forum_and_folder 🟢 (line 37, complexity: 4)
│   │   └── ⚡ main 🟡 (line 57, complexity: 6)
│   └── 📃 auth.py 🟢 (77 lines, complexity: 0)
│       └── ⚡ load_cookies 🟢 (line 15, complexity: 2)
│       └── ⚡ is_logged_in 🟢 (line 24, complexity: 3)
│       └── ⚡ handle_authentication 🟢 (line 42, complexity: 3)
├── 📁 config
│   └── 📃 settings.py 🟢 (88 lines, complexity: 0)
│       └── ⚙️ _load_yaml 🟢 (line 28, complexity: 3)
│       └── ⚙️ init 🟢 (line 39, complexity: 1)
├── 📁 core
│   ├── 📃 adblock.py 🟢 (41 lines, complexity: 0)
│   │   └── ⚡ _fetch_and_cache 🟢 (line 12, complexity: 3)
│   │   └── ⚡ update_hosts 🟢 (line 23, complexity: 4)
│   │   └── ⚙️ is_blocked_host 🟢 (line 40, complexity: 1)
│   ├── 📄 fetcher.py 🟢 (153 lines, complexity: 0)
│   │   ├── 🏛️ Fetcher (line 10, 1 methods)
│   ├── 📃 pathutils.py 🟢 (43 lines, complexity: 0)
│   │   └── ⚙️ url_to_local_path 🟢 (line 9, complexity: 4)
│   ├── 📃 redirects.py 🟢 (51 lines, complexity: 0)
│   │   ├── 🏛️ RedirectMap (line 7, 4 methods)
│   ├── 📃 state.py 🟢 (98 lines, complexity: 0)
│   │   ├── 🏛️ State (line 11, 10 methods)
│   └── 📃 throttle.py 🟢 (40 lines, complexity: 0)
│       ├── 🏛️ ThrottleController (line 4, 2 methods)
├── 📁 crawler
│   ├── 📄 discover.py 🟢 (123 lines, complexity: 0)
│   │   ├── 🏛️ LinkDiscoverer (line 65, 1 methods)
│   │   └── ⚙️ _strip_fragment 🟢 (line 20, complexity: 1)
│   │   └── ⚙️ _is_valid_link 🟡 (line 24, complexity: 7)
│   │   └── ⚙️ _path_plus_query 🟢 (line 40, complexity: 1)
│   │   └── ⚡ handle_redirect 🟢 (line 45, complexity: 4)
│   └── 📃 scheduler.py 🟢 (30 lines, complexity: 0)
│       └── ⚡ run_discovery_phase 🟢 (line 8, complexity: 4)
│       └── ⚡ run_download_phase 🟢 (line 23, complexity: 1)
├── 📁 downloader
│   ├── 📃 assets.py 🟢 (58 lines, complexity: 0)
│   │   ├── 🏛️ AssetManager (line 20, 2 methods)
│   └── 📃 workers.py 🟢 (50 lines, complexity: 0)
│       ├── 🏛️ DownloadWorker (line 14, 1 methods)
├── 📁 processor
│   ├── 📃 orchestrator.py 🟢 (36 lines, complexity: 0)
│   │   └── ⚡ process_html 🟢 (line 16, complexity: 1)
│   └── 📁 rewrite
│       ├── 📄 assets.py 🟢 (145 lines, complexity: 0)
│       │   └── ⚡ _download_and_replace 🟢 (line 29, complexity: 2)
│       │   └── ⚡ _rewrite_head 🟢 (line 37, complexity: 2)
│       │   └── ⚡ _handle_link_tags 🟡 (line 51, complexity: 9)
│       │   └── ⚡ _handle_head_scripts 🟢 (line 79, complexity: 4)
│       │   └── ⚡ _handle_inline_styles 🟢 (line 93, complexity: 5)
│       │   └── ⚡ _rewrite_body_assets 🟡 (line 110, complexity: 8)
│       └── 📃 links.py 🟢 (44 lines, complexity: 0)
│           └── ⚙️ rewrite_links 🟡 (line 15, complexity: 9)
├── 📁 tests
│   ├── 📃 conftest.py 🟢 (10 lines, complexity: 0)
│   │   └── ⚙️ tmp_root 🟢 (line 5, complexity: 1)
│   ├── 📃 test_pathutils.py 🟢 (7 lines, complexity: 0)
│   │   └── ⚙️ test_basic_mapping 🟢 (line 4, complexity: 1)
│   └── 📃 test_redirects.py 🟢 (7 lines, complexity: 0)
│       └── ⚙️ test_chain_resolution 🟢 (line 4, complexity: 1)
└── 📁 utils
    ├── 📃 files.py 🟢 (33 lines, complexity: 0)
    │   └── ⚡ safe_file_write 🟢 (line 13, complexity: 2)
    │   └── ⚡ safe_file_read 🟢 (line 27, complexity: 2)
    └── 📃 logging.py 🟢 (10 lines, complexity: 0)
        └── ⚙️ setup 🟢 (line 5, complexity: 1)
```

## 📊 Comprehensive Project Metrics

- **Python Files Analyzed:** 22
- **Total Lines of Code:** 1,375
- **Classes Defined:** 7
- **Top-Level Functions:** 35
- **Class Methods:** 21
- **Average File Complexity:** 0.0
- **External Dependencies:** 32
- **Most Complex Files:** Docstrings.py, cli/__main__.py, cli/auth.py

## 🔗 Dependency Overview

- **__future__** → Used in 6 files
- **aiohttp** → Used in 3 files
- **argparse** → Used in 1 files
- **ast** → Used in 1 files
- **asyncio** → Used in 8 files
- **bs4** → Used in 5 files
- **cli** → Used in 1 files
- **config** → Used in 7 files
- **core** → Used in 9 files
- **crawler** → Used in 3 files
- **downloader** → Used in 3 files
- **hashlib** → Used in 1 files
- **json** → Used in 3 files
- **logging** → Used in 1 files
- **mimetypes** → Used in 1 files
- **os** → Used in 7 files
- **pathlib** → Used in 8 files
- **platform** → Used in 1 files
- **processor** → Used in 2 files
- **pytest** → Used in 1 files
- **re** → Used in 2 files
- **shutil** → Used in 1 files
- **slugify** → Used in 1 files
- **subprocess** → Used in 1 files
- **sys** → Used in 3 files
- **tempfile** → Used in 2 files
- **time** → Used in 1 files
- **traceback** → Used in 3 files
- **typing** → Used in 2 files
- **urllib** → Used in 8 files
- **utils** → Used in 5 files
- **yaml** → Used in 1 files

---

## 📄 File Analysis: `Docstrings.py`

**Overview:** 116 lines, complexity: 0 🟢

### 📦 Import Analysis

**Direct Imports:**
- `argparse`
- `ast`
- `os`
- `sys`

### 🌐 Global Scope Variables

**Global Variables:**
- `source` = f.read() (line 14)
- `tree` = ast.parse(source, filename=filepath) (line 15)
- `docs` = [] (line 16)
- `obj_type` = 'class' if isinstance(node, ast.ClassDef) else 'function' (line 19)
- `name` = node.name (line 20)
- `lineno` = node.lineno (line 21)
- `doc` = ast.get_docstring(node) or '' (line 22)
- `args` = [arg.arg for arg in node.args.args] (line 25)
- `sig` = f'({', '.join(args)})' (line 26)
- `sig` = '' (line 28)
- `result` = {} (line 46)
- `full` = os.path.join(root, fn) (line 50)
- `rel` = os.path.relpath(full, base_path) (line 51)
- `docs` = extract_docstrings_from_file(full) (line 52)
- `header` = f'- **{item['type']}** `{item['name']}{item['signature']}` (line {item['lineno']})' (line 67)
- `default_output` = f'{os.path.basename(os.getcwd())}_docstrings.md' (line 80)
- `parser` = argparse.ArgumentParser(description='Generate a Markdown map of all Python docstrings in a project.') (line 82)
- `args` = parser.parse_args() (line 100)
- `project_map` = scan_project(args.project_root) (line 102)
- `old_stdout` = sys.stdout (line 106)

### ⚙️ Top-Level Functions

#### `extract_docstrings_from_file(filepath)` 🟢 (lines 8-38, complexity: 5)
**Purpose:** Parse a .py file and return a list of dicts for every
module-level class/function (and async function).
- 🔗 Function calls: `', '.join, ast.get_docstring, ast.parse, ast.walk, doc.strip, docs.append, f.read, isinstance` (+1 more)
- 📊 Local variables: `source, tree, docs, obj_type, name` (+5 more)

#### `scan_project(base_path)` 🟢 (lines 41-55, complexity: 5)
**Purpose:** Walk through base_path and build a map:
  { relative_filepath: [ {type,name,signature,lineno,docstring}, ... ], ... }
- 🔗 Function calls: `extract_docstrings_from_file, fn.endswith, os.path.join, os.path.relpath, os.walk`
- 📊 Local variables: `result, full, rel, docs`

#### `generate_markdown(project_map, title)` 🟡 (lines 58-75, complexity: 6)
**Purpose:** Given the map from scan_project, print Markdown to stdout.
- 🔗 Function calls: `item['docstring'].splitlines, print, sorted`
- 📊 Local variables: `header`

#### `main()` 🟢 (lines 78-112, complexity: 2)
- 🔗 Function calls: `argparse.ArgumentParser, generate_markdown, open, os.getcwd, os.path.basename, parser.add_argument, parser.parse_args, print` (+1 more)
- 📊 Local variables: `default_output, parser, args, project_map, old_stdout`

### 🌐 External API Usage

- **', '**: `', '.join`
- **argparse**: `argparse.ArgumentParser`
- **ast**: `ast.get_docstring, ast.parse, ast.walk`
- **doc**: `doc.strip`
- **docs**: `docs.append`
- **f**: `f.read`
- **fn**: `fn.endswith`
- **item['docstring']**: `item['docstring'].splitlines`
- **os**: `os.getcwd, os.path.basename, os.path.join, os.path.relpath, os.walk`
- **parser**: `parser.add_argument, parser.parse_args`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `extract_docstrings_from_file, generate_markdown, main, scan_project`

**External API calls:** `', '.join, argparse.ArgumentParser, ast.get_docstring, ast.parse, ast.walk, doc.strip, docs.append, f.read, fn.endswith, item['docstring'].splitlines, os.getcwd, os.path.basename, os.path.join, os.path.relpath, os.walk`
 (+2 more)

**Built-in functions:** `isinstance, open, print, sorted`

### 🤖 AI Modification Hints

- **Documentation needed:** Functions `main` lack docstrings

---

## 📄 File Analysis: `cli/__main__.py`

**Overview:** 115 lines, complexity: 0 🟢

**File Purpose:** Entry-point for Forum-Mirror CLI.
Usage: python -m cli

### 📦 Import Analysis

**Direct Imports:**
- `asyncio`
- `os`
- `platform`
- `settings`
- `shutil`
- `subprocess`
- `sys`

**From Imports:**
- `from __future__ import annotations`
- `from cli.auth import handle_authentication`
- `from config.settings import init_settings`
- `from core.adblock import update_hosts`
- `from core.fetcher import Fetcher`
- `from core.state import State`
- `from core.throttle import ThrottleController`
- `from crawler.scheduler import run_discovery_phase, run_download_phase`
- `from pathlib import Path`
- `from utils.logging import log_setup`

### 🌐 Global Scope Variables

**Global Variables:**
- `default_url` = last_url or 'https://sm-portugal.forumeiros.com/' (line 38)
- `forum` = input(f'🎯 Target Forum: (default {default_url}): ').strip() or default_url (line 39)
- `forum` = 'https://' + forum.lstrip('/') (line 41)
- `forum` = forum.rstrip('/') (line 42)
- `domain` = forum.split('//', 1)[1].split('/', 1)[0] (line 44)
- `slug` = domain.split('.')[0] (line 45)
- `desktop` = Path.home() / 'Desktop' (line 46)
- `default_dir` = desktop / slug (line 47)
- `out` = input(f'📁 Backup Folder: (default {default_dir}): ').strip() (line 48)
- `backup_root` = Path(out).expanduser() if out else default_dir (line 49)
- `yaml_path` = backup_root / 'settings.yaml' (line 62)
- `src` = Path(__file__).parents[1] / 'config' / 'defaults.yaml' (line 65)
- `editor` = os.environ.get('EDITOR') or ('notepad' if platform.system() == 'Windows' else 'nano') (line 69)
- `state_file` = backup_root / 'crawl_state.json' (line 86)
- `cache_file` = backup_root / 'assets_cache.json' (line 87)
- `state` = State(settings, str(state_file), str(cache_file)) (line 88)
- `throttle` = ThrottleController(settings) (line 96)
- `fetcher` = Fetcher(settings, throttle, cookies) (line 97)

### ⚙️ Top-Level Functions

#### `prompt_forum_and_folder(last_url: str | None) -> tuple[str, Path]` 🟢 (lines 37-51, complexity: 4)
- 🔗 Function calls: `Path, Path(out).expanduser, Path.home, backup_root.mkdir, domain.split, forum.lstrip, forum.rstrip, forum.split` (+5 more)
- 📊 Local variables: `default_url, forum, forum, forum, domain` (+5 more)

#### `async main()` 🟡 (lines 57-107, complexity: 6)
- 🔗 Function calls: `(backup_root / 'settings.yaml.lock').write_text, Fetcher, Path, State, ThrottleController, fetcher.close, handle_authentication, init_settings` (+16 more)
- 📊 Local variables: `yaml_path, src, editor, state_file, cache_file` (+3 more)

### 🌐 External API Usage

- **(backup_root / 'settings**: `(backup_root / 'settings.yaml.lock').write_text`
- **Path**: `Path.home`
- **Path(out)**: `Path(out).expanduser`
- **asyncio**: `asyncio.run`
- **backup_root**: `backup_root.mkdir`
- **domain**: `domain.split`
- **fetcher**: `fetcher.close`
- **forum**: `forum.lstrip, forum.rstrip, forum.split, forum.split('//', 1)[1].split, forum.startswith`
- **input('Open it now? (y/N): ')**: `input('Open it now? (y/N): ').lower`
- **input(f'🎯 Target Forum: (default {default_url}): ')**: `input(f'🎯 Target Forum: (default {default_url}): ').strip`
- **input(f'📁 Backup Folder: (default {default_dir}): ')**: `input(f'📁 Backup Folder: (default {default_dir}): ').strip`
- **os**: `os.environ.get`
- **platform**: `platform.system`
- **shutil**: `shutil.copy`
- **state**: `state.add_url, state.load, state.save`
- **subprocess**: `subprocess.call`
- **sys**: `sys.exit`
- **yaml_path**: `yaml_path.exists`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `Fetcher, Path, State, ThrottleController, handle_authentication, init_settings, input, log_setup, main, prompt_forum_and_folder, run_discovery_phase, run_download_phase, update_hosts`

**External API calls:** `(backup_root / 'settings.yaml.lock').write_text, Path(out).expanduser, Path.home, asyncio.run, backup_root.mkdir, domain.split, fetcher.close, forum.lstrip, forum.rstrip, forum.split, forum.split('//', 1)[1].split, forum.startswith, input('Open it now? (y/N): ').lower, input(f'🎯 Target Forum: (default {default_url}): ').strip, input(f'📁 Backup Folder: (default {default_dir}): ').strip`
 (+9 more)

**Built-in functions:** `print, str`

### 🤖 AI Modification Hints

- **Documentation needed:** Functions `prompt_forum_and_folder, main` lack docstrings

---

## 📄 File Analysis: `cli/auth.py`

**Overview:** 77 lines, complexity: 0 🟢

**File Purpose:** Cookie-based authentication flow.

### 📦 Import Analysis

**Direct Imports:**
- `aiohttp`
- `json`

**From Imports:**
- `from bs4 import BeautifulSoup`
- `from pathlib import Path`
- `from urllib.parse import urljoin, urlparse`
- `from utils.files import safe_file_write`

### 🌐 Global Scope Variables

**Global Variables:**
- `r` = await session.get(forum_url) (line 28)
- `html` = await r.text() (line 29)
- `soup` = BeautifulSoup(html, 'html.parser') (line 30)
- `href` = urljoin(forum_url, a['href']) (line 33)
- `parsed` = urlparse(href) (line 34)
- `cookies_file` = backup_root / 'cookies.json' (line 51)
- `cookies` = await load_cookies(cookies_file) (line 52)
- `ok` = await is_logged_in(s, forum_url) (line 55)
- `ans` = input('Reconfigure cookies? (y/N): ').strip().lower() (line 62)
- `domain` = forum_url.split('//', 1)[1].split('/', 1)[0] (line 67)
- `ck1` = f'fa_{domain.replace('.', '_')}_data' (line 68)
- `ck2` = f'fa_{domain.replace('.', '_')}_sid' (line 69)
- `new_cookies` = {ck1: input(f'{ck1}: ').strip(), ck2: input(f'{ck2}: ').strip()} (line 71)

### ⚙️ Top-Level Functions

#### `async load_cookies(cookies_file: Path) -> dict` 🟢 (lines 15-21, complexity: 2)
**Purpose:** Load cookies from the given file path.
- 🔗 Function calls: `cookies_file.exists, cookies_file.read_text, json.loads`

#### `async is_logged_in(session: aiohttp.ClientSession, forum_url: str) -> bool` 🟢 (lines 24-39, complexity: 3)
**Purpose:** Check if the current session is authenticated by looking for a '/profile' link in the path.
- 🔗 Function calls: `BeautifulSoup, parsed.path.lower, parsed.path.lower().startswith, r.text, session.get, soup.find_all, urljoin, urlparse`
- 📊 Local variables: `r, html, soup, href, parsed`

#### `async handle_authentication(backup_root: Path, forum_url: str) -> tuple[dict, bool]` 🟢 (lines 42-77, complexity: 3)
**Purpose:** Returns (cookies, logged_in_flag).
Uses backup_root to store cookies.json and prompts user to re-enter cookies if not authenticated.

Args:
    backup...
- 🔗 Function calls: `aiohttp.ClientSession, domain.replace, forum_url.split, forum_url.split('//', 1)[1].split, input, input('Reconfigure cookies? (y/N): ').strip, input('Reconfigure cookies? (y/N): ').strip().lower, input(f'{ck1}: ').strip` (+6 more)
- 📊 Local variables: `cookies_file, cookies, ok, ans, domain` (+3 more)

### 🌐 External API Usage

- **aiohttp**: `aiohttp.ClientSession`
- **cookies_file**: `cookies_file.exists, cookies_file.read_text`
- **domain**: `domain.replace`
- **forum_url**: `forum_url.split, forum_url.split('//', 1)[1].split`
- **input('Reconfigure cookies? (y/N): ')**: `input('Reconfigure cookies? (y/N): ').strip, input('Reconfigure cookies? (y/N): ').strip().lower`
- **input(f'{ck1}: ')**: `input(f'{ck1}: ').strip`
- **input(f'{ck2}: ')**: `input(f'{ck2}: ').strip`
- **json**: `json.dumps, json.loads`
- **parsed**: `parsed.path.lower, parsed.path.lower().startswith`
- **r**: `r.text`
- **session**: `session.get`
- **soup**: `soup.find_all`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `BeautifulSoup, input, is_logged_in, load_cookies, safe_file_write, urljoin, urlparse`

**External API calls:** `aiohttp.ClientSession, cookies_file.exists, cookies_file.read_text, domain.replace, forum_url.split, forum_url.split('//', 1)[1].split, input('Reconfigure cookies? (y/N): ').strip, input('Reconfigure cookies? (y/N): ').strip().lower, input(f'{ck1}: ').strip, input(f'{ck2}: ').strip, json.dumps, json.loads, parsed.path.lower, parsed.path.lower().startswith, r.text`
 (+2 more)

**Built-in functions:** `print`

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `config/settings.py`

**Overview:** 88 lines, complexity: 0 🟢

### 📦 Import Analysis

**Direct Imports:**
- `yaml`

**From Imports:**
- `from __future__ import annotations`
- `from pathlib import Path`
- `from urllib.parse import urlparse, urlparse`

### 🌐 Global Scope Variables

**Constants:**
- `BACKUP_ROOT` = backup_root (line 52)
- `BASE_URL` = forum_url (line 57)
- `BASE_DOMAIN` = urlparse(forum_url).netloc.lower() (line 58)
- `BACKUP_ROOT` = backup_root (line 52)
- `BASE_URL` = forum_url (line 57)
- `BASE_DOMAIN` = urlparse(forum_url).netloc.lower() (line 58)

**Global Variables:**
- `text` = path.read_text(encoding='utf-8') (line 33)
- `defaults_path` = Path(__file__).with_name('defaults.yaml') (line 61)
- `defaults` = _load_yaml(defaults_path) (line 62)
- `overrides` = _load_yaml(Path(user_yaml)) if user_yaml else {} (line 63)
- `cfg` = {**defaults, **overrides} (line 64)
- `fm` = cfg.get('folder_mapping', {}) (line 67)
- `ip` = tuple(cfg.get('ignored_prefixes', [])) (line 68)
- `bp` = set(cfg.get('blacklist_params', [])) (line 69)
- `ah` = set(cfg.get('ad_hosts', [])) (line 70)
- `tp` = cfg.get('tracker_patterns', []) (line 71)
- `srcs` = cfg.get('ad_sources', []) (line 72)
- `mb` = cfg.get('max_asset_kb') (line 73)
- `sl` = cfg.get('slug_max_len', SLUG_MAX_LEN) (line 74)

### ⚙️ Top-Level Functions

#### `_load_yaml(path: Path) -> dict` 🟢 (lines 28-36, complexity: 3)
**Purpose:** Load YAML from the given path, return empty dict if missing or invalid.
- 🔗 Function calls: `path.read_text, yaml.safe_load`
- 📊 Local variables: `text`

#### `init(backup_root: Path, user_yaml: Path | None, forum_url: str) -> None` 🟢 (lines 39-88, complexity: 1)
**Purpose:** Initialize configuration by loading defaults and per-forum overrides.

- Sets BACKUP_ROOT, BASE_URL, BASE_DOMAIN based on user input.
- Reads `default...
- 🔗 Function calls: `Path, Path(__file__).with_name, _load_yaml, cfg.get, globals, globals().update, set, tuple` (+2 more)
- 📊 Local variables: `defaults_path, defaults, overrides, cfg, fm` (+7 more)

### 🌐 External API Usage

- **Path(__file__)**: `Path(__file__).with_name`
- **cfg**: `cfg.get`
- **globals()**: `globals().update`
- **path**: `path.read_text`
- **urlparse(forum_url)**: `urlparse(forum_url).netloc.lower`
- **yaml**: `yaml.safe_load`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `Path, _load_yaml, globals, urlparse`

**External API calls:** `Path(__file__).with_name, cfg.get, globals().update, path.read_text, urlparse(forum_url).netloc.lower, yaml.safe_load`

**Built-in functions:** `set, tuple`

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `core/adblock.py`

**Overview:** 41 lines, complexity: 0 🟢

### 📦 Import Analysis

**Direct Imports:**
- `aiohttp`
- `re`
- `time`

**From Imports:**
- `from config.settings import AD_HOSTS, AD_SOURCES`
- `from pathlib import Path`

### 🌐 Global Scope Variables

**Constants:**
- `HOSTLINE_RE` = re.compile('^[0-9.]+\\\\s+([^#\\\\s]+)') (line 9)

**Global Variables:**
- `max_age` = src.get('cache_days', 7) * 86400 (line 13)
- `txt` = await r.text() (line 18)
- `ad_hosts` = set() (line 28)
- `fname` = 'hosts_' + Path(src['url']).stem + '.txt' (line 30)
- `cache` = Path(backup_root) / fname (line 31)
- `lines` = await _fetch_and_cache(src, cache) (line 32)
- `m` = HOSTLINE_RE.match(ln) (line 34)

### ⚙️ Top-Level Functions

#### `async _fetch_and_cache(src: dict, cache_file: Path)` 🟢 (lines 12-20, complexity: 3)
- 🔗 Function calls: `aiohttp.ClientSession, cache_file.exists, cache_file.read_text, cache_file.read_text('utf-8').splitlines, cache_file.stat, cache_file.write_text, r.text, s.get` (+3 more)
- 📊 Local variables: `max_age, txt`

#### `async update_hosts(backup_root: Path)` 🟢 (lines 23-37, complexity: 4)
**Purpose:** Download or use cached host files, parse out hostnames,
merge into AD_HOSTS.
- 🔗 Function calls: `AD_HOSTS.update, HOSTLINE_RE.match, Path, _fetch_and_cache, ad_hosts.add, m.group, m.group(1).lower, set`
- 📊 Local variables: `ad_hosts, fname, cache, lines, m`

#### `is_blocked_host(host: str) -> bool` 🟢 (lines 40-41, complexity: 1)
- 🔗 Function calls: `host.lower`

### 🌐 External API Usage

- **AD_HOSTS**: `AD_HOSTS.update`
- **HOSTLINE_RE**: `HOSTLINE_RE.match`
- **ad_hosts**: `ad_hosts.add`
- **aiohttp**: `aiohttp.ClientSession`
- **cache_file**: `cache_file.exists, cache_file.read_text, cache_file.read_text('utf-8').splitlines, cache_file.stat, cache_file.write_text`
- **host**: `host.lower`
- **m**: `m.group, m.group(1).lower`
- **r**: `r.text`
- **re**: `re.compile`
- **s**: `s.get`
- **src**: `src.get`
- **time**: `time.time`
- **txt**: `txt.splitlines`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `Path, _fetch_and_cache`

**External API calls:** `AD_HOSTS.update, HOSTLINE_RE.match, ad_hosts.add, aiohttp.ClientSession, cache_file.exists, cache_file.read_text, cache_file.read_text('utf-8').splitlines, cache_file.stat, cache_file.write_text, host.lower, m.group, m.group(1).lower, r.text, re.compile, s.get`
 (+3 more)

**Built-in functions:** `set`

### 🤖 AI Modification Hints

- **Documentation needed:** Functions `_fetch_and_cache, is_blocked_host` lack docstrings

---

## 📄 File Analysis: `core/fetcher.py`

**Overview:** 153 lines, complexity: 0 🟢

### 📦 Import Analysis

**Direct Imports:**
- `aiohttp`
- `traceback`

**From Imports:**
- `from aiohttp import ClientTimeout, TCPConnector`
- `from typing import Optional, Tuple`

### 🏛️ Class Definitions

#### `Fetcher` - lines 10-153
**Purpose:** Re-usable aiohttp session with adaptive throttle-awareness and cookies.
Methods:
  fetch_text(url, allow_redirects=True) -> (status, text|None, final_...

**Methods:**
- `__init__(self, cfg, throttle, cookies: dict)` 🟢 (lines 19-23, complexity: 1)

### 🌐 External API Usage

- **aiohttp**: `aiohttp.ClientSession`
- **resp**: `resp.read, resp.text`
- **traceback**: `traceback.format_exc`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `ClientTimeout, TCPConnector, self._ensure_session, self.session.close, self.session.get, self.throttle.after_response, self.throttle.before_request`

**External API calls:** `aiohttp.ClientSession, resp.read, resp.text, traceback.format_exc`

**Built-in functions:** `dict, print, str, type`

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `core/pathutils.py`

**Overview:** 43 lines, complexity: 0 🟢

### 📦 Import Analysis

**From Imports:**
- `from config.settings import BACKUP_ROOT, FOLDER_MAPPING, SLUG_MAX_LEN`
- `from pathlib import Path`
- `from slugify import slugify`
- `from urllib.parse import urlparse`

### 🌐 Global Scope Variables

**Global Variables:**
- `parsed` = urlparse(url) (line 17)
- `route` = parsed.path.lstrip('/').lower() (line 18)
- `segments` = route.split('/') (line 23)
- `slugged` = [slugify(seg, max_length=SLUG_MAX_LEN) for seg in segments] (line 24)
- `slug` = '_'.join(slugged) (line 25)
- `q` = parsed.query.replace('=', '-').replace('&', '_') (line 27)
- `key` = segments[0] (line 31)
- `folder` = FOLDER_MAPPING.get(key[0] if key else '', 'misc') (line 32)
- `out_dir` = Path(BACKUP_ROOT) / folder (line 33)
- `filename` = slug + '.html' (line 36)
- `path` = out_dir / filename (line 37)
- `dup` = 1 (line 39)
- `path` = out_dir / f'{slug}-dup{dup}.html' (line 41)

### ⚙️ Top-Level Functions

#### `url_to_local_path(url: str) -> str` 🟢 (lines 9-43, complexity: 4)
**Purpose:** Map a forum path to a local HTML file path under BACKUP_ROOT.
- lowercase
- slugify each segment (max SLUG_MAX_LEN)
- choose folder via FOLDER_MAPPING...
- 🔗 Function calls: `'_'.join, (Path(BACKUP_ROOT) / 'index.html').resolve, FOLDER_MAPPING.get, Path, out_dir.mkdir, parsed.path.lstrip, parsed.path.lstrip('/').lower, parsed.query.replace` (+6 more)
- 📊 Local variables: `parsed, route, segments, slugged, slug` (+8 more)

### 🌐 External API Usage

- **'_'**: `'_'.join`
- **(Path(BACKUP_ROOT) / 'index**: `(Path(BACKUP_ROOT) / 'index.html').resolve`
- **FOLDER_MAPPING**: `FOLDER_MAPPING.get`
- **out_dir**: `out_dir.mkdir`
- **parsed**: `parsed.path.lstrip, parsed.path.lstrip('/').lower, parsed.query.replace, parsed.query.replace('=', '-').replace`
- **path**: `path.exists`
- **route**: `route.split`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `Path, slugify, urlparse`

**External API calls:** `'_'.join, (Path(BACKUP_ROOT) / 'index.html').resolve, FOLDER_MAPPING.get, out_dir.mkdir, parsed.path.lstrip, parsed.path.lstrip('/').lower, parsed.query.replace, parsed.query.replace('=', '-').replace, path.exists, route.split`

**Built-in functions:** `str`

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `core/redirects.py`

**Overview:** 51 lines, complexity: 0 🟢

### 📦 Import Analysis

**Direct Imports:**
- `asyncio`
- `json`
- `os`

**From Imports:**
- `from typing import Dict`

### 🌐 Global Scope Variables

**Global Variables:**
- `redirects` = RedirectMap() (line 51)

### 🏛️ Class Definitions

#### `RedirectMap` - lines 7-48
**Purpose:** Persisted map of src_path->dst_path (redirects.json).
Thread-safe. resolve() follows chains (visited + depth≤16).

**Methods:**
- `__init__(self, filename: str)` 🟢 (lines 13-17, complexity: 1)
  - 🔗 Calls: `asyncio.Lock, os.getcwd, os.path.join, self._load`
- `_load(self)` 🟢 (lines 19-26, complexity: 3)
  - 🔗 Calls: `isinstance, json.load, open`
- `_persist(self)` 🟢 (lines 35-38, complexity: 1)
  - 🔗 Calls: `json.dump, open, os.makedirs, os.path.dirname`
- `resolve(self, path: str) -> str` 🟢 (lines 40-48, complexity: 3)
  - 🔗 Calls: `set, visited.add`

### 🌐 External API Usage

- **asyncio**: `asyncio.Lock, asyncio.to_thread`
- **json**: `json.dump, json.load`
- **os**: `os.getcwd, os.makedirs, os.path.dirname, os.path.join`
- **visited**: `visited.add`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `RedirectMap, self._load, self.map.get`

**External API calls:** `asyncio.Lock, asyncio.to_thread, json.dump, json.load, os.getcwd, os.makedirs, os.path.dirname, os.path.join, visited.add`

**Built-in functions:** `isinstance, open, set`

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `core/state.py`

**Overview:** 98 lines, complexity: 0 🟢

### 📦 Import Analysis

**Direct Imports:**
- `asyncio`
- `json`
- `os`
- `tempfile`

### 🌐 Global Scope Variables

**Constants:**
- `DEFAULT_REC` = ['', 0, 'l', 0, ''] (line 8)

### 🏛️ Class Definitions

#### `State` - lines 11-98
**Purpose:** Manages two JSON stores:
  - crawl_state.json: mapping URL->compact record
  - assets_cache.json: mapping assetURL->relPath
Thread-safe via asyncio.Lo...

**Methods:**
- `__init__(self, cfg, state_path: str, cache_path: str)` 🟢 (lines 19-25, complexity: 1)
  - 🔗 Calls: `asyncio.Lock`
- `add_url(self, path: str, rel: str)` 🟢 (lines 55-58, complexity: 2)
- `get_next(self, phase: str) -> str | None` 🟢 (lines 60-66, complexity: 3)
  - 🔗 Calls: `self.urls.items`
- `pending_count(self) -> int` 🟢 (lines 68-69, complexity: 1)
  - 🔗 Calls: `self.urls.values, sum`
- `mark_discovered(self, path: str)` 🟢 (lines 71-73, complexity: 1)
- `mark_downloaded(self, path: str)` 🟢 (lines 75-77, complexity: 1)
- `mark_redirect_source(self, path: str)` 🟢 (lines 79-82, complexity: 1)
- `update_after_fetch(self, path: str, success: bool, err: str)` 🟢 (lines 84-91, complexity: 2)
- `get_asset(self, url: str) -> str | None` 🟢 (lines 94-95, complexity: 1)
  - 🔗 Calls: `self.assets.get`
- `add_asset(self, url: str, rel: str)` 🟢 (lines 97-98, complexity: 1)

### 🌐 External API Usage

- **asyncio**: `asyncio.Lock`
- **json**: `json.dump, json.load`
- **os**: `os.fdopen, os.path.dirname, os.replace`
- **tempfile**: `tempfile.mkstemp`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `self.assets.get, self.urls.items, self.urls.values`

**External API calls:** `asyncio.Lock, json.dump, json.load, os.fdopen, os.path.dirname, os.replace, tempfile.mkstemp`

**Built-in functions:** `open, sum`

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `core/throttle.py`

**Overview:** 40 lines, complexity: 0 🟢

### 📦 Import Analysis

**Direct Imports:**
- `asyncio`

### 🏛️ Class Definitions

#### `ThrottleController` - lines 4-40
**Purpose:** Adaptive delay & worker governor.
  - base_delay: start from cfg.base_delay
  - min/max_delay: clamp
  - workers: current parallel worker count
API:
 ...

**Methods:**
- `__init__(self, cfg)` 🟢 (lines 15-22, complexity: 1)
- `after_response(self, status: int)` 🟢 (lines 27-40, complexity: 5)
  - 🔗 Calls: `max, min`

### 🌐 External API Usage

- **asyncio**: `asyncio.sleep`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**External API calls:** `asyncio.sleep`

**Built-in functions:** `max, min`

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `crawler/discover.py`

**Overview:** 123 lines, complexity: 0 🟢

**File Purpose:** Phase-1: discover links and save raw HTML.

### 📦 Import Analysis

**Direct Imports:**
- `asyncio`
- `traceback`

**From Imports:**
- `from __future__ import annotations`
- `from bs4 import BeautifulSoup`
- `from config.settings import BASE_DOMAIN, BASE_URL, BLACKLIST_PARAMS, IGNORED_PREFIXES`
- `from core.pathutils import url_to_local_path`
- `from core.redirects import redirects`
- `from core.state import State`
- `from urllib.parse import parse_qsl, urljoin, urlparse`
- `from utils.files import safe_file_write`

### 🌐 Global Scope Variables

**Global Variables:**
- `abs_url` = urljoin(BASE_URL, href) (line 27)
- `p` = urlparse(_strip_fragment(abs_url)) (line 28)
- `keys` = {k for k, _ in parse_qsl(p.query)} (line 34)
- `p` = urlparse(url) (line 41)
- `src` = _path_plus_query(src_url) (line 51)
- `dst` = _path_plus_query(dst_url) (line 52)
- `rel` = url_to_local_path(dst) (line 59)

### 🏛️ Class Definitions

#### `LinkDiscoverer` - lines 65-123
**Purpose:** Worker to fetch raw HTML, save it, discover links.

**Methods:**
- `__init__(self, cfg, state: State, fetcher, worker_id: int)` 🟢 (lines 70-74, complexity: 1)

### ⚙️ Top-Level Functions

#### `_strip_fragment(url: str) -> str` 🟢 (lines 20-21, complexity: 1)
- 🔗 Function calls: `url.split`

#### `_is_valid_link(href: str) -> bool` 🟡 (lines 24-37, complexity: 7)
- 🔗 Function calls: `_strip_fragment, any, href.startswith, p.path.startswith, parse_qsl, urljoin, urlparse`
- 📊 Local variables: `abs_url, p, keys`

#### `_path_plus_query(url: str) -> str` 🟢 (lines 40-42, complexity: 1)
- 🔗 Function calls: `urlparse`
- 📊 Local variables: `p`

#### `async handle_redirect(worker_id: int, src_url: str, dst_url: str, state: State) -> bool` 🟢 (lines 45-62, complexity: 4)
**Purpose:** Record an internal redirect and enqueue the destination.
- 🔗 Function calls: `_path_plus_query, print, redirects.add, state.add_url, state.mark_redirect_source, url_to_local_path, urlparse`
- 📊 Local variables: `src, dst, rel`

### 🌐 External API Usage

- **asyncio**: `asyncio.sleep`
- **href**: `href.startswith`
- **p**: `p.path.startswith`
- **redirects**: `redirects.add`
- **soup**: `soup.find_all`
- **state**: `state.add_url, state.mark_redirect_source`
- **traceback**: `traceback.print_exc`
- **url**: `url.split`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `BeautifulSoup, _is_valid_link, _path_plus_query, _strip_fragment, handle_redirect, parse_qsl, safe_file_write, self._parse_links, self._process, self.fetcher.fetch_text, self.state.add_url, self.state.get_next, self.state.mark_discovered, self.state.update_after_fetch, url_to_local_path`
 (+2 more)

**External API calls:** `asyncio.sleep, href.startswith, p.path.startswith, redirects.add, soup.find_all, state.add_url, state.mark_redirect_source, traceback.print_exc, url.split`

**Built-in functions:** `any, print`

### 🤖 AI Modification Hints

- **Documentation needed:** Functions `_strip_fragment, _is_valid_link, _path_plus_query` lack docstrings

---

## 📄 File Analysis: `crawler/scheduler.py`

**Overview:** 30 lines, complexity: 0 🟢

**File Purpose:** Orchestrate discovery and download phases.

### 📦 Import Analysis

**Direct Imports:**
- `asyncio`

**From Imports:**
- `from crawler.discover import LinkDiscoverer, LinkDiscoverer`
- `from downloader.workers import DownloadWorker, DownloadWorker`

### 🌐 Global Scope Variables

**Global Variables:**
- `tasks` = [asyncio.create_task(LinkDiscoverer(cfg, state, fetcher, 1).run())] (line 12)
- `n` = len(tasks) + 1 (line 16)
- `workers` = [DownloadWorker(cfg, state, fetcher, wid=i + 1) for i in range(cfg.workers)] (line 27)

### ⚙️ Top-Level Functions

#### `async run_discovery_phase(cfg, state, fetcher)` 🟢 (lines 8-20, complexity: 4)
- 🔗 Function calls: `LinkDiscoverer, LinkDiscoverer(cfg, state, fetcher, 1).run, LinkDiscoverer(cfg, state, fetcher, n).run, asyncio.create_task, asyncio.gather, asyncio.sleep, len, state.pending_count` (+2 more)
- 📊 Local variables: `tasks, n`

#### `async run_download_phase(cfg, state, fetcher)` 🟢 (lines 23-30, complexity: 1)
- 🔗 Function calls: `DownloadWorker, asyncio.create_task, asyncio.gather, range, w.run`
- 📊 Local variables: `workers`

### 🌐 External API Usage

- **LinkDiscoverer(cfg, state, fetcher, 1)**: `LinkDiscoverer(cfg, state, fetcher, 1).run`
- **LinkDiscoverer(cfg, state, fetcher, n)**: `LinkDiscoverer(cfg, state, fetcher, n).run`
- **asyncio**: `asyncio.create_task, asyncio.gather, asyncio.sleep`
- **state**: `state.pending_count`
- **tasks**: `tasks.append`
- **tasks[0]**: `tasks[0].done`
- **w**: `w.run`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `DownloadWorker, LinkDiscoverer`

**External API calls:** `LinkDiscoverer(cfg, state, fetcher, 1).run, LinkDiscoverer(cfg, state, fetcher, n).run, asyncio.create_task, asyncio.gather, asyncio.sleep, state.pending_count, tasks.append, tasks[0].done, w.run`

**Built-in functions:** `len, range`

### 🤖 AI Modification Hints

- **Documentation needed:** Functions `run_discovery_phase, run_download_phase` lack docstrings

---

## 📄 File Analysis: `downloader/assets.py`

**Overview:** 58 lines, complexity: 0 🟢

**File Purpose:** AssetManager: download, dedupe & classify assets.

### 📦 Import Analysis

**Direct Imports:**
- `hashlib`
- `mimetypes`
- `os`

**From Imports:**
- `from __future__ import annotations`
- `from config.settings import AD_HOSTS, BACKUP_ROOT, MAX_ASSET_KB`
- `from core.state import State`
- `from pathlib import Path`
- `from urllib.parse import urlparse`
- `from utils.files import safe_file_write`

### 🌐 Global Scope Variables

**Constants:**
- `IMAGE_EXTS` = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.bmp', '.ico'} (line 17)

### 🏛️ Class Definitions

#### `AssetManager` - lines 20-58
**Methods:**
- `__init__(self, fetcher, state: State)` 🟢 (lines 21-28, complexity: 2)
  - 🔗 Calls: `Path, p.mkdir`
- `_choose_ext(self, url: str, kind_hint: str) -> str` 🟢 (lines 51-58, complexity: 4)
  - 🔗 Calls: `Path, Path(urlparse(url).path).suffix.lower, mimetypes.guess_extension, urlparse`

### 🌐 External API Usage

- **Path(urlparse(url)**: `Path(urlparse(url).path).suffix.lower`
- **hashlib**: `hashlib.md5, hashlib.md5(url.encode()).hexdigest`
- **mimetypes**: `mimetypes.guess_extension`
- **os**: `os.path.relpath, os.path.relpath(full, BACKUP_ROOT).replace`
- **p**: `p.mkdir`
- **url**: `url.encode`
- **urlparse(url)**: `urlparse(url).netloc.lower`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `Path, safe_file_write, self._choose_ext, self.fetcher.fetch_bytes, self.state.add_asset, self.state.get_asset, urlparse`

**External API calls:** `Path(urlparse(url).path).suffix.lower, hashlib.md5, hashlib.md5(url.encode()).hexdigest, mimetypes.guess_extension, os.path.relpath, os.path.relpath(full, BACKUP_ROOT).replace, p.mkdir, url.encode, urlparse(url).netloc.lower`

**Built-in functions:** `len`

### 🤖 AI Modification Hints

- **Class documentation:** Classes `AssetManager` need docstrings

---

## 📄 File Analysis: `downloader/workers.py`

**Overview:** 50 lines, complexity: 0 🟢

**File Purpose:** Phase-2: fetch HTML, rewrite via processor, save final.

### 📦 Import Analysis

**Direct Imports:**
- `traceback`

**From Imports:**
- `from core.pathutils import url_to_local_path`
- `from core.state import State`
- `from crawler.discover import handle_redirect`
- `from processor.orchestrator import process_html`
- `from urllib.parse import urljoin`
- `from utils.files import safe_file_write`

### 🏛️ Class Definitions

#### `DownloadWorker` - lines 14-50
**Methods:**
- `__init__(self, cfg, state: State, fetcher, wid, progress)` 🟢 (lines 15-20, complexity: 1)

### 🌐 External API Usage

- **traceback**: `traceback.print_exc`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `handle_redirect, process_html, safe_file_write, self._process, self.fetcher.fetch_text, self.progress.update, self.state.get_next, self.state.mark_downloaded, self.state.update_after_fetch, url_to_local_path, urljoin`

**External API calls:** `traceback.print_exc`

### 🤖 AI Modification Hints

- **Class documentation:** Classes `DownloadWorker` need docstrings

---

## 📄 File Analysis: `processor/orchestrator.py`

**Overview:** 36 lines, complexity: 0 🟢

**File Purpose:** Coordinate HTML rewriting: assets, links, future optimizations.

### 📦 Import Analysis

**Direct Imports:**
- `pathlib`

**From Imports:**
- `from bs4 import BeautifulSoup`
- `from core.pathutils import url_to_local_path`
- `from core.state import State`
- `from downloader.assets import AssetManager`
- `from processor.optimize.htmlmin import _opt_run, _opt_run`
- `from processor.rewrite.assets import _rewrite_body_assets, _rewrite_head`
- `from processor.rewrite.links import rewrite_links`

### 🌐 Global Scope Variables

**Global Variables:**
- `soup` = BeautifulSoup(html, 'html.parser') (line 24)
- `mgr` = AssetManager(fetcher, state) (line 25)
- `out_path` = pathlib.Path(url_to_local_path(page_url)) (line 31)

### ⚙️ Top-Level Functions

#### `async process_html(page_url: str, html: str, fetcher, state: State) -> str` 🟢 (lines 16-36, complexity: 1)
**Purpose:** • Parse HTML with BeautifulSoup
• Localise head assets, body assets
• Rewrite internal anchors
• (Future) Pass through optimiser hook
- 🔗 Function calls: `AssetManager, BeautifulSoup, _opt_run, _rewrite_body_assets, _rewrite_head, pathlib.Path, rewrite_links, str` (+1 more)
- 📊 Local variables: `soup, mgr, out_path`

### 🌐 External API Usage

- **pathlib**: `pathlib.Path`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `AssetManager, BeautifulSoup, _opt_run, _rewrite_body_assets, _rewrite_head, rewrite_links, url_to_local_path`

**External API calls:** `pathlib.Path`

**Built-in functions:** `str`

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `processor/rewrite/assets.py`

**Overview:** 145 lines, complexity: 0 🟢

**File Purpose:** Download & rewrite <head> and <body>‐level external resources.

Public coroutines
-----------------
* _rewrite_head(soup, page_url, asset_mgr)
* _rewrite_body_assets(soup, page_url, asset_mgr)

Both modify the BeautifulSoup object **in-place** and never return HTML text.

### 📦 Import Analysis

**Direct Imports:**
- `asyncio`
- `re`

**From Imports:**
- `from __future__ import annotations`
- `from bs4 import BeautifulSoup`
- `from config.settings import BASE_URL`
- `from core.adblock import is_blocked_host`
- `from downloader.assets import AssetManager`
- `from urllib.parse import urljoin, urlparse`

### 🌐 Global Scope Variables

**Constants:**
- `CSS_URL_RE` = re.compile('url\\\\([\'\\\\\\"]?(.*?)[\'\\\\\\"]?\\\\)') (line 25)
- `IMG_TAGS` = ('img', 'input') (line 26)

**Global Variables:**
- `url` = urljoin(BASE_URL, tag[attr]) (line 30)
- `rep` = await mgr.fetch(url, 'images') (line 31)
- `head` = soup.head (line 42)
- `rels` = {r.lower() for r in link.get('rel', [])} (line 56)
- `href` = urljoin(BASE_URL, link['href']) (line 57)
- `host` = urlparse(href).netloc.lower() (line 58)
- `repl` = await mgr.fetch(href, 'css') (line 64)
- `repl` = await mgr.fetch(href, 'misc') (line 69)
- `repl` = await mgr.fetch(href, 'images') (line 74)
- `src_abs` = urljoin(BASE_URL, script['src']) (line 84)
- `repl` = await mgr.fetch(src_abs, 'js') (line 88)
- `css` = style.string (line 100)
- `abs_u` = urljoin(page_url, orig) (line 102)
- `repl` = await mgr.fetch(abs_u, 'fonts') (line 103)
- `css` = css.replace(orig, repl) (line 105)
- `newset` = [] (line 129)
- `url` = part.split()[0] (line 131)
- `repl` = await mgr.fetch(urljoin(BASE_URL, url), 'images') (line 132)
- `style` = tag['style'] (line 140)
- `repl` = await mgr.fetch(urljoin(page_url, orig), 'images') (line 142)
- `style` = style.replace(orig, repl) (line 144)

### ⚙️ Top-Level Functions

#### `async _download_and_replace(tag, attr, mgr: AssetManager)` 🟢 (lines 29-33, complexity: 2)
- 🔗 Function calls: `mgr.fetch, urljoin`
- 📊 Local variables: `url, rep`

#### `async _rewrite_head(soup: BeautifulSoup, page_url: str, mgr: AssetManager)` 🟢 (lines 37-48, complexity: 2)
**Purpose:** Rewrite <head> resources: stylesheets, icons, scripts, inline styles.
Delegates to helper functions for clarity and testability.
- 🔗 Function calls: `_handle_head_scripts, _handle_inline_styles, _handle_link_tags`
- 📊 Local variables: `head`

#### `async _handle_link_tags(head: BeautifulSoup, mgr: AssetManager)` 🟡 (lines 51-76, complexity: 9)
**Purpose:** Process <link> tags in <head>: stylesheets, preload/prefetch, icons.
- 🔗 Function calls: `head.find_all, is_blocked_host, link.decompose, link.get, mgr.fetch, r.lower, urljoin, urlparse` (+1 more)
- 📊 Local variables: `rels, href, host, repl, repl` (+1 more)

#### `async _handle_head_scripts(head: BeautifulSoup, mgr: AssetManager)` 🟢 (lines 79-90, complexity: 4)
**Purpose:** Process <script src="…"> tags in <head>.
- 🔗 Function calls: `head.find_all, is_blocked_host, mgr.fetch, script.decompose, urljoin, urlparse, urlparse(src_abs).netloc.lower`
- 📊 Local variables: `src_abs, repl`

#### `async _handle_inline_styles(head: BeautifulSoup, page_url: str, mgr: AssetManager)` 🟢 (lines 93-106, complexity: 5)
**Purpose:** Process inline <style> tags: find font URLs and download them.
- 🔗 Function calls: `CSS_URL_RE.findall, css.replace, head.find_all, mgr.fetch, style.string.replace_with, urljoin`
- 📊 Local variables: `css, abs_u, repl, css`

#### `async _rewrite_body_assets(soup: BeautifulSoup, page_url: str, mgr: AssetManager)` 🟡 (lines 110-145, complexity: 8)
- 🔗 Function calls: `','.join, CSS_URL_RE.findall, _download_and_replace, asyncio.gather, mgr.fetch, newset.append, part.replace, part.split` (+4 more)
- 📊 Local variables: `newset, url, repl, style, repl` (+1 more)

### 🌐 External API Usage

- **','**: `','.join`
- **CSS_URL_RE**: `CSS_URL_RE.findall`
- **asyncio**: `asyncio.gather`
- **css**: `css.replace`
- **head**: `head.find_all`
- **link**: `link.decompose, link.get`
- **mgr**: `mgr.fetch`
- **newset**: `newset.append`
- **part**: `part.replace, part.split`
- **r**: `r.lower`
- **re**: `re.compile`
- **script**: `script.decompose`
- **soup**: `soup.find_all`
- **src['srcset']**: `src['srcset'].split`
- **style**: `style.replace, style.string.replace_with`
- **urlparse(href)**: `urlparse(href).netloc.lower`
- **urlparse(src_abs)**: `urlparse(src_abs).netloc.lower`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `_download_and_replace, _handle_head_scripts, _handle_inline_styles, _handle_link_tags, is_blocked_host, urljoin, urlparse`

**External API calls:** `','.join, CSS_URL_RE.findall, asyncio.gather, css.replace, head.find_all, link.decompose, link.get, mgr.fetch, newset.append, part.replace, part.split, r.lower, re.compile, script.decompose, soup.find_all`
 (+5 more)

### 🤖 AI Modification Hints

- **Documentation needed:** Functions `_download_and_replace, _rewrite_body_assets` lack docstrings

---

## 📄 File Analysis: `processor/rewrite/links.py`

**Overview:** 44 lines, complexity: 0 🟢

**File Purpose:** Rewrite every internal <a href> so it points to the correct local file.

### 📦 Import Analysis

**Direct Imports:**
- `os`

**From Imports:**
- `from bs4 import BeautifulSoup`
- `from config.settings import BASE_DOMAIN, BASE_URL`
- `from core.redirects import redirects`
- `from core.state import REL, State`
- `from urllib.parse import urljoin, urlparse`

### 🌐 Global Scope Variables

**Global Variables:**
- `cur_dir` = os.path.dirname(cur_file) (line 16)
- `href` = a['href'] (line 19)
- `abs_url` = urljoin(BASE_URL, href) (line 23)
- `netloc` = urlparse(base).netloc (line 25)
- `key` = urlparse(base).path + (f'?{urlparse(base).query}' if urlparse(base).query else '') (line 30)
- `key` = redirects.resolve(key) (line 33)
- `rec` = state.urls.get(key) (line 35)
- `target_file` = rec[REL] (line 38)
- `rel_link` = os.path.relpath(target_file, cur_dir).replace(os.sep, '/') (line 39)
- `rel_link` = rel_link[:-len('index.html')] or './' (line 41)

### ⚙️ Top-Level Functions

#### `rewrite_links(soup: BeautifulSoup, cur_file: str, state: State)` 🟡 (lines 15-44, complexity: 9)
- 🔗 Function calls: `abs_url.split, href.startswith, len, os.path.dirname, os.path.relpath, os.path.relpath(target_file, cur_dir).replace, redirects.resolve, rel_link.endswith` (+4 more)
- 📊 Local variables: `cur_dir, href, abs_url, netloc, key` (+5 more)

### 🌐 External API Usage

- **abs_url**: `abs_url.split`
- **href**: `href.startswith`
- **os**: `os.path.dirname, os.path.relpath, os.path.relpath(target_file, cur_dir).replace`
- **redirects**: `redirects.resolve`
- **rel_link**: `rel_link.endswith`
- **soup**: `soup.find_all`
- **state**: `state.urls.get`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `urljoin, urlparse`

**External API calls:** `abs_url.split, href.startswith, os.path.dirname, os.path.relpath, os.path.relpath(target_file, cur_dir).replace, redirects.resolve, rel_link.endswith, soup.find_all, state.urls.get`

**Built-in functions:** `len`

### 🤖 AI Modification Hints

- **Documentation needed:** Functions `rewrite_links` lack docstrings

---

## 📄 File Analysis: `tests/conftest.py`

**Overview:** 10 lines, complexity: 0 🟢

### 📦 Import Analysis

**Direct Imports:**
- `pytest`

### ⚙️ Top-Level Functions

#### `tmp_root(tmp_path)` 🟢 (lines 5-10, complexity: 1) @pytest.fixture
**Purpose:** Create an isolated BACKUP_ROOT folder for each test.
Auto-cleaned by pytest.

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `tests/test_pathutils.py`

**Overview:** 7 lines, complexity: 0 🟢

### 📦 Import Analysis

**From Imports:**
- `from core.pathutils import url_to_local_path`

### 🌐 Global Scope Variables

**Global Variables:**
- `out` = url_to_local_path('/f17-something') (line 6)

### ⚙️ Top-Level Functions

#### `test_basic_mapping(tmp_root, monkeypatch)` 🟢 (lines 4-7, complexity: 1)
- 🔗 Function calls: `monkeypatch.setattr, out.endswith, url_to_local_path`
- 📊 Local variables: `out`

### 🌐 External API Usage

- **monkeypatch**: `monkeypatch.setattr`
- **out**: `out.endswith`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `url_to_local_path`

**External API calls:** `monkeypatch.setattr, out.endswith`

### 🤖 AI Modification Hints

- **Documentation needed:** Functions `test_basic_mapping` lack docstrings

---

## 📄 File Analysis: `tests/test_redirects.py`

**Overview:** 7 lines, complexity: 0 🟢

### 📦 Import Analysis

**From Imports:**
- `from core.redirects import RedirectMap`

### 🌐 Global Scope Variables

**Global Variables:**
- `rm` = RedirectMap(':memory:') (line 5)

### ⚙️ Top-Level Functions

#### `test_chain_resolution()` 🟢 (lines 4-7, complexity: 1)
- 🔗 Function calls: `RedirectMap, rm.map.update, rm.resolve`
- 📊 Local variables: `rm`

### 🌐 External API Usage

- **rm**: `rm.map.update, rm.resolve`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `RedirectMap`

**External API calls:** `rm.map.update, rm.resolve`

### 🤖 AI Modification Hints

- **Documentation needed:** Functions `test_chain_resolution` lack docstrings

---

## 📄 File Analysis: `utils/files.py`

**Overview:** 33 lines, complexity: 0 🟢

**File Purpose:** Atomic file I/O helpers.

### 📦 Import Analysis

**Direct Imports:**
- `asyncio`
- `os`
- `tempfile`

**From Imports:**
- `from __future__ import annotations`
- `from pathlib import Path`

### 🌐 Global Scope Variables

**Global Variables:**
- `p` = Path(path) (line 15)

### ⚙️ Top-Level Functions

#### `async safe_file_write(path: str | Path, data: str | bytes, mode: str) -> bool` 🟢 (lines 13-24, complexity: 2)
- 🔗 Function calls: `Path, fh.write, os.fdopen, os.replace, p.parent.mkdir, print, tempfile.mkstemp`
- 📊 Local variables: `p`

#### `async safe_file_read(path: str | Path, mode: str)` 🟢 (lines 27-33, complexity: 2)
- 🔗 Function calls: `Path, asyncio.to_thread`

### 🌐 External API Usage

- **asyncio**: `asyncio.to_thread`
- **fh**: `fh.write`
- **os**: `os.fdopen, os.replace`
- **p**: `p.parent.mkdir`
- **tempfile**: `tempfile.mkstemp`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**Internal calls:** `Path`

**External API calls:** `asyncio.to_thread, fh.write, os.fdopen, os.replace, p.parent.mkdir, tempfile.mkstemp`

**Built-in functions:** `print`

### 🤖 AI Modification Hints

- **Documentation needed:** Functions `safe_file_write, safe_file_read` lack docstrings

---

## 📄 File Analysis: `utils/logging.py`

**Overview:** 10 lines, complexity: 0 🟢

### 📦 Import Analysis

**Direct Imports:**
- `logging`
- `sys`

### ⚙️ Top-Level Functions

#### `setup(level)` 🟢 (lines 5-10, complexity: 1)
- 🔗 Function calls: `getattr, logging.StreamHandler, logging.basicConfig`

### 🌐 External API Usage

- **logging**: `logging.StreamHandler, logging.basicConfig`

### 📞 Function Call Graph

*All function calls detected in this file (for AI dependency analysis)*

**External API calls:** `logging.StreamHandler, logging.basicConfig`

**Built-in functions:** `getattr`

### 🤖 AI Modification Hints

- **Documentation needed:** Functions `setup` lack docstrings

## 🔍 Cross-Reference Analysis

*For AI understanding of code relationships and dependencies*

### 🌍 External Dependencies Summary

- **', '**: 1 calls - `', '.join`
- **','**: 1 calls - `','.join`
- **'_'**: 1 calls - `'_'.join`
- **(Path(BACKUP_ROOT) / 'index**: 1 calls - `(Path(BACKUP_ROOT) / 'index.html').resolve`
- **(backup_root / 'settings**: 1 calls - `(backup_root / 'settings.yaml.lock').write_text`
- **AD_HOSTS**: 1 calls - `AD_HOSTS.update`
- **CSS_URL_RE**: 1 calls - `CSS_URL_RE.findall`
- **FOLDER_MAPPING**: 1 calls - `FOLDER_MAPPING.get`
- **HOSTLINE_RE**: 1 calls - `HOSTLINE_RE.match`
- **LinkDiscoverer(cfg, state, fetcher, 1)**: 1 calls - `LinkDiscoverer(cfg, state, fetcher, 1).run`
- **LinkDiscoverer(cfg, state, fetcher, n)**: 1 calls - `LinkDiscoverer(cfg, state, fetcher, n).run`
- **Path**: 1 calls - `Path.home`
- **Path(__file__)**: 1 calls - `Path(__file__).with_name`
- **Path(out)**: 1 calls - `Path(out).expanduser`
- **Path(urlparse(url)**: 1 calls - `Path(urlparse(url).path).suffix.lower`
- **abs_url**: 1 calls - `abs_url.split`
- **ad_hosts**: 1 calls - `ad_hosts.add`
- **aiohttp**: 1 calls - `aiohttp.ClientSession`
- **argparse**: 1 calls - `argparse.ArgumentParser`
- **ast**: 3 calls - `ast.get_docstring, ast.parse, ast.walk`
- **asyncio**: 6 calls - `asyncio.Lock, asyncio.create_task, asyncio.gather, asyncio.run, asyncio.sleep` (+1 more)
- **backup_root**: 1 calls - `backup_root.mkdir`
- **cache_file**: 5 calls - `cache_file.exists, cache_file.read_text, cache_file.read_text('utf-8').splitlines, cache_file.stat, cache_file.write_text`
- **cfg**: 1 calls - `cfg.get`
- **cookies_file**: 2 calls - `cookies_file.exists, cookies_file.read_text`
- **css**: 1 calls - `css.replace`
- **doc**: 1 calls - `doc.strip`
- **docs**: 1 calls - `docs.append`
- **domain**: 2 calls - `domain.replace, domain.split`
- **f**: 1 calls - `f.read`
- **fetcher**: 1 calls - `fetcher.close`
- **fh**: 1 calls - `fh.write`
- **fn**: 1 calls - `fn.endswith`
- **forum**: 5 calls - `forum.lstrip, forum.rstrip, forum.split, forum.split('//', 1)[1].split, forum.startswith`
- **forum_url**: 2 calls - `forum_url.split, forum_url.split('//', 1)[1].split`
- **globals()**: 1 calls - `globals().update`
- **hashlib**: 2 calls - `hashlib.md5, hashlib.md5(url.encode()).hexdigest`
- **head**: 1 calls - `head.find_all`
- **host**: 1 calls - `host.lower`
- **href**: 1 calls - `href.startswith`
- **input('Open it now? (y/N): ')**: 1 calls - `input('Open it now? (y/N): ').lower`
- **input('Reconfigure cookies? (y/N): ')**: 2 calls - `input('Reconfigure cookies? (y/N): ').strip, input('Reconfigure cookies? (y/N): ').strip().lower`
- **input(f'{ck1}: ')**: 1 calls - `input(f'{ck1}: ').strip`
- **input(f'{ck2}: ')**: 1 calls - `input(f'{ck2}: ').strip`
- **input(f'🎯 Target Forum: (default {default_url}): ')**: 1 calls - `input(f'🎯 Target Forum: (default {default_url}): ').strip`
- **input(f'📁 Backup Folder: (default {default_dir}): ')**: 1 calls - `input(f'📁 Backup Folder: (default {default_dir}): ').strip`
- **item['docstring']**: 1 calls - `item['docstring'].splitlines`
- **json**: 4 calls - `json.dump, json.dumps, json.load, json.loads`
- **link**: 2 calls - `link.decompose, link.get`
- **logging**: 2 calls - `logging.StreamHandler, logging.basicConfig`
- **m**: 2 calls - `m.group, m.group(1).lower`
- **mgr**: 1 calls - `mgr.fetch`
- **mimetypes**: 1 calls - `mimetypes.guess_extension`
- **monkeypatch**: 1 calls - `monkeypatch.setattr`
- **newset**: 1 calls - `newset.append`
- **os**: 12 calls - `os.environ.get, os.fdopen, os.getcwd, os.makedirs, os.path.basename` (+7 more)
- **out**: 1 calls - `out.endswith`
- **out_dir**: 1 calls - `out_dir.mkdir`
- **p**: 3 calls - `p.mkdir, p.parent.mkdir, p.path.startswith`
- **parsed**: 6 calls - `parsed.path.lower, parsed.path.lower().startswith, parsed.path.lstrip, parsed.path.lstrip('/').lower, parsed.query.replace` (+1 more)
- **parser**: 2 calls - `parser.add_argument, parser.parse_args`
- **part**: 2 calls - `part.replace, part.split`
- **path**: 2 calls - `path.exists, path.read_text`
- **pathlib**: 1 calls - `pathlib.Path`
- **platform**: 1 calls - `platform.system`
- **r**: 2 calls - `r.lower, r.text`
- **re**: 1 calls - `re.compile`
- **redirects**: 2 calls - `redirects.add, redirects.resolve`
- **rel_link**: 1 calls - `rel_link.endswith`
- **resp**: 2 calls - `resp.read, resp.text`
- **rm**: 2 calls - `rm.map.update, rm.resolve`
- **route**: 1 calls - `route.split`
- **s**: 1 calls - `s.get`
- **script**: 1 calls - `script.decompose`
- **session**: 1 calls - `session.get`
- **shutil**: 1 calls - `shutil.copy`
- **soup**: 1 calls - `soup.find_all`
- **src**: 1 calls - `src.get`
- **src['srcset']**: 1 calls - `src['srcset'].split`
- **state**: 6 calls - `state.add_url, state.load, state.mark_redirect_source, state.pending_count, state.save` (+1 more)
- **style**: 2 calls - `style.replace, style.string.replace_with`
- **subprocess**: 1 calls - `subprocess.call`
- **sys**: 1 calls - `sys.exit`
- **tasks**: 1 calls - `tasks.append`
- **tasks[0]**: 1 calls - `tasks[0].done`
- **tempfile**: 1 calls - `tempfile.mkstemp`
- **time**: 1 calls - `time.time`
- **traceback**: 2 calls - `traceback.format_exc, traceback.print_exc`
- **txt**: 1 calls - `txt.splitlines`
- **url**: 2 calls - `url.encode, url.split`
- **urlparse(forum_url)**: 1 calls - `urlparse(forum_url).netloc.lower`
- **urlparse(href)**: 1 calls - `urlparse(href).netloc.lower`
- **urlparse(src_abs)**: 1 calls - `urlparse(src_abs).netloc.lower`
- **urlparse(url)**: 1 calls - `urlparse(url).netloc.lower`
- **visited**: 1 calls - `visited.add`
- **w**: 1 calls - `w.run`
- **yaml**: 1 calls - `yaml.safe_load`
- **yaml_path**: 1 calls - `yaml_path.exists`

---

## 📋 Report Generation Metadata

- **Generated on:** 2025-06-27 01:52:50
- **Script version:** AI Code Mapper v2.0
- **Analysis root:** `C:\Users\Sammu\O meu disco\Código\Forum_Backup`
- **Files analyzed:** 22
- **Total errors:** 0
- **Self-awareness:** Skipped analysis of `Mapeador.py`

*This report is optimized for AI model comprehension and code modification assistance.*

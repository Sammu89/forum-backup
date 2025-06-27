## `Docstrings.py`

- **function** `extract_docstrings_from_file(filepath)` (line 8)
  Parse a .py file and return a list of dicts for every
  module-level class/function (and async function).
- **function** `scan_project(base_path)` (line 41)
  Walk through base_path and build a map:
    { relative_filepath: [ {type,name,signature,lineno,docstring}, ... ], ... }
- **function** `generate_markdown(project_map, title)` (line 58)
  Given the map from scan_project, print Markdown to stdout.
- **function** `main()` (line 78)
  *(no docstring)*

## `Mapeador.py`

- **class** `VariableInfo` (line 48)
  Information about variables and their usage.
- **class** `FunctionInfo` (line 59)
  Comprehensive information about a function or method.
- **class** `ClassInfo` (line 79)
  Comprehensive information about a class.
- **class** `FileInfo` (line 95)
  Comprehensive information about a Python file.
- **class** `ComprehensiveAnalyzer` (line 113)
  Advanced AST analyzer with scope awareness and comprehensive code mapping.
- **function** `analyze_python_file(path)` (line 414)
  Analyze a Python file and return its comprehensive structure.
- **function** `build_project_tree(data)` (line 433)
  Build comprehensive project tree structure.
- **function** `generate_tree_visualization(tree, prefix)` (line 467)
  Generate comprehensive tree visualization.
- **function** `generate_comprehensive_markdown(tree_lines, data)` (line 536)
  Generate comprehensive AI-friendly Markdown report.
- **function** `discover_python_files(root_path)` (line 934)
  Discover all Python files in the project, excluding ignored paths and self.
- **function** `generate_cross_reference_analysis(data)` (line 959)
  Generate cross-reference analysis for AI understanding.
- **function** `main()` (line 1030)
  *(no docstring)*
- **function** `__init__(self)` (line 116)
  *(no docstring)*
- **function** `visit_Module(self, node)` (line 124)
  Analyze module-level constructs.
- **function** `visit_Import(self, node)` (line 133)
  Process import statements.
- **function** `visit_ImportFrom(self, node)` (line 141)
  Process from...import statements.
- **function** `visit_Assign(self, node)` (line 157)
  Track variable assignments.
- **function** `visit_Call(self, node)` (line 178)
  Analyze function calls.
- **function** `visit_Raise(self, node)` (line 196)
  Track raised exceptions.
- **function** `_get_exception_name(self, node)` (line 205)
  Extract exception name from raise statement.
- **function** `_get_call_name(self, node)` (line 211)
  Extract function call name robustly.
- **function** `visit_ClassDef(self, node)` (line 226)
  Analyze class definitions comprehensively.
- **function** `visit_FunctionDef(self, node)` (line 277)
  Analyze function definitions.
- **function** `visit_AsyncFunctionDef(self, node)` (line 286)
  Handle async functions.
- **function** `_analyze_function(self, node, is_method, is_async)` (line 294)
  Comprehensively analyze a function or method.
- **function** `_calculate_complexity(self, node)` (line 377)
  Calculate cyclomatic complexity of a function.
- **function** `_get_end_line(self, node)` (line 389)
  Get the end line number of a node.
- **function** `_get_decorator_name(self, decorator)` (line 397)
  Extract decorator name.
- **function** `_safe_unparse(self, node)` (line 406)
  Safe unparsing that doesn't fail.

## `cli\__main__.py`

- **function** `prompt_forum_and_folder(last_url)` (line 37)
  *(no docstring)*
- **function** `main()` (line 57)
  *(no docstring)*

## `cli\auth.py`

- **function** `load_cookies(cookies_file)` (line 15)
  Load cookies from the given file path.
- **function** `is_logged_in(session, forum_url)` (line 24)
  Check if the current session is authenticated by looking for a '/profile' link in the path.
- **function** `handle_authentication(backup_root, forum_url)` (line 42)
  Returns (cookies, logged_in_flag).
  Uses backup_root to store cookies.json and prompts user to re-enter cookies if not authenticated.
  
  Args:
      backup_root: Path to the backup folder where cookies.json is stored.
      forum_url:   Base URL of the forum to check authentication.

## `config\settings.py`

- **function** `_load_yaml(path)` (line 28)
  Load YAML from the given path, return empty dict if missing or invalid.
- **function** `init(backup_root, user_yaml, forum_url)` (line 39)
  Initialize configuration by loading defaults and per-forum overrides.
  
  - Sets BACKUP_ROOT, BASE_URL, BASE_DOMAIN based on user input.
  - Reads `defaults.yaml` and merges with `user_yaml` if provided.
  
  Args:
      backup_root: Path to the forum's output folder.
      user_yaml:   Optional Path to a forum-specific YAML file.
      forum_url:   Base URL provided by the user at startup.

## `core\adblock.py`

- **function** `_fetch_and_cache(src, cache_file)` (line 12)
  *(no docstring)*
- **function** `update_hosts(backup_root)` (line 23)
  Download or use cached host files, parse out hostnames,
  merge into AD_HOSTS.
- **function** `is_blocked_host(host)` (line 40)
  *(no docstring)*

## `core\fetcher.py`

- **class** `Fetcher` (line 10)
  Re-usable aiohttp session with adaptive throttle-awareness and cookies.
  Methods:
    fetch_text(url, allow_redirects=True) -> (status, text|None, final_url)
    fetch_bytes(url)                     -> (status, bytes|None)
    close()                              -> closes session
- **function** `__init__(self, cfg, throttle, cookies)` (line 19)
  *(no docstring)*
- **function** `_ensure_session(self)` (line 29)
  *(no docstring)*
- **function** `fetch_text(self, url, allow_redirects)` (line 49)
  Fetch text content from URL. Returns (status, text, final_url).
- **function** `fetch_bytes(self, url)` (line 114)
  Fetch binary content. Returns (status, data).
- **function** `close(self)` (line 150)
  Close the aiohttp session.

## `core\pathutils.py`

- **function** `url_to_local_path(url)` (line 9)
  Map a forum path to a local HTML file path under BACKUP_ROOT.
  - lowercase
  - slugify each segment (max SLUG_MAX_LEN)
  - choose folder via FOLDER_MAPPING, fallback to 'misc'
  - on name collision append -dupN

## `core\redirects.py`

- **class** `RedirectMap` (line 7)
  Persisted map of src_path->dst_path (redirects.json).
  Thread-safe. resolve() follows chains (visited + depth≤16).
- **function** `__init__(self, filename)` (line 13)
  *(no docstring)*
- **function** `_load(self)` (line 19)
  *(no docstring)*
- **function** `add(self, src, dst)` (line 28)
  *(no docstring)*
- **function** `_persist(self)` (line 35)
  *(no docstring)*
- **function** `resolve(self, path)` (line 40)
  *(no docstring)*

## `core\state.py`

- **class** `State` (line 11)
  Manages two JSON stores:
    - crawl_state.json: mapping URL->compact record
    - assets_cache.json: mapping assetURL->relPath
  Thread-safe via asyncio.Lock.
- **function** `__init__(self, cfg, state_path, cache_path)` (line 19)
  *(no docstring)*
- **function** `load(self)` (line 27)
  *(no docstring)*
- **function** `save(self)` (line 41)
  *(no docstring)*
- **function** `add_url(self, path, rel)` (line 55)
  *(no docstring)*
- **function** `get_next(self, phase)` (line 60)
  *(no docstring)*
- **function** `pending_count(self)` (line 68)
  *(no docstring)*
- **function** `mark_discovered(self, path)` (line 71)
  *(no docstring)*
- **function** `mark_downloaded(self, path)` (line 75)
  *(no docstring)*
- **function** `mark_redirect_source(self, path)` (line 79)
  *(no docstring)*
- **function** `update_after_fetch(self, path, success, err)` (line 84)
  *(no docstring)*
- **function** `get_asset(self, url)` (line 94)
  *(no docstring)*
- **function** `add_asset(self, url, rel)` (line 97)
  *(no docstring)*

## `core\throttle.py`

- **class** `ThrottleController` (line 4)
  Adaptive delay & worker governor.
    - base_delay: start from cfg.base_delay
    - min/max_delay: clamp
    - workers: current parallel worker count
  API:
    before_request()  -> async sleep(current delay)
    after_response(status) -> adjust delay/workers
- **function** `__init__(self, cfg)` (line 15)
  *(no docstring)*
- **function** `before_request(self)` (line 24)
  *(no docstring)*
- **function** `after_response(self, status)` (line 27)
  *(no docstring)*

## `crawler\discover.py`

- **function** `_strip_fragment(url)` (line 20)
  *(no docstring)*
- **function** `_is_valid_link(href)` (line 24)
  *(no docstring)*
- **function** `_path_plus_query(url)` (line 40)
  *(no docstring)*
- **function** `handle_redirect(worker_id, src_url, dst_url, state)` (line 45)
  Record an internal redirect and enqueue the destination.
- **class** `LinkDiscoverer` (line 65)
  Worker to fetch raw HTML, save it, discover links.
- **function** `__init__(self, cfg, state, fetcher, worker_id)` (line 70)
  *(no docstring)*
- **function** `run(self)` (line 76)
  *(no docstring)*
- **function** `_process(self, path)` (line 89)
  *(no docstring)*
- **function** `_parse_links(self, html)` (line 111)
  *(no docstring)*

## `crawler\scheduler.py`

- **function** `run_discovery_phase(cfg, state, fetcher)` (line 8)
  *(no docstring)*
- **function** `run_download_phase(cfg, state, fetcher)` (line 23)
  *(no docstring)*

## `downloader\assets.py`

- **class** `AssetManager` (line 20)
  *(no docstring)*
- **function** `__init__(self, fetcher, state)` (line 21)
  *(no docstring)*
- **function** `fetch(self, url, kind_hint)` (line 30)
  *(no docstring)*
- **function** `_choose_ext(self, url, kind_hint)` (line 51)
  *(no docstring)*

## `downloader\workers.py`

- **class** `DownloadWorker` (line 14)
  *(no docstring)*
- **function** `__init__(self, cfg, state, fetcher, wid, progress)` (line 15)
  *(no docstring)*
- **function** `run(self)` (line 22)
  *(no docstring)*
- **function** `_process(self, path)` (line 29)
  *(no docstring)*

## `processor\orchestrator.py`

- **function** `process_html(page_url, html, fetcher, state)` (line 16)
  • Parse HTML with BeautifulSoup
  • Localise head assets, body assets
  • Rewrite internal anchors
  • (Future) Pass through optimiser hook

## `processor\rewrite\assets.py`

- **function** `_download_and_replace(tag, attr, mgr)` (line 29)
  *(no docstring)*
- **function** `_rewrite_head(soup, page_url, mgr)` (line 37)
  Rewrite <head> resources: stylesheets, icons, scripts, inline styles.
  Delegates to helper functions for clarity and testability.
- **function** `_handle_link_tags(head, mgr)` (line 51)
  Process <link> tags in <head>: stylesheets, preload/prefetch, icons.
- **function** `_handle_head_scripts(head, mgr)` (line 79)
  Process <script src="…"> tags in <head>.
- **function** `_handle_inline_styles(head, page_url, mgr)` (line 93)
  Process inline <style> tags: find font URLs and download them.
- **function** `_rewrite_body_assets(soup, page_url, mgr)` (line 110)
  *(no docstring)*

## `processor\rewrite\links.py`

- **function** `rewrite_links(soup, cur_file, state)` (line 15)
  *(no docstring)*

## `tests\conftest.py`

- **function** `tmp_root(tmp_path)` (line 5)
  Create an isolated BACKUP_ROOT folder for each test.
  Auto-cleaned by pytest.

## `tests\test_pathutils.py`

- **function** `test_basic_mapping(tmp_root, monkeypatch)` (line 4)
  *(no docstring)*

## `tests\test_redirects.py`

- **function** `test_chain_resolution()` (line 4)
  *(no docstring)*

## `utils\files.py`

- **function** `safe_file_write(path, data, mode)` (line 13)
  *(no docstring)*
- **function** `safe_file_read(path, mode)` (line 27)
  *(no docstring)*

## `utils\logging.py`

- **function** `setup(level)` (line 5)
  *(no docstring)*


# 🧠 AI-Friendly Code Structure Analysis

*Generated for AI model comprehension and code modification assistance*

## 🌲 Project Structure & Complexity Map

```text
📊 Legend:
🟢 Low Complexity (≤10)  🟡 Medium (11-20)  🔴 High (>20)
📃 Small (<100 lines)   📄 Medium (100-500)  📚 Large (>500)
🏛️ Class  ⚙️ Function  ⚡ Async  🔶 Abstract  📁 Directory

PROJECT_ROOT/
├── 📄 Docstrings.py 🟢 (109 lines, complexity: 0)
│   └── ⚙️ extract_docstrings_from_file 🟢 (line 7, complexity: 5)
│   └── ⚙️ scan_project 🟢 (line 37, complexity: 5)
│   └── ⚙️ generate_markdown 🟡 (line 53, complexity: 6)
│   └── ⚙️ main 🟢 (line 72, complexity: 2)
├── 📁 cli
│   ├── 📃 __main__.py 🟢 (0 lines, complexity: 0)
│   └── 📃 auth.py 🟢 (0 lines, complexity: 0)
├── 📁 config
│   └── 📃 settings.py 🟢 (0 lines, complexity: 0)
├── 📁 core
│   ├── 📃 adblock.py 🟢 (0 lines, complexity: 0)
│   ├── 📃 fetcher.py 🟢 (0 lines, complexity: 0)
│   ├── 📃 pathutils.py 🟢 (0 lines, complexity: 0)
│   ├── 📃 redirects.py 🟢 (0 lines, complexity: 0)
│   ├── 📃 state.py 🟢 (0 lines, complexity: 0)
│   └── 📃 throttle.py 🟢 (0 lines, complexity: 0)
├── 📁 crawler
│   ├── 📃 discover.py 🟢 (0 lines, complexity: 0)
│   └── 📃 scheduler.py 🟢 (0 lines, complexity: 0)
├── 📁 downloader
│   ├── 📃 assets.py 🟢 (0 lines, complexity: 0)
│   └── 📃 workers.py 🟢 (0 lines, complexity: 0)
├── 📁 processor
│   ├── 📃 orchestrator.py 🟢 (0 lines, complexity: 0)
│   └── 📁 rewrite
│       ├── 📃 assets.py 🟢 (0 lines, complexity: 0)
│       └── 📃 links.py 🟢 (0 lines, complexity: 0)
└── 📁 utils
    ├── 📃 files.py 🟢 (0 lines, complexity: 0)
    └── 📃 logging.py 🟢 (0 lines, complexity: 0)
```

## 📊 Comprehensive Project Metrics

- **Python Files Analyzed:** 19
- **Total Lines of Code:** 109
- **Classes Defined:** 0
- **Top-Level Functions:** 4
- **Class Methods:** 0
- **Average File Complexity:** 0.0
- **External Dependencies:** 4
- **Most Complex Files:** Docstrings.py, cli/__main__.py, cli/auth.py

## 🔗 Dependency Overview

- **argparse** → Used in 1 files
- **ast** → Used in 1 files
- **os** → Used in 1 files
- **sys** → Used in 1 files

---

## 📄 File Analysis: `Docstrings.py`

**Overview:** 109 lines, complexity: 0 🟢

### 📦 Import Analysis

**Direct Imports:**
- `argparse`
- `ast`
- `os`
- `sys`

### 🌐 Global Scope Variables

**Global Variables:**
- `source` = f.read() (line 13)
- `tree` = ast.parse(source, filename=filepath) (line 14)
- `docs` = [] (line 15)
- `obj_type` = 'class' if isinstance(node, ast.ClassDef) else 'function' (line 18)
- `name` = node.name (line 19)
- `lineno` = node.lineno (line 20)
- `doc` = ast.get_docstring(node) or '' (line 21)
- `args` = [arg.arg for arg in node.args.args] (line 24)
- `sig` = f'({', '.join(args)})' (line 25)
- `sig` = '' (line 27)
- `result` = {} (line 42)
- `full` = os.path.join(root, fn) (line 46)
- `rel` = os.path.relpath(full, base_path) (line 47)
- `docs` = extract_docstrings_from_file(full) (line 48)
- `header` = f'- **{item['type']}** `{item['name']}{item['signature']}` (line {item['lineno']})' (line 62)
- `default_output` = f'{os.path.basename(os.getcwd())}_docstrings.md' (line 74)
- `parser` = argparse.ArgumentParser(description='Generate a Markdown map of all Python docstrings in a project.') (line 76)
- `args` = parser.parse_args() (line 94)
- `project_map` = scan_project(args.project_root) (line 96)
- `old_stdout` = sys.stdout (line 100)

### ⚙️ Top-Level Functions

#### `extract_docstrings_from_file(filepath)` 🟢 (lines 7-35, complexity: 5)
**Purpose:** Parse a .py file and return a list of dicts for every
module-level class/function (and async function).
- 🔗 Function calls: `', '.join, ast.get_docstring, ast.parse, ast.walk, doc.strip, docs.append, f.read, isinstance` (+1 more)
- 📊 Local variables: `source, tree, docs, obj_type, name` (+5 more)

#### `scan_project(base_path)` 🟢 (lines 37-51, complexity: 5)
**Purpose:** Walk through base_path and build a map:
  { relative_filepath: [ {type,name,signature,lineno,docstring}, ... ], ... }
- 🔗 Function calls: `extract_docstrings_from_file, fn.endswith, os.path.join, os.path.relpath, os.walk`
- 📊 Local variables: `result, full, rel, docs`

#### `generate_markdown(project_map, title)` 🟡 (lines 53-70, complexity: 6)
**Purpose:** Given the map from scan_project, print Markdown to stdout.
- 🔗 Function calls: `item['docstring'].splitlines, print, sorted`
- 📊 Local variables: `header`

#### `main()` 🟢 (lines 72-106, complexity: 2)
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

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `cli/auth.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `config/settings.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `core/adblock.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `core/fetcher.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `core/pathutils.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `core/redirects.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `core/state.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `core/throttle.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `crawler/discover.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `crawler/scheduler.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `downloader/assets.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `downloader/workers.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `processor/orchestrator.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `processor/rewrite/assets.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `processor/rewrite/links.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `utils/files.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

---

## 📄 File Analysis: `utils/logging.py`

**Overview:** 0 lines, complexity: 0 🟢

### 🤖 AI Modification Hints

- ✅ Code structure appears well-organized for AI modifications

## 🔍 Cross-Reference Analysis

*For AI understanding of code relationships and dependencies*

### 🌍 External Dependencies Summary

- **', '**: 1 calls - `', '.join`
- **argparse**: 1 calls - `argparse.ArgumentParser`
- **ast**: 3 calls - `ast.get_docstring, ast.parse, ast.walk`
- **doc**: 1 calls - `doc.strip`
- **docs**: 1 calls - `docs.append`
- **f**: 1 calls - `f.read`
- **fn**: 1 calls - `fn.endswith`
- **item['docstring']**: 1 calls - `item['docstring'].splitlines`
- **os**: 5 calls - `os.getcwd, os.path.basename, os.path.join, os.path.relpath, os.walk`
- **parser**: 2 calls - `parser.add_argument, parser.parse_args`

---

## 📋 Report Generation Metadata

- **Generated on:** 2025-06-26 22:11:34
- **Script version:** AI Code Mapper v2.0
- **Analysis root:** `C:\Users\Sammu\O meu disco\Código\Forum_Backup`
- **Files analyzed:** 19
- **Total errors:** 0
- **Self-awareness:** Skipped analysis of `Mapeador.py`

*This report is optimized for AI model comprehension and code modification assistance.*

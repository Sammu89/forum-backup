## `Docstrings.py`

- **function** `extract_docstrings_from_file(filepath)` (line 7)
  Parse a .py file and return a list of dicts for every
  module-level class/function (and async function).
- **function** `scan_project(base_path)` (line 37)
  Walk through base_path and build a map:
    { relative_filepath: [ {type,name,signature,lineno,docstring}, ... ], ... }
- **function** `generate_markdown(project_map, title)` (line 53)
  Given the map from scan_project, print Markdown to stdout.
- **function** `main()` (line 72)
  *(no docstring)*

## `Mapeador.py`

- **class** `VariableInfo` (line 36)
  Information about variables and their usage.
- **class** `FunctionInfo` (line 45)
  Comprehensive information about a function or method.
- **class** `ClassInfo` (line 63)
  Comprehensive information about a class.
- **class** `FileInfo` (line 77)
  Comprehensive information about a Python file.
- **class** `ComprehensiveAnalyzer` (line 93)
  Advanced AST analyzer with scope awareness and comprehensive code mapping.
- **function** `analyze_python_file(path)` (line 378)
  Analyze a Python file and return its comprehensive structure.
- **function** `build_project_tree(data)` (line 396)
  Build comprehensive project tree structure.
- **function** `generate_tree_visualization(tree, prefix)` (line 423)
  Generate comprehensive tree visualization.
- **function** `generate_comprehensive_markdown(tree_lines, data)` (line 471)
  Generate comprehensive AI-friendly Markdown report.
- **function** `discover_python_files(root_path)` (line 745)
  Discover all Python files in the project, excluding ignored paths and self.
- **function** `generate_cross_reference_analysis(data)` (line 769)
  Generate cross-reference analysis for AI understanding.
- **function** `main()` (line 835)
  *(no docstring)*
- **function** `__init__(self)` (line 96)
  *(no docstring)*
- **function** `visit_Module(self, node)` (line 104)
  Analyze module-level constructs.
- **function** `visit_Import(self, node)` (line 111)
  Process import statements.
- **function** `visit_ImportFrom(self, node)` (line 119)
  Process from...import statements.
- **function** `visit_Assign(self, node)` (line 135)
  Track variable assignments.
- **function** `visit_Call(self, node)` (line 156)
  Analyze function calls.
- **function** `visit_Raise(self, node)` (line 172)
  Track raised exceptions.
- **function** `_get_exception_name(self, node)` (line 181)
  Extract exception name from raise statement.
- **function** `_get_call_name(self, node)` (line 187)
  Extract function call name robustly.
- **function** `visit_ClassDef(self, node)` (line 202)
  Analyze class definitions comprehensively.
- **function** `visit_FunctionDef(self, node)` (line 251)
  Analyze function definitions.
- **function** `visit_AsyncFunctionDef(self, node)` (line 260)
  Handle async functions.
- **function** `_analyze_function(self, node, is_method, is_async)` (line 268)
  Comprehensively analyze a function or method.
- **function** `_calculate_complexity(self, node)` (line 342)
  Calculate cyclomatic complexity of a function.
- **function** `_get_end_line(self, node)` (line 354)
  Get the end line number of a node.
- **function** `_get_decorator_name(self, decorator)` (line 362)
  Extract decorator name.
- **function** `_safe_unparse(self, node)` (line 371)
  Safe unparsing that doesn't fail.


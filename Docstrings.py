#!/usr/bin/env python3
import os
import ast
import argparse
import sys

def extract_docstrings_from_file(filepath):
    """
    Parse a .py file and return a list of dicts for every
    module-level class/function (and async function).
    """
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()
    tree = ast.parse(source, filename=filepath)
    docs = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            obj_type = "class" if isinstance(node, ast.ClassDef) else "function"
            name = node.name
            lineno = node.lineno
            doc = ast.get_docstring(node) or ""
            # build a simple signature for functions
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                args = [arg.arg for arg in node.args.args]
                sig = f"({', '.join(args)})"
            else:
                sig = ""
            docs.append({
                "type": obj_type,
                "name": name,
                "signature": sig,
                "lineno": lineno,
                "docstring": doc.strip()
            })
    return docs

def scan_project(base_path):
    """
    Walk through base_path and build a map:
      { relative_filepath: [ {type,name,signature,lineno,docstring}, ... ], ... }
    """
    result = {}
    for root, _, files in os.walk(base_path):
        for fn in files:
            if fn.endswith(".py"):
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, base_path)
                docs = extract_docstrings_from_file(full)
                if docs:
                    result[rel] = docs
    return result

def generate_markdown(project_map, title=None):
    """
    Given the map from scan_project, print Markdown to stdout.
    """
    if title:
        print(f"# {title}\n")
    for filepath in sorted(project_map):
        print(f"## `{filepath}`\n")
        for item in project_map[filepath]:
            header = f"- **{item['type']}** `{item['name']}{item['signature']}` (line {item['lineno']})"
            print(header)
            if item["docstring"]:
                # indent each line of the docstring
                for line in item["docstring"].splitlines():
                    print(f"  {line}")
            else:
                print("  *(no docstring)*")
        print("")  # blank line between files

def main():
    # default output filename: <current_folder>_docstrings.md
    default_output = f"{os.path.basename(os.getcwd())}_docstrings.md"

    parser = argparse.ArgumentParser(
        description="Generate a Markdown map of all Python docstrings in a project."
    )
    parser.add_argument(
        "project_root",
        nargs="?",
        default=os.getcwd(),
        help="Path to the root folder of your Python project (defaults to current directory)"
    )
    parser.add_argument(
        "-o", "--output",
        default=default_output,
        help="Write Markdown to this file (defaults to '<current_folder>_docstrings.md')"
    )
    parser.add_argument(
        "-t", "--title",
        help="Optional title for the Markdown document"
    )
    args = parser.parse_args()

    project_map = scan_project(args.project_root)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as md:
            old_stdout = sys.stdout
            sys.stdout = md
            generate_markdown(project_map, title=args.title)
            sys.stdout = old_stdout
        print(f"Markdown written to {args.output}")
    else:
        generate_markdown(project_map, title=args.title)

if __name__ == "__main__":
    main()

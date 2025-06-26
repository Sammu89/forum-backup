@echo off
title Documentation Generator

REM Execute Mapeador.py in current directory
echo Running Mapeador.py...
python Mapeador.py --root .
if %errorlevel% neq 0 (
   echo Error: Mapeador.py failed to execute.
   pause
   exit /b 1
)

REM Rename AI_CODE_MAP.md to Map_comprehensive.md if it exists
if exist "AI_CODE_MAP.md" (
    ren "AI_CODE_MAP.md" "Map_comprehensive.md"
    echo Renamed AI_CODE_MAP.md to Map_comprehensive.md
)

REM Execute Docstrings.py
echo Running Docstrings.py...
python Docstrings.py
if %errorlevel% neq 0 (
   echo Error: Docstrings.py failed to execute.
   pause
   exit /b 1
)

REM Get current folder name
for %%i in ("%cd%") do set "currentFolder=%%~nxi"

REM Rename currentfoldername_docstrings.md to Map_docstrings.md if it exists
if exist "%currentFolder%_docstrings.md" (
    ren "%currentFolder%_docstrings.md" "Map_docstrings.md"
    echo Renamed %currentFolder%_docstrings.md to Map_docstrings.md
)

echo.
echo Documentation generation completed successfully.
pause
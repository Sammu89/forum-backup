@echo off
REM -----------------------------------------------------------------------------
REM format_and_lint.bat
REM Runs Black → isort → Ruff → mypy; pauses on errors without exiting.
REM -----------------------------------------------------------------------------

echo ==============================================
echo  Running Black formatter
echo ==============================================
black .
if errorlevel 1 (
    echo ERROR: Black encountered errors.
    pause
)

echo.
echo ==============================================
echo  Running isort (import sorter)
echo ==============================================
isort .
if errorlevel 1 (
    echo ERROR: isort encountered errors.
    pause
)

echo.
echo ==============================================
echo  Running Ruff lint check
echo ==============================================
ruff check .
if errorlevel 1 (
    echo.
    echo Ruff found lint issues, applying auto-fix...
    echo ruff check --fix .
	ruff check --fix .
    echo Re-running Ruff lint check
    echo ruff check .
	ruff check .
    if errorlevel 1 (
        echo ERROR: Ruff still reports issues after auto-fix.
        pause
    ) else (
        echo All Ruff issues auto-fixed successfully.
    )
) else (
    echo Ruff check passed with no issues.
)

echo.

echo ==============================================
echo  All formatting & linting steps complete.
echo ==============================================
pause

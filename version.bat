@echo off
REM PDF Merger Version and Release Management Script
REM Semantic Versioning Support

setlocal enabledelayedexpansion

if "%1"=="" (
    goto show_help
)

if /i "%1"=="--version" goto show_version
if /i "%1"=="--help" goto show_help
if /i "%1"=="bump" goto bump_version
if /i "%1"=="release" goto create_release
if /i "%1"=="info" goto show_info

goto show_help

:show_version
echo PDF Merger v1.0.0
exit /b 0

:show_info
echo.
echo ========================================
echo PDF Merger Release Information
echo ========================================
echo.
echo Version: 1.0.0
echo Release Date: 2026-04-18
echo Status: Stable
echo.
echo Key Features in v1.0.0:
echo   - Recursive PDF file discovery
echo   - Intelligent PDF merging based on filename patterns
echo   - Multi-digit filename support (e.g., document-10.pdf^)
echo   - Directory structure preservation
echo.
echo Installation:
echo   1. Run: release.bat
echo   2. Extract the generated pdf_merger_v1.0.0_windows folder
echo   3. Place PDFs in the 'in' folder
echo   4. Run: pdf_merger.bat
echo.
exit /b 0

:bump_version
echo Semantic Versioning available for future releases
echo Current version: 1.0.0
echo.
echo Usage for future releases:
echo   version.bat bump major    (e.g., 1.0.0 ^-^> 2.0.0^)
echo   version.bat bump minor    (e.g., 1.0.0 ^-^> 1.1.0^)
echo   version.bat bump patch    (e.g., 1.0.0 ^-^> 1.0.1^)
exit /b 0

:create_release
echo Creating release package for v1.0.0...
call release.bat
exit /b %errorlevel%

:show_help
echo.
echo PDF Merger v1.0.0 - Version Management
echo.
echo Usage: version.bat [COMMAND]
echo.
echo Commands:
echo   --version              Show current version
echo   --help                 Show this help message
echo   info                   Show release information
echo   release                Create release package for Windows
echo   bump                   Semantic versioning utilities (future^)
echo.
echo Examples:
echo   version.bat --version
echo   version.bat info
echo   version.bat release
echo.
exit /b 0

@echo off
REM PDF Merger v1.0.0 Release Script for Windows
REM This script packages the PDF Merger application for Windows distribution

setlocal enabledelayedexpansion

REM Define variables
set VERSION=1.0.0
set PROJECT_NAME=pdf_merger
set BUILD_DIR=build
set DIST_DIR=dist
set RELEASE_NAME=%PROJECT_NAME%_v%VERSION%_windows
set PYTHON_MIN_VERSION=3.10

echo.
echo ========================================
echo PDF Merger v%VERSION% Release Build
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python %PYTHON_MIN_VERSION% or higher
    pause
    exit /b 1
)

echo [1/5] Checking Python version...
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Found Python %PYTHON_VERSION%

REM Clean previous builds
echo.
echo [2/5] Cleaning previous builds...
if exist %BUILD_DIR% rmdir /s /q %BUILD_DIR%
if exist %DIST_DIR% rmdir /s /q %DIST_DIR%
if exist %RELEASE_NAME% rmdir /s /q %RELEASE_NAME%
echo Previous builds cleaned

REM Create release directory
echo.
echo [3/5] Creating release package...
mkdir %RELEASE_NAME%
mkdir %RELEASE_NAME%\in
mkdir %RELEASE_NAME%\out

REM Copy application files
echo Copying application files...
xcopy "*.py" "%RELEASE_NAME%\" /E /I /Y >nul
xcopy "merger" "%RELEASE_NAME%\merger" /E /I /Y >nul
xcopy "dir" "%RELEASE_NAME%\dir" /E /I /Y >nul
xcopy "infrastructure" "%RELEASE_NAME%\infrastructure" /E /I /Y >nul
xcopy "shared" "%RELEASE_NAME%\shared" /E /I /Y >nul 2>nul
copy "README.md" "%RELEASE_NAME%\" >nul
copy "CHANGELOG.md" "%RELEASE_NAME%\" >nul
copy "LICENSE" "%RELEASE_NAME%\" >nul
copy "Pipfile" "%RELEASE_NAME%\" >nul

REM Create requirements.txt from Pipfile
echo.
echo [4/5] Installing dependencies...
python -m pip install --upgrade pip setuptools wheel >nul 2>&1

REM Create requirements.txt if it doesn't exist
if not exist "requirements.txt" (
    (
        echo pypdf2
    ) > "%RELEASE_NAME%\requirements.txt"
) else (
    copy "requirements.txt" "%RELEASE_NAME%\" >nul
)

REM Install dependencies in the release directory
cd "%RELEASE_NAME%"
python -m pip install -r requirements.txt --target .\libs --quiet
cd ..

REM Create batch file wrapper for easy execution
echo.
echo [5/5] Creating Windows launcher...
(
    echo @echo off
    echo REM PDF Merger v%VERSION% - Windows Launcher
    echo title PDF Merger v%VERSION%
    echo python main.py %%*
    echo if errorlevel 1 (
    echo     echo.
    echo     echo An error occurred. Press any key to exit...
    echo     pause
    echo )
) > "%RELEASE_NAME%\pdf_merger.bat"

REM Create alternative Python wrapper
(
    echo @echo off
    echo REM PDF Merger v%VERSION% - Direct Python Launcher
    echo python "%~dp0main.py" %%*
) > "%RELEASE_NAME%\run.bat"

REM Create installation instructions
(
    echo # PDF Merger v%VERSION% - Windows Installation
    echo.
    echo ## Quick Start
    echo.
    echo 1. Extract this folder to your desired location
    echo 2. Place PDF files in the `in` folder, organized in subdirectories
    echo 3. Double-click `pdf_merger.bat` to run the merger
    echo 4. Check the `out` folder for merged results
    echo.
    echo ## Requirements
    echo.
    echo - Python %PYTHON_MIN_VERSION% or higher
    echo - PyPDF2 (automatically installed^)
    echo.
    echo ## Usage
    echo.
    echo Simply run `pdf_merger.bat` or `run.bat` from the command line:
    echo.
    echo ```
    echo pdf_merger.bat
    echo ```
    echo.
    echo ## Documentation
    echo.
    echo See README.md for complete documentation and usage instructions.
) > "%RELEASE_NAME%\INSTALL.md"

REM Create version file
(
    echo VERSION=1.0.0
    echo BUILD_DATE=%date%
    echo BUILD_TIME=%time%
) > "%RELEASE_NAME%\version.txt"

REM Create compressed archive
echo.
echo Creating compressed archive...
if exist "%RELEASE_NAME%.zip" del "%RELEASE_NAME%.zip"

REM Try to use Windows built-in compression if available
powershell -NoProfile -Command "Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::CreateFromDirectory('!CD!\%RELEASE_NAME%', '!CD!\%RELEASE_NAME%.zip')" >nul 2>&1

if errorlevel 1 (
    echo WARNING: Could not create ZIP archive. Using uncompressed folder instead.
) else (
    echo ZIP archive created successfully
)

echo.
echo ========================================
echo Build Complete!
echo ========================================
echo.
echo Release Package: %RELEASE_NAME%
echo.
echo What's included:
echo   - Application files (main.py, merger/, dir/, infrastructure/)
echo   - Documentation (README.md, CHANGELOG.md, INSTALL.md)
echo   - LICENSE file
echo   - Sample input and output directories
echo   - Windows batch launchers (pdf_merger.bat, run.bat^)
echo   - Python dependencies (if libs folder created^)
echo.
echo Next Steps:
echo   1. Review the CHANGELOG.md for version history
echo   2. Test with sample PDF files in the 'in' folder
echo   3. Run: pdf_merger.bat
echo.
echo For distribution, compress the '%RELEASE_NAME%' folder
echo or use the generated '%RELEASE_NAME%.zip' file
echo.
pause

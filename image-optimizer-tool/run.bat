@echo off
title Shopfa Image Optimizer Server
echo ======================================================
echo          Shopfa Smart Image Optimizer
echo ======================================================
echo.
echo Checking Python prerequisites...
echo.

:: Check python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to PATH.
    echo Please install Python and check 'Add Python to PATH' during installation.
    echo.
    pause
    exit /b
)

:: Check if pip is installed
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] pip package manager not found. Installing automatically...
    python -m ensurepip --default-pip
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to install pip automatically.
        echo Please reinstall Python and make sure pip is checked.
        pause
        exit /b
    )
)

:: Install dependencies
echo Installing/Updating required libraries (Flask and Pillow)...
python -m pip install --upgrade pip >nul 2>&1
python -m pip install flask pillow

if %errorlevel% neq 0 (
    echo [WARNING] Some dependencies failed to install. Please check your internet connection.
)

echo.
echo Starting local server...
echo.
echo Your browser will automatically open in a few seconds.
echo Server Address: http://127.0.0.1:5000
echo To stop the server, close this window or press Ctrl+C.
echo.

python app.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] The server crashed or failed to start.
    pause
)

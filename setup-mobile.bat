@echo off
REM Mobile App Setup Script for Windows
REM This script sets up the environment and builds the Android APK

echo ===================================
echo Medical LLM Tutor - Mobile Setup
echo ===================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.10+ from https://www.python.org/
    pause
    exit /b 1
)

echo ✓ Python found

REM Install Kivy and Buildozer
echo.
echo Installing Kivy and Buildozer...
pip install kivy buildozer cython

echo.
echo Installing mobile requirements...
pip install -r requirements-mobile.txt

echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. Install Java Development Kit (JDK) 11+
echo 2. Install Android SDK
echo 3. Set JAVA_HOME environment variable
echo 4. Run: buildozer android debug
echo.
echo For more details, see MOBILE_DEPLOYMENT.md
echo.
pause

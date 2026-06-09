#!/bin/bash
# Mobile App Setup Script for macOS/Linux

echo "==================================="
echo "Medical LLM Tutor - Mobile Setup"
echo "==================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.10+ from https://www.python.org/"
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo ""

# Install Kivy and Buildozer
echo "Installing Kivy and Buildozer..."
pip3 install kivy buildozer cython

echo ""
echo "Installing mobile requirements..."
pip3 install -r requirements-mobile.txt

echo ""
echo "Setup complete!"
echo ""
echo "Next steps for Android:"
echo "1. Install Java Development Kit (JDK) 11+"
echo "2. Install Android SDK"
echo "3. Set JAVA_HOME environment variable"
echo "4. Run: buildozer android debug"
echo ""
echo "Next steps for iOS (macOS only):"
echo "1. pip install kivy-ios"
echo "2. toolchain create Medical_LLM_Tutor ."
echo ""
echo "For more details, see MOBILE_DEPLOYMENT.md"

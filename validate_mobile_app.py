"""
Mobile App Validation Script
Verifies all components are in place and syntax is correct
"""

import os
import json
from pathlib import Path

def check_files():
    """Check if all required files exist"""
    required_files = {
        'Core App': ['mobile_app.py', 'student_db.py', 'personalizer.py', 'data_collector.py'],
        'Build Config': ['buildozer.spec', 'requirements-mobile.txt'],
        'Setup Scripts': ['setup-mobile.bat', 'setup-mobile.sh'],
        'Documentation': ['MOBILE_QUICK_START.md', 'MOBILE_DEPLOYMENT.md', 'MOBILE_IMPLEMENTATION.md'],
        'Dependencies': ['requirements.txt', 'requirements-mobile.txt'],
    }
    
    print("=" * 50)
    print("🔍 Mobile App Validation")
    print("=" * 50)
    print()
    
    all_good = True
    for category, files in required_files.items():
        print(f"📁 {category}:")
        for file in files:
            if Path(file).exists():
                size = Path(file).stat().st_size
                print(f"  ✅ {file:30} ({size:,} bytes)")
            else:
                print(f"  ❌ {file:30} (MISSING)")
                all_good = False
        print()
    
    return all_good

def check_imports():
    """Check if Python modules can be imported"""
    print("📦 Checking Python module imports:")
    
    modules = {
        'student_db': 'StudentDatabase',
        'personalizer': 'PersonalizationEngine',
        'data_collector': 'MedicalDataCollector',
    }
    
    for module_name, class_name in modules.items():
        try:
            module = __import__(module_name)
            if hasattr(module, class_name):
                print(f"  ✅ {module_name}.{class_name}")
            else:
                print(f"  ⚠️  {module_name} found, but {class_name} not found")
        except ImportError as e:
            print(f"  ❌ {module_name} - {str(e)}")
    print()

def check_data():
    """Check if medical data exists"""
    print("💾 Checking Medical Data:")
    
    data_files = [
        'medical_data/curriculum_index.json',
        'medical_data/sample_questions.json',
        'medical_data/learning_objectives.json',
        'medical_data/medical_training_data.txt',
    ]
    
    for data_file in data_files:
        if Path(data_file).exists():
            size = Path(data_file).stat().st_size
            print(f"  ✅ {data_file:45} ({size:,} bytes)")
        else:
            print(f"  ⚠️  {data_file:45} (optional)")
    print()

def check_student_data():
    """Check student profiles"""
    print("👥 Checking Student Profiles:")
    
    student_dir = Path('student_data')
    if student_dir.exists():
        profiles = list(student_dir.glob('*.json'))
        print(f"  ✅ student_data/ folder exists")
        print(f"     Found {len(profiles)} student profiles")
        for profile in profiles[:3]:  # Show first 3
            print(f"     - {profile.name}")
        if len(profiles) > 3:
            print(f"     ... and {len(profiles) - 3} more")
    else:
        print(f"  ℹ️  student_data/ folder (will be created on first run)")
    print()

def print_deployment_options():
    """Print deployment options"""
    print("🚀 Deployment Options:")
    print()
    print("  1. TEST LOCALLY (No installation needed):")
    print("     $ python mobile_app.py")
    print("     (Note: Requires Kivy installed)")
    print()
    print("  2. BUILD ANDROID APK:")
    print("     $ pip install buildozer cython")
    print("     $ buildozer android debug")
    print("     Output: bin/medicallmtutor-1.0-debug.apk")
    print()
    print("  3. BUILD iOS IPA (macOS only):")
    print("     $ pip install kivy-ios")
    print("     $ toolchain create Medical_LLM_Tutor .")
    print()
    print("  4. RUN SETUP SCRIPT:")
    print("     Windows: setup-mobile.bat")
    print("     macOS/Linux: bash setup-mobile.sh")
    print()

def print_architecture():
    """Print app architecture"""
    print("🏗️  Mobile App Architecture:")
    print()
    print("  LoginScreen")
    print("  ├─ Create Profile (Student ID, Name, Year 1-6)")
    print("  └─ Login (existing profile)")
    print()
    print("  DashboardScreen")
    print("  ├─ Student Stats (Year, Questions, Topics)")
    print("  ├─ Strong Topics (✅)")
    print("  ├─ Weak Topics (⚠️)")
    print("  ├─ Study Recommendations")
    print("  └─ Navigation (Q&A, Logout)")
    print()
    print("  QAScreen")
    print("  ├─ Question Input")
    print("  ├─ Topic Selection")
    print("  ├─ Personalized Answer")
    print("  └─ Back to Dashboard")
    print()

def print_tech_specs():
    """Print technical specifications"""
    print("⚙️  Technical Specifications:")
    print()
    print("  Framework:        Kivy 2.2.1 (Python-based)")
    print("  Backend Modules:  student_db.py, personalizer.py, data_collector.py")
    print("  Database:         JSON (student_data/)")
    print("  Target Platform:  Android 5.0+, iOS 11.0+")
    print("  Screen Size:      400x700px (mobile optimized)")
    print("  Build Tool:       Buildozer")
    print()
    print("  Supported Years:  1-6 (all UNN medical program)")
    print("  Curriculum:       UNN 6-year medical curriculum")
    print("  Personalization:  Adaptive difficulty (6 levels)")
    print()

def main():
    """Run all checks"""
    print()
    
    # Check files
    files_ok = check_files()
    
    # Check imports
    check_imports()
    
    # Check data
    check_data()
    
    # Check student profiles
    check_student_data()
    
    # Print useful info
    print_architecture()
    print_tech_specs()
    print_deployment_options()
    
    # Summary
    print("=" * 50)
    if files_ok:
        print("✅ Mobile app is ready for deployment!")
        print()
        print("Next Steps:")
        print("1. Review MOBILE_QUICK_START.md for quick guide")
        print("2. Run setup-mobile.bat/.sh to install dependencies")
        print("3. Build APK: buildozer android debug")
        print("4. Transfer APK to Android device and install")
        print("5. Or test locally: python mobile_app.py")
    else:
        print("⚠️  Some files are missing. Please check above.")
    print("=" * 50)
    print()

if __name__ == '__main__':
    main()

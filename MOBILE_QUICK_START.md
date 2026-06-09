# 📱 Mobile App Quick Start

## Getting the App on Your Phone

### Option 1: Download Pre-built APK (Easiest)
*(Coming soon - we'll provide direct APK download link)*

### Option 2: Build It Yourself

#### For Windows:
```bash
cd c:\Users\HI\Documents\personal_project
setup-mobile.bat
buildozer android debug
```

#### For macOS/Linux:
```bash
cd personal_project
bash setup-mobile.sh
buildozer android debug
```

## First Time Using the App

### Step 1: Create Your Profile
1. Tap **"Create Profile"**
2. Enter your Student ID (e.g., `MED001` or `2024/MED/001`)
3. Enter your Full Name
4. Select your Medical School Year (1-6)
5. Tap **"Create Profile"**

### Step 2: Ask a Question
1. Tap **"Ask Question"** button
2. Type your medical question (e.g., "What is the function of the pancreas?")
3. Select the Topic (Anatomy, Pharmacology, etc.)
4. Tap **"Get Personalized Answer"**
5. Get a personalized, year-appropriate response!

### Step 3: Check Your Progress
1. Go back to **Dashboard**
2. See your Strong Topics (things you know well)
3. See Topics Needing Improvement
4. Get a recommendation for what to study next

## Features

📚 **Personalized Learning**
- Answers adjust to your year level
- Questions tracked automatically
- Weak areas highlighted

🎓 **6-Year Medical Program**
- Anatomy, Physiology, Pharmacology, etc.
- Preclinical (Years 1-3) content
- Clinical (Years 3-6) content

📊 **Learning Dashboard**
- Track your progress
- See which topics you're strong in
- Get study recommendations

🔐 **Offline Ready**
- Most features work without internet
- Data saved locally on your phone

## Tips for Best Results

1. **Be Specific**: Ask detailed questions for better answers
2. **Choose Right Topic**: Selecting the correct topic helps with personalization
3. **Regular Practice**: Ask questions regularly for accurate tracking
4. **Review Weak Topics**: Focus on topics marked as "needing improvement"

## Troubleshooting

**Q: Can't find my profile after restarting?**
- A: Profiles are saved automatically. Use your Student ID to login.

**Q: App is slow?**
- A: Close other apps and try again. Clear old data if needed.

**Q: Answers seem generic?**
- A: The app learns from your questions. Ask more for personalization!

**Q: Need to reinstall?**
- A: Your data is saved. Just create your profile again with the same Student ID.

## Campus Features (Coming Soon)

🔄 **Sync with Study Groups**
⭐ **Achievements & Badges**
🏆 **Leaderboards**
📈 **Advanced Analytics**
💬 **Peer Discussion Forums**

## File Sizes

- **Android APK**: ~60-80 MB
- **Storage on Phone**: ~5-10 MB (per 100 profiles)
- **Memory While Running**: ~100-150 MB

## Device Requirements

- **Android**: Version 5.0 (Lollipop) or higher
- **iOS**: Version 11.0 or higher
- **Storage**: At least 100 MB free space

## Getting Help

1. Check [MOBILE_DEPLOYMENT.md](MOBILE_DEPLOYMENT.md) for detailed guide
2. Review [README.md](README.md) for overall project info
3. Check [QUICK_START.md](QUICK_START.md) for general usage

## Want to Contribute?

The mobile app is built with Kivy (Python-based). You can:
- Add new features
- Improve the UI
- Optimize performance
- Fix bugs

See the main codebase structure:
- `mobile_app.py` - Main app interface
- `student_db.py` - Student data management
- `personalizer.py` - Learning personalization
- `data_collector.py` - Medical curriculum

---

**Happy Learning! 🎓📱**

University of Nigeria Nsukka - Medical LLM Tutor v1.0

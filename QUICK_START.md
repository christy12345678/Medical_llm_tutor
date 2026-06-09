# 🚀 Quick Start Guide - UNN Medical LLM

## Getting Started with Medical LLM Tutor (University of Nigeria Nsukka)

### Customized for UNN 6-Year Program
This system is fully integrated with University of Nigeria Nsukka's medical curriculum!

### Step 1: Verify Installation ✅
All required modules are already tested and working!

```
✓ student_db.py       - Student profiles working
✓ personalizer.py     - Personalization engine working  
✓ data_collector.py   - Medical data collected
✓ model_trainer.py    - Model trainer ready
✓ app.py              - Web interface ready
✓ Streamlit           - Installed and ready
```

### Step 2: Run the Application 🚀

Open your terminal and run:

```bash
cd C:\Users\HI\Documents\personal_project
streamlit run app.py
```

This will:
1. Start a local web server
2. Open the app at `http://localhost:8501`
3. Show you the Medical LLM Tutor interface

### Step 3: Create Your Student Profile 🎓

1. Go to **"Student Login"** page
2. Click **"Create Profile"** tab
3. Enter:
   - Student ID: (e.g., MED001 or 2024/MED/001)
   - Full Name: (your name)
   - Medical School Year: 1, 2, 3, 4, 5, or 6
   - Specialization: (optional, e.g., "Interested in Surgery")
4. Click **"Create Profile"**

### Step 4: Start Using the System 💡

**Ask Questions:**
- Go to **"Q&A Assistant"**
- Type your medical question
- Select the topic
- Rate your confidence level
- Get personalized answer

**Track Progress:**
- Go to **"Learning Dashboard"**
- See your strong and weak topics
- Get recommendations
- View learning path

**Access Resources:**
- Go to **"Resources"**
- Find recommended materials for your year

## What's Different Each Year?

### Year 1 Students
- Simpler explanations for foundational sciences
- Focus on Chemistry, Biology, Physics basics
- More basic examples per topic
- Topics: CHM 101, BIO 101, PHY 101

### Year 2 Students  
- Intermediate depth with mechanisms explained
- Anatomy, Biochemistry, Physiology
- 2-3 examples per topic
- Topics: ANA 201, BIC 201, PYS 201

### Year 3 Students
- Advanced clinical focus with patient cases
- Pharmacology, Pathology, Clinical Medicine intro
- Multiple detailed clinical examples
- Topics: PHA 301, PAT 301, MED 301, SUG 301

### Year 4 Students
- Expert-level clinical content
- Specialization-focused (OB/GYN, Pediatrics, Surgery)
- Complex case discussions
- Topics: OBG 401, PAE 410, SUG courses

### Year 5 Students
- Specialized rotations focus
- Evidence-based specialty medicine
- Real patient management cases
- Topics: OBG 503, COM 502, Specialty clinics

### Year 6 Students
- Final year practice excellence
- Medical ethics and leadership
- Research-oriented advanced topics
- Topics: MED 601, SUG 601, MED 610

## Features to Explore

### 🎯 Smart Personalization
The system remembers:
- Your year of study
- Your strong topics (boost difficulty)
- Your weak topics (simplify explanations)
- Your previous questions

### 📊 Learning Dashboard
Shows:
- Topics you're strong at ✅
- Topics needing improvement ⚠️
- Personalized recommendations 🎯
- What to study next 📚

### 🧠 Adaptive Explanations
Each answer is customized:
- To your medical school year
- To your previous performance
- With appropriate examples
- At the right difficulty level

## File Generated

When you use the system, these are created:

```
personal_project/
├── student_data/              # Your profile storage
│   └── MED001.json           # Your student profile
├── medical_data/              # Medical curriculum
│   ├── curriculum_index.json   # Topics by year
│   ├── sample_questions.json   # Q&A database
│   └── learning_objectives.json
└── models/                    # Trained models (future)
```

## Troubleshooting

### Streamlit won't start?
```bash
# Try with explicit Python path
C:\Users\HI\Documents\personal_project\.venv\Scripts\python.exe -m streamlit run app.py
```

### Port 8501 already in use?
```bash
# Use different port
streamlit run app.py --server.port 8502
```

### Clear all student data?
```bash
# Delete student_data folder to reset
rmdir student_data /s /q
```

## Next Steps 🎯

1. ✅ **Setup Complete** - Run `streamlit run app.py`
2. 🎓 **Create Profile** - Fill in your information
3. 💬 **Ask Questions** - Start learning with personalization
4. 📊 **View Dashboard** - Track your progress
5. 🚀 **Deploy** - Share with other students

## Advanced Features (Coming Soon)

- 🤖 Fine-tuned LLM model
- 📱 Mobile app version
- 🎮 Gamified learning
- 👥 Study groups
- 📈 Analytics dashboard
- 🌍 Multiple languages

## Need Help?

- Check **README.md** for detailed documentation
- Review **PROJECT_PLAN.md** for architecture
- Look at module docstrings in Python files

---

**You're all set! 🎉**

Now run: `streamlit run app.py`

Good luck with your medical studies! 🏥

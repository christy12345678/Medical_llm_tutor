# 🏥 Medical LLM Tutor - Personalized AI Learning Platform

A comprehensive AI-powered learning system tailored for University of Nigeria Nsukka medical students (6-year program), providing personalized answers aligned with UNN's medical curriculum.

## Features

✨ **Key Features:**
- 🎓 **Comprehensive Curriculum**: Complete 6-year medical school curriculum
- 🧠 **Personalized Learning**: Answers adapted to student level and weak areas
- 📊 **Progress Tracking**: Monitor learning progress across topics
- 🎯 **Smart Recommendations**: AI-powered suggestions for what to study next
- 💡 **Adaptive Difficulty**: Automatically adjusts explanation complexity
- 📚 **Multi-source**: Combines textbooks, Q&A, and clinical cases
- 🌐 **Web Interface**: Easy-to-use Streamlit dashboard
- 📱 **Mobile App**: Native Android/iOS app for on-the-go learning

## Available Interfaces

### 🌐 Web Interface (Streamlit)
- Browser-based access
- Full feature set
- Easy cloud deployment
- **Getting Started**: See [QUICK_START.md](QUICK_START.md)

### 📱 Mobile App (Kivy)
- Native Android APK
- Native iOS IPA
- Offline-capable
- Optimized for mobile experience
- **Getting Started**: See [MOBILE_QUICK_START.md](MOBILE_QUICK_START.md)
- **Detailed Guide**: See [MOBILE_DEPLOYMENT.md](MOBILE_DEPLOYMENT.md)

## System Architecture

```
┌─────────────────────────────────────────────┐
│      Streamlit Web Interface (app.py)       │
├─────────────────────────────────────────────┤
│         Student Profile Management          │
│           (student_db.py)                   │
├─────────────────────────────────────────────┤
│         Personalization Engine              │
│          (personalizer.py)                  │
├─────────────────────────────────────────────┤
│         Medical LLM Model                   │
│        (model_trainer.py)                   │
├─────────────────────────────────────────────┤
│        Data & Curriculum                    │
│      (data_collector.py)                    │
└─────────────────────────────────────────────┘
```

## Installation

### Prerequisites
- Python 3.8+
- pip or conda
- Virtual environment (recommended)

### Setup Instructions

1. **Clone/Download the project:**
```bash
cd personal_project
```

2. **Create virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application:**
```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

## Usage

### 1. Create Student Profile
- Navigate to "Student Login" page
- Click "Create Profile" tab
- Fill in your details:
  - Student ID
  - Full Name
  - Medical School Year (1-4)
  - Specialization (optional)

### 2. Ask Questions
- Go to "Q&A Assistant"
- Enter your medical question
- Select the topic
- Indicate your confidence level
- Get personalized answer tailored to your year

### 3. Track Progress
- View "Learning Dashboard"
- See strong and weak topics
- Get personalized recommendations
- Monitor improvement over time

### 4. Access Resources
- Browse "Resources" page
- Find recommended textbooks and platforms
- Get topic-specific learning materials

## Project Structure

```
personal_project/
├── app.py                      # Main Streamlit web interface
├── mobile_app.py              # Mobile app interface (Kivy)
├── student_db.py              # Student profile & database system
├── personalizer.py            # Personalization engine
├── model_trainer.py           # LLM training module
├── data_collector.py          # Curriculum data collection
├── requirements.txt           # Web app dependencies
├── requirements-mobile.txt    # Mobile app dependencies
├── buildozer.spec            # Mobile build configuration
├── setup-mobile.bat          # Mobile setup (Windows)
├── setup-mobile.sh           # Mobile setup (macOS/Linux)
├── PROJECT_PLAN.md           # Detailed project roadmap
├── QUICK_START.md            # Web app quick start guide
├── MOBILE_QUICK_START.md     # Mobile app quick start guide
├── MOBILE_DEPLOYMENT.md      # Mobile deployment guide
├── UNN_CURRICULUM.md         # Curriculum details
├── student_data/             # Student profiles (auto-created)
└── medical_data/             # Medical curriculum data (auto-created)
```

## Core Modules

### `app.py`
Streamlit web application with pages:
- **Home**: Introduction and features
- **Student Login**: Create/login to student account
- **Q&A Assistant**: Ask medical questions
- **Learning Dashboard**: View progress and recommendations
- **Resources**: Access learning materials

### `student_db.py`
Student profile management:
- Student profiles with year and learning history
- Track weak and strong topics
- Record questions and performance scores
- Generate learning focus areas

### `personalizer.py`
Personalization engine:
- Adapt answer difficulty to student year
- Adjust based on previous performance
- Generate learning recommendations
- Suggest next topics to study

### `model_trainer.py`
LLM training module:
- Build and train medical LLM
- Manage curriculum data
- Evaluate model performance
- Save/load trained models

### `data_collector.py`
Data collection system:
- Medical curriculum index (Year 1-4)
- Sample Q&A pairs
- Learning objectives
- Training data compilation

## Curriculum Organization

### Year 1 - Foundation
- Anatomy
- Physiology
- Biochemistry

### Year 2 - Mechanisms
- Pathology
- Pharmacology
- Microbiology

### Year 3 - Clinical
- Internal Medicine
- Surgery
- Pediatrics

### Year 4 - Specialization
- Radiology
- Psychiatry
- Neurology

## Personalization Strategy

The system personalizes responses in multiple ways:

1. **By Student Year**
   - Year 1: Simple overview, basic concepts
   - Year 2: Intermediate detail
   - Year 3: Advanced, clinical-focused
   - Year 4: Expert level, research-oriented

2. **By Performance History**
   - Weak topics: Simplified explanations
   - Strong topics: More challenging content
   - Mixed performance: Balanced approach

3. **By Learning Progress**
   - Tracks comprehension scores
   - Identifies improvement areas
   - Recommends focus topics

## Example Workflow

```
1. Student creates profile (Year 2)
   ↓
2. Asks: "What is glycolysis?"
   ↓
3. System checks: Year 2 + strong biochemistry
   ↓
4. Generates answer with:
   - Intermediate difficulty
   - 2-3 clinical examples
   - Focus on metabolism pathways
   ↓
5. Scores response (comprehension = 75%)
   ↓
6. System updates profile
   ↓
7. Next time: Recommends related topics
```

## Development Roadmap

### Phase 1: Foundation ✓
- [x] Student profile system
- [x] Personalization engine
- [x] Web interface
- [x] Data collector

### Phase 2: Model Integration
- [ ] Fine-tune GPT-2 on medical data
- [ ] Integrate LLM into Q&A system
- [ ] Test model performance

### Phase 3: Enhancement
- [ ] Add more medical topics
- [ ] Implement spaced repetition
- [ ] Add study materials/flashcards
- [ ] Implement peer learning features

### Phase 4: Production
- [ ] Deploy to cloud
- [ ] Add authentication system
- [ ] Implement analytics
- [ ] Scale infrastructure

## Configuration

### Modify Difficulty Levels
Edit `personalizer.py`:
```python
DIFFICULTY_MAP = {
    1: "simple_overview",
    2: "intermediate",
    3: "advanced",
    4: "expert"
}
```

### Add New Medical Topics
Edit `data_collector.py`:
```python
medical_topics = [
    {"topic": "New Topic", "year": 1, "subtopics": [...]},
    ...
]
```

### Adjust Training Parameters
Edit `model_trainer.py`:
```python
trainer = MedicalLLMTrainer()
model = trainer.build_model(vocab_size=5000, embedding_dim=256)
model = trainer.train(model, data, epochs=50, batch_size=64)
```

## Testing

Run individual modules:

```bash
# Test student database
python student_db.py

# Test personalization engine
python personalizer.py

# Test data collection
python data_collector.py

# Test model trainer
python model_trainer.py
```

## Troubleshooting

### Issue: Module not found errors
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: Streamlit not starting
**Solution:**
```bash
streamlit run app.py --logger.level=debug
```

### Issue: PyTorch installation problems
**Solution:**
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

## Performance Tips

1. **Speed up LLM responses**
   - Use GPU if available
   - Implement caching for common questions
   - Use quantization for model compression

2. **Improve recommendations**
   - Collect more student performance data
   - Fine-tune model on real medical data
   - Implement collaborative filtering

3. **Scale the system**
   - Use database instead of JSON files
   - Implement API backend
   - Deploy with Docker/Kubernetes

## Contributing

To add features:

1. Create a feature branch
2. Implement changes
3. Test thoroughly
4. Submit for review

## Future Enhancements

- 🔄 Real-time model updates
- 📱 Mobile app version
- 🎮 Gamification (points, badges)
- 👥 Peer learning features
- 📈 Advanced analytics
- 🌍 Multi-language support
- 🎤 Voice Q&A
- 📹 Video explanations

## License

This project is for educational purposes.

## Support

For issues or questions:
1. Check the PROJECT_PLAN.md
2. Review module documentation
3. Check example usage in main blocks

---

**Happy Learning! 🎓**

*Medical LLM Tutor - Personalized AI Education for Medical Excellence*

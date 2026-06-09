# Medical LLM - Project Roadmap

## Phase 1: Foundation (Week 1-2)
- [ ] Data collection & preprocessing
- [ ] Set up training infrastructure
- [ ] Basic LLM training on medical content
- [ ] Student profile system

## Phase 2: Personalization (Week 3)
- [ ] Implement learning level tracking
- [ ] Track topic performance
- [ ] Create learning recommendations
- [ ] Weak topic identification

## Phase 3: Web Interface (Week 4)
- [ ] Streamlit UI for students
- [ ] Authentication system
- [ ] Student dashboard
- [ ] Real-time Q&A

## Phase 4: Optimization (Week 5+)
- [ ] Model fine-tuning
- [ ] Performance improvements
- [ ] User testing & feedback

---

## Data Sources
1. **Medical Textbooks**: OpenStax, Wikipedia medical articles
2. **Q&A Datasets**: MedQA, HealthQA
3. **Curriculum**: USMLE, MBBS syllabus
4. **Student Progress**: Tracked via database

## Key Components
- `data_collector.py` - Fetch medical content
- `model_trainer.py` - Train LLM
- `personalizer.py` - Personalization logic
- `student_db.py` - Student profiles & progress
- `app.py` - Streamlit web interface

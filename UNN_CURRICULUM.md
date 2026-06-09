# 🏥 Medical LLM Tutor - University of Nigeria Nsukka Integration

## Overview

This system has been customized for **University of Nigeria Nsukka's medical curriculum**, featuring a complete 6-year medical education program (Years 1-6).

## Curriculum Structure

### **Preclinical Phase (Years 1-2)**
Foundation in basic medical sciences

**Year 1 - Foundational Sciences (GPA for preparation)**
- Chemistry (CHM 101, 111, 121) - 6 units
- Biology (BIO 101, 151, 152, 153) - 6 units  
- Physics (PHY 101, 191, 102, 103) - 7 units
- General Studies (GS 111, 102, 202, 207, 208) - 5 units
- **Total: ~38 units**

**Year 2 - Preclinical Sciences Advancement**
- Gross Anatomy (ANA 201-206) - 11 units
- Biochemistry (BIC 201, 203, 208) - 7 units
- Physiology (PYS 201, 202, 203, 204) - 11 units
- Philosophy (PHIL 131, 132) - 3 units
- **Total: ~30 units**

### **Clinical Phase (Years 3-6)**
Clinical training and specialization

**Year 3 - Clinical Introduction**
- General Pharmacology (PHA 301, 302) - 4 units
- Microbiology (MIC 302) - 2 units
- Clinical Chemistry (CPT 301, 302, 304) - 5 units
- Pathology (PAT 301) - 1 unit
- **Clinical Medicine** (MED 301-309) - Cardiology, Respiratory, GI, Nephrology, Neurology, Hematology
- **Clinical Surgery** (SUG 301-306) - General, GI, Congenital, Urology, Trauma
- **Total: ~43 units**

**Year 4 - Advanced Clinical**
- Advanced Pharmacology (PHA 401-405) - 4 units
- Medical Microbiology (MIC 401-405) - 5 units
- Hematology (HEM 401-403) - 4 units
- Obstetrics & Gynaecology (OBG 401-402) - 6 units
- Pediatrics (PAE 410, 402) - 3 units
- Forensic Medicine (PAT 403) - 2 units
- **Total: ~27 units**

**Year 5 - Specialized Clinical Rotations**
- Obstetric Clinics (OBG 503) - 8 units
- Pediatric Clinics (PAE 501-504) - Multiple units
- Community Health (COM 502-504) - 12 units
- **Total: ~30 units**

**Year 6 - Final Clinical Year**
- Advanced Internal Medicine (MED 601-608) - Specialties including Tropical Medicine
- Advanced Surgery (SUG 601-605) - Cardiothoracic, Neurosurgery, Pediatric, Neurosurgery
- Medical Ethics & Jurisprudence (MED 610-612) - 5 units
- **Total: ~18 units**

## System Customization for UNN

### Files Updated

1. **data_collector.py**
   - Added UNN course codes (ANA 201, BIC 201, PHA 301, etc.)
   - Organized courses by year and semester
   - Created learning objectives matching UNN requirements
   - Updated sample Q&A with UNN curriculum topics

2. **personalizer.py**
   - Extended difficulty levels for 6 years instead of 4
   - `simple_foundation` (Yr 1) → `intermediate_sciences` (Yr 2) → `transition_clinical` (Yr 3) → `clinical_advanced` (Yr 4) → `specialist_clinical` (Yr 5) → `expert_final` (Yr 6)
   - Adaptive recommendations based on UNN year-specific challenges

3. **app.py**
   - Updated year selection to support Years 1-6
   - Updated dashboard text and examples to reflect UNN context

4. **student_db.py**
   - No changes needed (year-agnostic)

5. **model_trainer.py**
   - Prepared curriculum structure matching UNN's 6-year program

### Generated Data Files

Located in `medical_data/` folder:

```
medical_data/
├── curriculum_index.json      # UNN curriculum by year
├── sample_questions.json      # UNN-aligned Q&A pairs with course codes
├── learning_objectives.json   # Objectives for each topic
└── medical_training_data.txt  # Compiled training text
```

## Key Features for UNN Students

### 1. **Preclinical Foundation Support (Years 1-2)**
- Simplified explanations for foundational sciences
- Focus on understanding basic concepts
- Integration of practical chemistry, biology, physics
- Minimal clinical correlation initially

### 2. **Clinical Transition Support (Year 3)**
- Bridging preclinical and clinical knowledge
- Introduction to patient management
- Clinical examination techniques
- Hospital-based learning structure

### 3. **Advanced Clinical Support (Years 4-5)**
- Specialization-specific guidance
- Evidence-based management protocols
- Complex case discussions
- Examination preparation (MBE format)

### 4. **Final Year Support (Year 6)**
- Professional practice guidelines
- Medical-legal and ethical frameworks
- Research methodology
- Career guidance

## Personalization Algorithm

The system adapts based on:

1. **Student Year**
   - Year 1-2: Simple, concept-focused explanations
   - Year 3: Clinical integration begins
   - Year 4-5: Specialization-focused content
   - Year 6: Expert-level, evidence-based guidance

2. **Performance Tracking**
   - Identifies weak areas in pharmacology, surgery, medicine, etc.
   - Recommends focus areas based on past performance
   - Tracks improvement over time

3. **Topic Difficulty**
   - Weak topics: Downgrade to simpler explanations
   - Strong topics: Upgrade to more challenging content
   - Mixed performance: Balanced approach with examples

## Usage Examples

### For a Year 1 Student
**Question:** "What is the citric acid cycle?"
**Response Style:** Simple overview, 1 example, basic biochemistry focus
**Difficulty:** Foundation level

### For a Year 3 Student
**Question:** "What is the citric acid cycle?"
**Response Style:** Clinically relevant, 2-3 examples, links to metabolic disorders
**Difficulty:** Intermediate with clinical application

### For a Year 6 Student
**Question:** "What is the citric acid cycle?"
**Response Style:** Expert-level, research-oriented, 5+ examples, latest evidence
**Difficulty:** Comprehensive with specialty implications

## Course Code Integration

All courses include UNN course codes:
- **Chemistry**: CHM 101, CHM 111, CHM 121
- **Biology**: BIO 101, BIO 151, BIO 152, BIO 153
- **Anatomy**: ANA 201-303
- **Biochemistry**: BIC 201-301
- **Pharmacology**: PHA 301-506
- **Pathology**: PAT 301-403
- **Internal Medicine**: MED 301-612
- **Surgery**: SUG 301-605

And many more following UNN's departmental structure.

## How to Run

```bash
# Activate virtual environment
.venv\Scripts\activate  # Windows

# Run the application
streamlit run app.py

# Create profile for UNN student
- Year: Select 1-6
- Medical School: UNN
- Student ID: Follow UNN format (e.g., 2024/MED/001)
```

## Testing Results

✅ **All modules tested successfully:**
- `data_collector.py` - Generates UNN curriculum
- `personalizer.py` - Adapts to 6-year program
- `student_db.py` - Tracks student progress
- `model_trainer.py` - Ready for model training
- `app.py` - Web interface supports Years 1-6

## Next Steps

1. ✅ **UNN Curriculum Integration** - COMPLETED
2. 📊 **Fine-tune LLM** - Train on medical textbooks and case studies
3. 🎓 **Add MBE Exam Prep** - For professional examination preparation
4. 📱 **Mobile App** - Complement to web interface
5. 🏥 **Hospital Integration** - Connect with teaching hospital
6. 👥 **Student Community** - Study groups and peer learning

## Support & Customization

To modify the curriculum:
1. Edit `data_collector.py` - Update course lists, codes, subtopics
2. Re-run: `python data_collector.py`
3. System automatically regenerates all data files

To adjust difficulty levels:
1. Edit `personalizer.py` - Modify `TOPIC_ADJUSTMENTS`
2. Test with `python personalizer.py`

---

**Medical LLM Tutor for University of Nigeria Nsukka** 🎓
*Supporting medical excellence through personalized AI learning*

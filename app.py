"""
Medical LLM Web Interface
Streamlit app for medical students to get personalized learning assistance
"""
import streamlit as st
import os
from student_db import StudentProfile, StudentDatabase
from personalizer import PersonalizationEngine
from data_collector import MedicalDataCollector

# Page configuration
st.set_page_config(
    page_title="Medical LLM Tutor",
    page_icon="🏥",
    layout="wide"
)

# Initialize session state
if 'student' not in st.session_state:
    st.session_state.student = None
if 'db' not in st.session_state:
    st.session_state.db = StudentDatabase()
if 'personalizer' not in st.session_state:
    st.session_state.personalizer = PersonalizationEngine()

# Sidebar navigation
st.sidebar.title("🏥 Medical LLM Tutor")
page = st.sidebar.radio("Navigate", 
    ["Home", "Student Login", "Q&A Assistant", "Learning Dashboard", "Resources"])

# ============= HOME PAGE =============
if page == "Home":
    st.title("🏥 Medical LLM Tutor")
    st.subheader("Personalized AI Learning for Medical Students")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Features
        - 📚 **Comprehensive Coverage**: Year 1-4 medical curriculum
        - 🎯 **Personalized Learning**: Adapted to your level and weak areas
        - 💡 **Smart Explanations**: Context-aware answers
        - 📊 **Progress Tracking**: Monitor your improvement
        - 🎓 **Recommendations**: Get study suggestions
        """)
    
    with col2:
        st.markdown("""
        ### How It Works
        1. **Sign in** with your information
        2. **Ask questions** about any medical topic
        3. Get **personalized answers** based on your year
        4. Track your **learning progress**
        5. Receive **recommendations** for improvement
        
        > This AI tutor adapts to your learning style and pace!
        """)
    
    st.info("👈 Start by logging in or creating a student profile!")

# ============= STUDENT LOGIN/SIGNUP =============
elif page == "Student Login":
    st.title("Student Authentication")
    
    tab1, tab2 = st.tabs(["Login", "Create Profile"])
    
    with tab1:
        st.subheader("Login to Your Account")
        student_id = st.text_input("Student ID:", key="login_id")
        
        if st.button("Login", key="login_btn"):
            profile = st.session_state.db.load_profile(student_id)
            if profile:
                st.session_state.student = profile
                st.success(f"Welcome back, {profile.name}! 👋")
                st.rerun()
            else:
                st.error("Student ID not found. Please create a new profile.")
    
    with tab2:
        st.subheader("Create New Student Profile")
        col1, col2 = st.columns(2)
        
        with col1:
            new_id = st.text_input("Student ID:")
            name = st.text_input("Full Name:")
        
        with col2:
            year = st.selectbox("Medical School Year:", [1, 2, 3, 4, 5, 6])
            specialization = st.text_input("Specialization (optional):")
        
        if st.button("Create Profile", key="create_btn"):
            if new_id and name:
                new_profile = StudentProfile(new_id, name, year)
                st.session_state.db.save_profile(new_profile)
                st.session_state.student = new_profile
                st.success(f"Profile created! Welcome, {name}! 🎉")
                st.rerun()
            else:
                st.error("Please fill in all required fields")

# ============= Q&A ASSISTANT =============
elif page == "Q&A Assistant":
    if not st.session_state.student:
        st.warning("Please login first! Go to 'Student Login' page.")
    else:
        student = st.session_state.student
        st.title(f"🎓 Q&A Assistant for {student.name}")
        st.subheader(f"Year {student.year} Medical Student")
        
        # Question input
        question = st.text_area("Ask your medical question:", 
                               placeholder="e.g., What is hypertension and how is it treated?")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            topic = st.selectbox("Topic:", 
                                ["Anatomy", "Physiology", "Pharmacology", "Pathology", 
                                 "Internal Medicine", "Surgery", "Pediatrics", "Other"])
        with col2:
            confidence = st.slider("How confident are you?", 0, 100, 50)
        
        if st.button("Get Personalized Answer", key="qa_btn"):
            if question:
                with st.spinner("Generating personalized answer..."):
                    # Get personalization template
                    template = st.session_state.personalizer.get_answer_template(student, topic)
                    
                    # Display answer section
                    st.markdown("### 📖 Your Personalized Answer")
                    st.info(template)
                    
                    # Placeholder answer (in real system, would call fine-tuned LLM)
                    st.markdown("""
                    **Sample Answer:**
                    
                    Hypertension, or high blood pressure, is defined as a systolic pressure ≥140 mmHg 
                    or diastolic pressure ≥90 mmHg. It's a leading cause of cardiovascular disease...
                    
                    [Actual LLM response would appear here with personalized depth and examples]
                    """)
                    
                    # Record the interaction
                    comprehension_score = confidence  # Simplified scoring
                    student.add_question(question, topic, comprehension_score)
                    st.session_state.db.save_profile(student)
                    
                    # Show follow-up suggestions
                    st.markdown("### 💭 Would you like to:")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        if st.button("Ask more details"):
                            st.info("Ask a follow-up question above!")
                    with col2:
                        if st.button("See resources"):
                            st.success("Resources have been bookmarked!")
                    with col3:
                        if st.button("Move to next topic"):
                            st.info(st.session_state.personalizer.suggest_next_topic(student))
            else:
                st.error("Please enter a question!")

# ============= LEARNING DASHBOARD =============
elif page == "Learning Dashboard":
    if not st.session_state.student:
        st.warning("Please login first!")
    else:
        student = st.session_state.student
        st.title(f"📊 Learning Dashboard - {student.name}")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Year", student.year)
        with col2:
            st.metric("Questions Asked", len(student.questions_asked))
        with col3:
            st.metric("Topics Covered", len(student.weak_topics) + len(student.strong_topics))
        
        # Strong topics
        st.subheader("✅ Strong Topics")
        if student.strong_topics:
            for topic, score in student.strong_topics.items():
                st.progress(score/100, text=f"{topic}: {score}%")
        else:
            st.info("No strong topics recorded yet")
        
        # Weak topics needing improvement
        st.subheader("⚠️ Topics Needing Improvement")
        if student.weak_topics:
            for topic, score in student.weak_topics.items():
                st.progress(score/100, text=f"{topic}: {score}% (needs focus)")
        else:
            st.success("Great! All topics are going well!")
        
        # Personalized recommendations
        st.subheader("🎯 Personalized Recommendations")
        recommendations = st.session_state.personalizer.generate_learning_recommendations(student)
        
        for rec in recommendations:
            with st.expander(f"{rec['topic']} - Priority: {rec['priority'].upper()}"):
                st.write(f"**Score:** {rec['current_score']}/100")
                st.write(f"**Recommendation:** {rec['recommendation']}")
                st.write("**Resources:**")
                for resource in rec['suggested_resources']:
                    st.write(f"- {resource}")
        
        # Next topic suggestion
        st.subheader("📚 What to Study Next")
        st.info(st.session_state.personalizer.suggest_next_topic(student))

# ============= RESOURCES =============
elif page == "Resources":
    st.title("📚 Learning Resources")
    
    if st.session_state.student:
        student = st.session_state.student
        st.subheader(f"Resources for Year {student.year}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Textbooks & References
        - Gray's Anatomy
        - Guyton & Hall Physiology
        - Robbins & Cotran Pathology
        - Goodman & Gilman Pharmacology
        """)
    
    with col2:
        st.markdown("""
        ### Online Platforms
        - OpenStax Medical
        - Khan Academy
        - MedScape
        - UpToDate
        """)
    
    st.markdown("""
    ### Q&A Platforms
    - Board Review Questions
    - Case Studies
    - Clinical Scenarios
    """)

# ============= FOOTER =============
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🏥 Medical LLM Tutor v1.0</p>
    <p>Personalized learning for medical excellence</p>
</div>
""", unsafe_allow_html=True)

# Show current student status in sidebar
if st.session_state.student:
    st.sidebar.success(f"✓ Logged in as: {st.session_state.student.name}")
    st.sidebar.info(f"Year: {st.session_state.student.year}")

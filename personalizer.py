"""
Personalization Engine
Generates customized answers based on student level and learning history
"""
from typing import Dict, List
from student_db import StudentProfile

class PersonalizationEngine:
    """Personalizes LLM responses based on student profile"""
    
    # Difficulty levels by year (University of Nigeria Nsukka: 6 years)
    DIFFICULTY_MAP = {
        1: "simple_foundation",    # 1st year: Basic sciences foundation
        2: "intermediate_sciences", # 2nd year: Advanced sciences
        3: "transition_clinical",   # 3rd year: Transition to clinical
        4: "clinical_advanced",     # 4th year: Advanced clinical
        5: "specialist_clinical",   # 5th year: Specialized clinical rotations
        6: "expert_final"           # 6th year: Final clinical year
    }
    
    # Topic difficulty levels
    TOPIC_ADJUSTMENTS = {
        "simple_foundation": {
            "style": "beginner-friendly, foundational",
            "examples": 1,
            "depth": "basic",
            "clinical_relevance": "minimal"
        },
        "intermediate_sciences": {
            "style": "clear, detailed with mechanisms",
            "examples": 2,
            "depth": "intermediate",
            "clinical_relevance": "emerging"
        },
        "transition_clinical": {
            "style": "clinically-focused, problem-based",
            "examples": 2,
            "depth": "comprehensive",
            "clinical_relevance": "moderate"
        },
        "clinical_advanced": {
            "style": "technical, clinical-focused, patient-centered",
            "examples": 3,
            "depth": "comprehensive with variations",
            "clinical_relevance": "high"
        },
        "specialist_clinical": {
            "style": "specialized, evidence-based, case-driven",
            "examples": 4,
            "depth": "exhaustive with specialty focus",
            "clinical_relevance": "very high"
        },
        "expert_final": {
            "style": "expert-level, research-oriented, critical appraisal",
            "examples": 5,
            "depth": "exhaustive with latest evidence",
            "clinical_relevance": "research and practice leadership"
        }
    }
    
    def __init__(self):
        pass
    
    def get_answer_template(self, student: StudentProfile, topic: str) -> str:
        """Generate a customized answer template based on student profile"""
        
        year = student.year
        difficulty_level = self.DIFFICULTY_MAP[year]
        
        # Check if student struggled with this topic before
        weak_topics = dict(student.weak_topics)
        if topic in weak_topics:
            # Adjust difficulty downward
            if difficulty_level != "simple_overview":
                difficulty_level = self.DIFFICULTY_MAP[max(1, year - 1)]
        
        # Check if student excels at this topic
        strong_topics = dict(student.strong_topics)
        if topic in strong_topics and year > 1:
            # Can use more advanced explanations
            difficulty_level = self.DIFFICULTY_MAP[min(4, year + 1)]
        
        adjustments = self.TOPIC_ADJUSTMENTS[difficulty_level]
        
        template = f"""
[PERSONALIZED ANSWER]
Student: {student.name} (Year {student.year})
Topic: {topic}
Difficulty: {difficulty_level}
---

Style: {adjustments['style']}
Include {adjustments['examples']} real-world example(s)
Depth: {adjustments['depth']} level
Clinical focus: {adjustments['clinical_relevance']}

ANSWER:
"""
        return template
    
    def generate_learning_recommendations(self, student: StudentProfile) -> List[Dict]:
        """Generate personalized learning recommendations"""
        
        recommendations = []
        weak_topics = student.get_learning_focus()  # Top 5 weak areas
        
        for topic, score in weak_topics:
            recommendations.append({
                "topic": topic,
                "current_score": score,
                "recommendation": f"Focus on '{topic}' - you scored {score}/100",
                "suggested_resources": self._get_resources_for_year(student.year, topic),
                "priority": "high" if score < 40 else "medium"
            })
        
        return recommendations
    
    def _get_resources_for_year(self, year: int, topic: str) -> List[str]:
        """Get appropriate learning resources based on year"""
        
        resources = {
            1: [f"Introduction to {topic}", "Basic concepts textbook", "Video tutorials"],
            2: [f"Intermediate {topic}", "Case studies", "Study guides"],
            3: [f"Clinical {topic}", "Patient case discussions", "Research papers"],
            4: [f"Advanced {topic}", "Research literature", "Expert reviews"]
        }
        
        return resources.get(year, resources[1])
    
    def suggest_next_topic(self, student: StudentProfile) -> str:
        """Suggest the next topic to study"""
        
        weak_topics = student.get_learning_focus()
        if weak_topics:
            next_topic = weak_topics[0][0]
            return f"Based on your performance, I suggest focusing on: {next_topic}"
        else:
            return "Great job! You're performing well. Let's explore advanced topics."
    
    def get_adaptive_difficulty(self, student: StudentProfile, topic: str) -> float:
        """Get difficulty multiplier (0.5 = easier, 2.0 = harder)"""
        
        base_difficulty = student.year / 2  # 0.5 to 2.0
        
        # Adjust based on past performance
        if topic in student.weak_topics:
            base_difficulty *= 0.7  # Make easier
        elif topic in student.strong_topics:
            base_difficulty *= 1.3  # Make harder
        
        return min(2.0, max(0.5, base_difficulty))


# Example usage
if __name__ == "__main__":
    from student_db import StudentProfile
    
    # Create a student
    student = StudentProfile("MED001", "Sarah Khan", 2)
    student.weak_topics = {"pharmacology": 45, "biochemistry": 55}
    student.strong_topics = {"anatomy": 92}
    
    # Personalize
    engine = PersonalizationEngine()
    
    print("=== Personalized Answer Template ===")
    print(engine.get_answer_template(student, "pharmacology"))
    
    print("\n=== Learning Recommendations ===")
    for rec in engine.generate_learning_recommendations(student):
        print(rec)
    
    print("\n=== Next Topic ===")
    print(engine.suggest_next_topic(student))
    
    print("\n=== Difficulty Adjustment ===")
    print(f"Pharmacology difficulty: {engine.get_adaptive_difficulty(student, 'pharmacology')}")
    print(f"Anatomy difficulty: {engine.get_adaptive_difficulty(student, 'anatomy')}")

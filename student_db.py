"""
Student Profile & Learning Tracking System
Stores personalized learning data for each medical student
"""
import json
import os
from datetime import datetime
from typing import Dict, List

class StudentProfile:
    def __init__(self, student_id: str, name: str, year: int):
        """
        Args:
            student_id: Unique identifier
            name: Student name
            year: Medical school year (1-4)
        """
        self.student_id = student_id
        self.name = name
        self.year = year  # 1st, 2nd, 3rd, 4th year
        self.created_at = datetime.now()
        
        # Learning tracking
        self.weak_topics = {}  # {topic: score (0-100)}
        self.strong_topics = {}  # {topic: score (0-100)}
        self.questions_asked = []  # History of questions
        self.learning_path = []  # Recommended learning path
        
    def add_question(self, question: str, topic: str, score: float):
        """Record a question and performance"""
        self.questions_asked.append({
            "question": question,
            "topic": topic,
            "score": score,  # 0-100 (0 = didn't understand, 100 = fully understood)
            "timestamp": datetime.now().isoformat()
        })
        self._update_topic_scores(topic, score)
    
    def _update_topic_scores(self, topic: str, score: float):
        """Update weak/strong topics based on performance"""
        if score < 60:
            self.weak_topics[topic] = score
            self.strong_topics.pop(topic, None)
        elif score > 80:
            self.strong_topics[topic] = score
            self.weak_topics.pop(topic, None)
    
    def get_learning_focus(self) -> List[str]:
        """Return prioritized topics to focus on"""
        return sorted(self.weak_topics.items(), key=lambda x: x[1])[:5]
    
    def to_dict(self) -> Dict:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "year": self.year,
            "weak_topics": self.weak_topics,
            "strong_topics": self.strong_topics,
            "total_questions": len(self.questions_asked),
            "created_at": self.created_at.isoformat()
        }


class StudentDatabase:
    """Simple file-based student database"""
    def __init__(self, db_path: str = "student_data"):
        self.db_path = db_path
        os.makedirs(db_path, exist_ok=True)
    
    def save_profile(self, profile: StudentProfile):
        """Save student profile to file"""
        file_path = os.path.join(self.db_path, f"{profile.student_id}.json")
        with open(file_path, 'w') as f:
            json.dump(profile.__dict__, f, default=str, indent=2)
    
    def load_profile(self, student_id: str) -> StudentProfile:
        """Load student profile"""
        file_path = os.path.join(self.db_path, f"{student_id}.json")
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        profile = StudentProfile(data["student_id"], data["name"], data["year"])
        profile.weak_topics = data.get("weak_topics", {})
        profile.strong_topics = data.get("strong_topics", {})
        profile.questions_asked = data.get("questions_asked", [])
        return profile


# Example usage
if __name__ == "__main__":
    # Create a sample student
    db = StudentDatabase()
    student = StudentProfile("MED001", "John Smith", 2)
    
    # Simulate learning
    student.add_question("What is hypertension?", "cardiology", 85)
    student.add_question("Pathophysiology of diabetes", "endocrinology", 45)
    student.add_question("Anatomy of the heart", "cardiology", 90)
    
    # Save and display
    db.save_profile(student)
    print("Student Profile:", student.to_dict())
    print("Focus Areas:", student.get_learning_focus())

"""
Medical Data Collector
Fetches medical curriculum content from multiple sources
"""
import os
import json
from typing import List, Dict
from pathlib import Path

class MedicalDataCollector:
    """Collects medical curriculum data from various sources"""
    
    def __init__(self, output_dir: str = "medical_data"):
        self.output_dir = output_dir
        Path(output_dir).mkdir(exist_ok=True)
        
        self.medical_topics = [
            # 1st Year - Preclinical Foundation
            {"topic": "Chemistry", "year": 1, "code": "CHM 101", "subtopics": ["Basic Practical Chemistry", "Principles of Chemistry"]},
            {"topic": "Biology", "year": 1, "code": "BIO 101", "subtopics": ["Genetics for Medical Students", "General Biology"]},
            {"topic": "Physics", "year": 1, "code": "PHY 101", "subtopics": ["General Physics for Life Sciences", "Practical Physics"]},
            {"topic": "General Studies", "year": 1, "code": "GS 111", "subtopics": ["Use of English", "Library & Study Skills", "Issues of Peace & Conflict"]},
            
            # 2nd Year - Preclinical Sciences
            {"topic": "Gross Anatomy", "year": 2, "code": "ANA 201", "subtopics": ["Skeletal system", "Muscular system", "Nervous system", "Organ systems"]},
            {"topic": "Embryology and Genetics", "year": 2, "code": "ANA 203", "subtopics": ["Embryonic development", "Genetic principles", "Congenital abnormalities"]},
            {"topic": "Histology and Histochemistry", "year": 2, "code": "ANA 205", "subtopics": ["Tissue types", "Cellular organization", "Microscopy"]},
            {"topic": "Biochemistry", "year": 2, "code": "BIC 201", "subtopics": ["Carbohydrate metabolism", "Protein metabolism", "Lipid metabolism", "Enzyme kinetics"]},
            {"topic": "Physiology", "year": 2, "code": "PYS 201", "subtopics": ["Blood physiology", "Cardiovascular physiology", "Respiratory physiology", "GI physiology"]},
            
            # 3rd Year - Preclinical to Clinical Transition
            {"topic": "Pharmacology", "year": 3, "code": "PHA 301", "subtopics": ["General Pharmacology", "Drug classification", "Pharmacokinetics", "Pharmacodynamics"]},
            {"topic": "Microbiology", "year": 3, "code": "MIC 302", "subtopics": ["Bacteriology", "Virology", "Parasitology", "Immunology"]},
            {"topic": "Pathology", "year": 3, "code": "PAT 301", "subtopics": ["Cell injury", "Inflammation", "Neoplasia", "Systemic pathology"]},
            {"topic": "Clinical Chemistry", "year": 3, "code": "CPT 301", "subtopics": ["Lab diagnostics", "Metabolic pathways", "Clinical correlations"]},
            {"topic": "Internal Medicine", "year": 3, "code": "MED 301", "subtopics": ["Cardiology I", "Respiratory Medicine I", "Gastroenterology", "Nephrology I", "Neurology I", "Hematology"]},
            {"topic": "Clinical Surgery", "year": 3, "code": "SUG 301", "subtopics": ["General Surgery", "GI Surgery", "Congenital Abnormalities", "Urology", "Trauma Surgery"]},
            
            # 4th Year - Advanced Clinical
            {"topic": "Advanced Pharmacology", "year": 4, "code": "PHA 401", "subtopics": ["Antimicrobial drugs", "CNS drugs", "Chemotherapy", "Special therapeutics"]},
            {"topic": "Advanced Microbiology", "year": 4, "code": "MIC 401", "subtopics": ["Medical Protozoology", "Medical Helminthology", "Medical Entomology"]},
            {"topic": "Hematology", "year": 4, "code": "HEM 401", "subtopics": ["Blood cell disorders", "Hemostasis", "Blood transfusion", "Hematologic malignancies"]},
            {"topic": "Obstetrics and Gynaecology", "year": 4, "code": "OBG 401", "subtopics": ["Reproductive physiology", "Pregnancy", "Labour", "Gynecologic disorders"]},
            {"topic": "Pediatrics", "year": 4, "code": "PAE 410", "subtopics": ["Growth and development", "Pediatric diseases", "Neonatal care", "Pediatric nutrition"]},
            {"topic": "Forensic Medicine", "year": 4, "code": "PAT 403", "subtopics": ["Medical jurisprudence", "Toxicology", "Death investigation"]},
            
            # 5th Year - Specialized Clinical
            {"topic": "Obstetric Clinics", "year": 5, "code": "OBG 503", "subtopics": ["Antenatal care", "Labor management", "Postpartum care", "High-risk obstetrics"]},
            {"topic": "Pediatric Clinics", "year": 5, "code": "PAE 501", "subtopics": ["Pediatric endocrinology", "Pediatric neurology", "Pediatric surgery", "Infectious diseases"]},
            {"topic": "Community Health", "year": 5, "code": "COM 502", "subtopics": ["Public health", "Epidemiology", "Primary health care", "Health promotion"]},
            
            # 6th Year - Final Clinical Training
            {"topic": "Advanced Internal Medicine", "year": 6, "code": "MED 601", "subtopics": ["Cardiology II", "Respiratory Medicine II", "Gastroenterology II", "Nephrology II", "Neurology II"]},
            {"topic": "Advanced Surgery", "year": 6, "code": "SUG 601", "subtopics": ["Cardiothoracic surgery", "Neurosurgery", "Oncologic surgery", "Vascular surgery"]},
            {"topic": "Tropical Medicine", "year": 6, "code": "MED 608", "subtopics": ["Endemic diseases", "Parasitic infections", "Vector-borne diseases", "Infectious disease management"]},
            {"topic": "Medical Ethics", "year": 6, "code": "MED 610", "subtopics": ["Professional ethics", "Jurisprudence", "Medical-legal issues", "Patient rights"]},
        ]
    
    def create_curriculum_index(self) -> Dict:
        """Create a comprehensive curriculum index"""
        curriculum = {
            "year_1": self._get_year_curriculum(1),
            "year_2": self._get_year_curriculum(2),
            "year_3": self._get_year_curriculum(3),
            "year_4": self._get_year_curriculum(4),
        }
        
        # Save index
        index_path = os.path.join(self.output_dir, "curriculum_index.json")
        with open(index_path, 'w') as f:
            json.dump(curriculum, f, indent=2)
        
        print(f"✓ Curriculum index saved to {index_path}")
        return curriculum
    
    def _get_year_curriculum(self, year: int) -> List[Dict]:
        """Get all topics for a specific year"""
        return [t for t in self.medical_topics if t["year"] == year]
    
    def create_sample_questions(self) -> List[Dict]:
        """Generate sample medical Q&A for training - University of Nigeria Nsukka curriculum"""
        
        sample_qa = [
            # Year 1 - General Sciences
            {"year": 1, "course": "CHM 101", "question": "What are the basic principles of chemistry relevant to medical science?", 
             "topic": "Chemistry", "answer": "Chemistry for medical students focuses on organic and biochemistry principles including molecular bonds, pH, buffers..."},
            
            {"year": 1, "course": "BIO 101", "question": "Explain the concept of genetics for medical students.", 
             "topic": "Biology", "answer": "Genetics covers Mendelian inheritance, DNA structure, gene expression, and clinical significance of genetic mutations..."},
            
            # Year 2 - Anatomy & Basic Sciences
            {"year": 2, "course": "ANA 201", "question": "Name the major bones of the upper limb and their anatomical landmarks.", 
             "topic": "Gross Anatomy", "answer": "The upper limb skeleton includes humerus, radius, ulna, and carpal bones with important bony landmarks..."},
            
            {"year": 2, "course": "BIC 201", "question": "Describe the citric acid cycle and its clinical significance.", 
             "topic": "Biochemistry", "answer": "The citric acid cycle generates energy and intermediates for biosynthesis. Defects lead to metabolic disorders..."},
            
            {"year": 2, "course": "PYS 201", "question": "Explain the physiology of blood pressure regulation.", 
             "topic": "Physiology", "answer": "Blood pressure is maintained by cardiac output, peripheral resistance, and neurohumoral regulation..."},
            
            # Year 3 - Transition to Clinical
            {"year": 3, "course": "PHA 301", "question": "What is pharmacokinetics and how does it affect drug dosing?", 
             "topic": "Pharmacology", "answer": "Pharmacokinetics involves absorption, distribution, metabolism, and excretion. These guide appropriate dosing..."},
            
            {"year": 3, "course": "PAT 301", "question": "Explain the process of inflammation and its outcomes.", 
             "topic": "Pathology", "answer": "Inflammation involves vasodilation, cellular infiltration, and can resolve, suppurate, or become chronic..."},
            
            {"year": 3, "course": "MED 301", "question": "What are the cardinal signs and symptoms of heart failure?", 
             "topic": "Internal Medicine", "answer": "Heart failure presents with dyspnea, fatigue, edema, and orthopnea due to reduced cardiac output..."},
            
            {"year": 3, "course": "SUG 301", "question": "Describe the principles of surgical asepsis and infection control.", 
             "topic": "Clinical Surgery", "answer": "Surgical asepsis involves sterilization, maintaining sterile fields, and proper technique to prevent SSI..."},
            
            # Year 4 - Advanced Clinical
            {"year": 4, "course": "OBG 401", "question": "What are the stages of labor and normal delivery management?", 
             "topic": "Obstetrics and Gynaecology", "answer": "Labor has three stages: cervical dilation, fetal descent, and placental delivery requiring careful monitoring..."},
            
            {"year": 4, "course": "PAE 410", "question": "Describe normal growth and development milestones in children.", 
             "topic": "Pediatrics", "answer": "Growth and development follow predictable patterns. Deviations may indicate nutritional or genetic problems..."},
            
            {"year": 4, "course": "HEM 401", "question": "What are the classification and clinical features of anemia?", 
             "topic": "Hematology", "answer": "Anemia is classified by RBC size and hemoglobin content. Symptoms depend on severity and acuity..."},
            
            # Year 5 - Specialized Clinical
            {"year": 5, "course": "OBG 503", "question": "Discuss the management of a complicated pregnancy.", 
             "topic": "Obstetric Clinics", "answer": "Complications require multidisciplinary management with consideration of maternal and fetal factors..."},
            
            {"year": 5, "course": "COM 502", "question": "Explain the role of epidemiology in disease control.", 
             "topic": "Community Health", "answer": "Epidemiology identifies disease patterns, risk factors, and guides public health interventions..."},
            
            # Year 6 - Final Clinical
            {"year": 6, "course": "MED 601", "question": "Discuss the management of acute coronary syndrome.", 
             "topic": "Advanced Internal Medicine", "answer": "ACS management involves rapid diagnosis, antiplatelet/anticoagulation therapy, and revascularization..."},
            
            {"year": 6, "course": "MED 610", "question": "Explain informed consent and its legal implications.", 
             "topic": "Medical Ethics", "answer": "Informed consent requires disclosure of risks, benefits, and alternatives with patient autonomy assessment..."},
        ]
        
        qa_path = os.path.join(self.output_dir, "sample_questions.json")
        with open(qa_path, 'w') as f:
            json.dump(sample_qa, f, indent=2)
        
        print(f"✓ Sample Q&A saved to {qa_path}")
        return sample_qa
    
    def create_learning_objectives(self) -> Dict:
        """Create learning objectives for University of Nigeria Nsukka curriculum"""
        
        objectives = {
            "Gross Anatomy": [
                "Understand human skeletal anatomy with landmarks",
                "Identify major organs and systems",
                "Apply anatomical knowledge to clinical examination"
            ],
            "Biochemistry": [
                "Understand metabolic pathways and energy production",
                "Know enzyme kinetics and regulation",
                "Apply biochemistry to clinical disorders"
            ],
            "Pharmacology": [
                "Understand drug classifications and mechanisms",
                "Know pharmacokinetics and pharmacodynamics",
                "Manage drug interactions and side effects safely"
            ],
            "Pathology": [
                "Understand cell injury and disease mechanisms",
                "Diagnose pathological conditions",
                "Apply pathological knowledge to clinical practice"
            ],
            "Internal Medicine": [
                "Diagnose and manage internal diseases",
                "Know evidence-based treatment guidelines",
                "Manage patient care with clinical judgment"
            ],
            "Clinical Surgery": [
                "Understand surgical principles and asepsis",
                "Manage acute surgical emergencies",
                "Apply surgical techniques appropriately"
            ],
            "Obstetrics and Gynaecology": [
                "Understand normal and abnormal pregnancy",
                "Manage labor and delivery",
                "Manage gynecologic disorders"
            ],
            "Pediatrics": [
                "Understand growth and development",
                "Diagnose and manage pediatric diseases",
                "Provide preventive pediatric care"
            ],
            "Medical Ethics": [
                "Understand professional and ethical responsibilities",
                "Know medical-legal principles",
                "Apply ethics to clinical decision-making"
            ]
        }
        
        obj_path = os.path.join(self.output_dir, "learning_objectives.json")
        with open(obj_path, 'w') as f:
            json.dump(objectives, f, indent=2)
        
        print(f"✓ Learning objectives saved to {obj_path}")
        return objectives
    
    def compile_training_data(self) -> str:
        """Compile all training data into a single file"""
        
        training_text = "# Medical Curriculum Training Data\n\n"
        
        for topic_info in self.medical_topics:
            training_text += f"\n## {topic_info['topic']} (Year {topic_info['year']})\n"
            training_text += f"Subtopics: {', '.join(topic_info['subtopics'])}\n"
        
        output_path = os.path.join(self.output_dir, "medical_training_data.txt")
        with open(output_path, 'w') as f:
            f.write(training_text)
        
        print(f"✓ Training data compiled to {output_path}")
        return output_path


# Run data collection
if __name__ == "__main__":
    collector = MedicalDataCollector("medical_data")
    
    print("Collecting medical curriculum data...\n")
    collector.create_curriculum_index()
    collector.create_sample_questions()
    collector.create_learning_objectives()
    collector.compile_training_data()
    
    print("\n✓ Data collection complete!")
    print("All data saved to 'medical_data' directory")

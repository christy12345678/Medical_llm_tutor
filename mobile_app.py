"""
Mobile App for Medical LLM Tutor
Uses Kivy for cross-platform Android/iOS support
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.progressbar import ProgressBar
import os
import json

# Import our modules
from student_db import StudentProfile, StudentDatabase
from personalizer import PersonalizationEngine
from data_collector import MedicalDataCollector

# Set window size for mobile
Window.size = (400, 700)

class LoginScreen(Screen):
    """Student login/signup screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = StudentDatabase()
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title
        title = Label(
            text='🏥 Medical LLM Tutor\nUniversity of Nigeria Nsukka',
            size_hint_y=0.15,
            font_size='18sp',
            bold=True
        )
        layout.add_widget(title)
        
        # Scrollable form
        scroll = ScrollView(size_hint=(1, 0.7))
        form_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        form_layout.bind(minimum_height=form_layout.setter('height'))
        
        # Student ID
        form_layout.add_widget(Label(text='Student ID:', size_hint_y=None, height=40))
        self.student_id = TextInput(
            hint_text='e.g., MED001 or 2024/MED/001',
            multiline=False,
            size_hint_y=None,
            height=40
        )
        form_layout.add_widget(self.student_id)
        
        # Full Name
        form_layout.add_widget(Label(text='Full Name:', size_hint_y=None, height=40))
        self.name = TextInput(
            hint_text='Your full name',
            multiline=False,
            size_hint_y=None,
            height=40
        )
        form_layout.add_widget(self.name)
        
        # Year Selection
        form_layout.add_widget(Label(text='Medical School Year:', size_hint_y=None, height=40))
        self.year_spinner = Spinner(
            text='1',
            values=('1', '2', '3', '4', '5', '6'),
            size_hint_y=None,
            height=40
        )
        form_layout.add_widget(self.year_spinner)
        
        # Specialization
        form_layout.add_widget(Label(text='Specialization (optional):', size_hint_y=None, height=40))
        self.specialization = TextInput(
            hint_text='e.g., Surgery, Medicine',
            multiline=False,
            size_hint_y=None,
            height=40
        )
        form_layout.add_widget(self.specialization)
        
        scroll.add_widget(form_layout)
        layout.add_widget(scroll)
        
        # Buttons
        button_layout = BoxLayout(size_hint_y=0.15, spacing=10)
        
        login_btn = Button(text='Login', background_color=(0.2, 0.6, 0.8, 1))
        login_btn.bind(on_press=self.login)
        button_layout.add_widget(login_btn)
        
        create_btn = Button(text='Create Profile', background_color=(0.2, 0.8, 0.6, 1))
        create_btn.bind(on_press=self.create_profile)
        button_layout.add_widget(create_btn)
        
        layout.add_widget(button_layout)
        
        self.add_widget(layout)
    
    def login(self, instance):
        """Login to existing profile"""
        student_id = self.student_id.text
        if not student_id:
            self.show_popup("Error", "Please enter Student ID")
            return
        
        profile = self.db.load_profile(student_id)
        if profile:
            self.manager.get_screen('dashboard').student = profile
            self.manager.current = 'dashboard'
        else:
            self.show_popup("Error", "Student ID not found. Create a new profile.")
    
    def create_profile(self, instance):
        """Create new student profile"""
        if not self.student_id.text or not self.name.text:
            self.show_popup("Error", "Please fill in Student ID and Full Name")
            return
        
        year = int(self.year_spinner.text)
        profile = StudentProfile(self.student_id.text, self.name.text, year)
        self.db.save_profile(profile)
        
        self.manager.get_screen('dashboard').student = profile
        self.show_popup("Success", f"Profile created! Welcome, {self.name.text}")
        self.manager.current = 'dashboard'
    
    def show_popup(self, title, message):
        """Show popup dialog"""
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.9, 0.3)
        )
        popup.open()


class QAScreen(Screen):
    """Q&A Assistant screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.student = None
        self.engine = PersonalizationEngine()
        self.db = StudentDatabase()
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Header
        layout.add_widget(Label(text='❓ Ask a Question', size_hint_y=0.08, font_size='18sp', bold=True))
        
        # Question input
        layout.add_widget(Label(text='Your Question:', size_hint_y=0.06, font_size='14sp'))
        self.question = TextInput(
            hint_text='Ask about any medical topic...',
            multiline=True,
            size_hint_y=0.25
        )
        layout.add_widget(self.question)
        
        # Topic selection
        layout.add_widget(Label(text='Topic:', size_hint_y=0.06, font_size='14sp'))
        self.topic = Spinner(
            text='Anatomy',
            values=('Anatomy', 'Pharmacology', 'Pathology', 'Physiology', 'Biochemistry', 'Medicine', 'Surgery', 'Other'),
            size_hint_y=0.08
        )
        layout.add_widget(self.topic)
        
        # Ask button
        ask_btn = Button(text='Get Personalized Answer', background_color=(0.2, 0.6, 0.8, 1), size_hint_y=0.1)
        ask_btn.bind(on_press=self.get_answer)
        layout.add_widget(ask_btn)
        
        # Answer display
        layout.add_widget(Label(text='Answer:', size_hint_y=0.06, font_size='14sp', bold=True))
        
        scroll = ScrollView(size_hint_y=0.3)
        self.answer_display = Label(
            text='[Personalized answer will appear here]',
            markup=True,
            size_hint_y=None,
            text_size=(380, None)
        )
        self.answer_display.bind(texture_size=self.answer_display.setter('size'))
        scroll.add_widget(self.answer_display)
        layout.add_widget(scroll)
        
        # Back button
        back_btn = Button(text='← Back to Dashboard', background_color=(0.8, 0.6, 0.2, 1), size_hint_y=0.08)
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
    
    def get_answer(self, instance):
        """Get personalized answer"""
        if not self.student:
            return
        
        if not self.question.text:
            self.show_popup("Error", "Please enter a question")
            return
        
        # Get personalization template
        template = self.engine.get_answer_template(self.student, self.topic.text)
        
        # Sample answer (in production, would call fine-tuned LLM)
        sample_answers = {
            'Anatomy': 'The human skeleton provides support and protection for organs. It consists of 206 bones in adults...',
            'Pharmacology': 'Pharmacology is the study of drug actions and interactions. Understanding mechanisms helps predict patient responses...',
            'Pathology': 'Pathology examines disease mechanisms and tissue changes. It bridges basic science and clinical medicine...',
            'Physiology': 'Physiology explains how body systems function. Homeostasis is maintained through complex regulatory mechanisms...',
            'Biochemistry': 'Biochemistry studies molecular processes in living organisms. Metabolic pathways generate energy and build molecules...',
            'Medicine': 'Internal medicine manages adult diseases. Evidence-based diagnosis and treatment are essential...',
            'Surgery': 'Surgery treats conditions through operative intervention. Preoperative and postoperative care are critical...',
        }
        
        answer = sample_answers.get(self.topic.text, 'General medical information provided based on your question and level.')
        
        # Display
        self.answer_display.text = f"""[b]{template}[/b]

[i]Sample Answer:[/i]
{answer}

[size=12sp][i]Year {self.student.year} - {self.topic.text}[/i][/size]"""
        
        # Record interaction
        self.student.add_question(self.question.text, self.topic.text, 75)
        self.db.save_profile(self.student)
        
        # Clear input
        self.question.text = ''
    
    def go_back(self, instance):
        """Go back to dashboard"""
        self.manager.current = 'dashboard'
    
    def show_popup(self, title, message):
        """Show popup dialog"""
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.9, 0.3)
        )
        popup.open()


class DashboardScreen(Screen):
    """Learning Dashboard"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.student = None
        self.engine = PersonalizationEngine()
        self.db = StudentDatabase()
    
    def on_enter(self):
        """Refresh dashboard when entering"""
        if not self.student:
            return
        
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Header
        header = BoxLayout(size_hint_y=0.12, spacing=10)
        header.add_widget(Label(text=f'📊 Dashboard\n{self.student.name}', font_size='16sp', bold=True))
        header.add_widget(Label(text=f'Year {self.student.year}', font_size='14sp'))
        layout.add_widget(header)
        
        # Stats
        stats_layout = GridLayout(cols=3, size_hint_y=0.15, spacing=10)
        stats_layout.add_widget(self._make_stat('Year', str(self.student.year)))
        stats_layout.add_widget(self._make_stat('Questions', str(len(self.student.questions_asked))))
        stats_layout.add_widget(self._make_stat('Topics', str(len(self.student.weak_topics) + len(self.student.strong_topics))))
        layout.add_widget(stats_layout)
        
        # Scrollable content
        scroll = ScrollView(size_hint_y=0.65)
        content = GridLayout(cols=1, spacing=15, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))
        
        # Strong topics
        content.add_widget(Label(text='✅ Strong Topics', size_hint_y=None, height=40, bold=True, font_size='14sp'))
        if self.student.strong_topics:
            for topic, score in self.student.strong_topics.items():
                topic_label = Label(
                    text=f'{topic}: {score}%',
                    size_hint_y=None,
                    height=35,
                    markup=True
                )
                content.add_widget(topic_label)
        else:
            content.add_widget(Label(text='No strong topics yet', size_hint_y=None, height=35))
        
        # Weak topics
        content.add_widget(Label(text='⚠️ Topics Needing Improvement', size_hint_y=None, height=40, bold=True, font_size='14sp'))
        if self.student.weak_topics:
            for topic, score in self.student.weak_topics.items():
                topic_label = Label(
                    text=f'{topic}: {score}%',
                    size_hint_y=None,
                    height=35
                )
                content.add_widget(topic_label)
        else:
            content.add_widget(Label(text='All topics are going well!', size_hint_y=None, height=35))
        
        # Recommendations
        content.add_widget(Label(text='🎯 Next to Study', size_hint_y=None, height=40, bold=True, font_size='14sp'))
        rec = self.engine.suggest_next_topic(self.student)
        content.add_widget(Label(text=rec, size_hint_y=None, height=60, markup=True))
        
        scroll.add_widget(content)
        layout.add_widget(scroll)
        
        # Navigation buttons
        nav_layout = GridLayout(cols=2, size_hint_y=0.15, spacing=10)
        
        qa_btn = Button(text='❓ Ask Question', background_color=(0.2, 0.6, 0.8, 1))
        qa_btn.bind(on_press=self.go_to_qa)
        nav_layout.add_widget(qa_btn)
        
        logout_btn = Button(text='🚪 Logout', background_color=(0.8, 0.2, 0.2, 1))
        logout_btn.bind(on_press=self.logout)
        nav_layout.add_widget(logout_btn)
        
        layout.add_widget(nav_layout)
        
        self.add_widget(layout)
    
    def _make_stat(self, label, value):
        """Create a stat box"""
        box = BoxLayout(orientation='vertical', size_hint_y=None, height=60)
        box.add_widget(Label(text=value, font_size='18sp', bold=True))
        box.add_widget(Label(text=label, font_size='12sp'))
        return box
    
    def go_to_qa(self, instance):
        """Go to Q&A screen"""
        self.manager.get_screen('qa').student = self.student
        self.manager.current = 'qa'
    
    def logout(self, instance):
        """Logout and return to login"""
        self.student = None
        self.manager.current = 'login'


class MedicalLLMMobileApp(App):
    """Main Mobile App"""
    
    def build(self):
        """Build the app"""
        # Create screen manager
        sm = ScreenManager()
        
        # Add screens
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(QAScreen(name='qa'))
        
        return sm


if __name__ == '__main__':
    app = MedicalLLMMobileApp()
    app.run()

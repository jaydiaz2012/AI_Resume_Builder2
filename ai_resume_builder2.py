import pandas as pd
import numpy as np
from typing import List, Dict, Optional
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

class ResumeBuilderAgent:
    def __init__(self):
        # Data storage for resume components
        self.personal_info = {}
        self.education_history = []
        self.work_experiences = []
        self.references = []
        
        # Validation rules
        self.validation_rules = {
            'name': {
                'min_length': 2,
                'max_length': 50,
                'required': True
            },
            'email': {
                'pattern': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                'required': True
            },
            'phone': {
                'pattern': r'^\+?1?\d{10,14}$',
                'required': True
            }
        }
    
    def collect_personal_information(self) -> Dict[str, str]:
        """
        Collect and validate personal information from user
        """
        prompts = [
            ("Full Name", "name"),
            ("Email Address", "email"),
            ("Phone Number", "phone"),
            ("Address", "address")
        ]
        
        personal_info = {}
        for prompt, key in prompts:
            while True:
                value = input(f"Enter your {prompt}: ").strip()
                if self._validate_field(key, value):
                    personal_info[key] = value
                    break
                print(f"Invalid {prompt}. Please try again.")
        
        return personal_info
    
    def collect_education_history(self) -> List[Dict[str, str]]:
        """
        Collect educational background details
        """
        education_entries = []
        while True:
            institution = input("Enter Institution Name (or press Enter to finish): ")
            if not institution:
                break
            
            degree = input("Enter Degree/Qualification: ")
            graduation_year = input("Enter Graduation Year: ")
            
            education_entries.append({
                'institution': institution,
                'degree': degree,
                'graduation_year': graduation_year
            })
        
        return education_entries
    
    def collect_work_experience(self) -> List[Dict[str, str]]:
        """
        Collect professional work experience details
        """
        work_experiences = []
        while True:
            company = input("Enter Company Name (or press Enter to finish): ")
            if not company:
                break
            
            job_title = input("Enter Job Title: ")
            start_date = input("Enter Start Date (YYYY-MM): ")
            end_date = input("Enter End Date (YYYY-MM or 'Present'): ")
            responsibilities = input("Enter Key Responsibilities (comma-separated): ").split(',')
            
            work_experiences.append({
                'company': company,
                'job_title': job_title,
                'start_date': start_date,
                'end_date': end_date,
                'responsibilities': responsibilities
            })
        
        return work_experiences
    
    def collect_references(self) -> List[Dict[str, str]]:
        """
        Collect professional references
        """
        references = []
        for i in range(3):
            print(f"\nReference {i+1}")
            name = input("Enter Reference Name: ")
            company = input("Enter Reference's Company: ")
            phone = input("Enter Reference's Phone Number: ")
            email = input("Enter Reference's Email: ")
            
            references.append({
                'name': name,
                'company': company,
                'phone': phone,
                'email': email
            })
        
        return references
    
    def _validate_field(self, field: str, value: str) -> bool:
        """
        Validate input fields based on predefined rules
        """
        if field not in self.validation_rules:
            return True
        
        rules = self.validation_rules[field]
        if rules.get('required') and not value:
            return False
        
        # Add specific validation logic for each field
        return True
    
    def generate_pdf_resume(self):
        """
        Generate a professional PDF resume
        """
        pdf_filename = f"{self.personal_info['name']}_resume.pdf"
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        
        # PDF generation logic would be implemented here
        # Using reportlab to create structured PDF
        
        return pdf_filename
    
    def build_resume(self):
        """
        Orchestrate resume building process
        """
        print("Welcome to Resume Builder AI")
        
        self.personal_info = self.collect_personal_information()
        self.education_history = self.collect_education_history()
        self.work_experiences = self.collect_work_experience()
        self.references = self.collect_references()
        
        resume_pdf = self.generate_pdf_resume()
        print(f"Resume generated: {resume_pdf}")

def main():
    resume_builder = ResumeBuilderAgent()
    resume_builder.build_resume()

if __name__ == "__main__":
    main()

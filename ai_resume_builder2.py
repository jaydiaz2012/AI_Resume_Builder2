import streamlit as st
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import re
import io

class ResumeBuilderApp:
    def __init__(self):
        st.set_page_config(page_title="Resume Builder", page_icon=":memo:")
        self.validate_rules = {
            'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            'phone': r'^\+?1?\d{10,14}$'
        }

    def validate_input(self, field, value):
        if field == 'email':
            return re.match(self.validate_rules['email'], value) is not None
        elif field == 'phone':
            return re.match(self.validate_rules['phone'], value) is not None
        return bool(value and len(value) > 2)

    def personal_info_section(self):
        st.header("Personal Information")
        personal_info = {}
        personal_info['name'] = st.text_input("Full Name")
        personal_info['email'] = st.text_input("Email Address")
        personal_info['phone'] = st.text_input("Phone Number")
        personal_info['address'] = st.text_input("Address")
        return personal_info

    def education_section(self):
        st.header("Education Background")
        education_entries = []
        num_edu = st.number_input("Number of Educational Entries", min_value=1, max_value=5, value=1)
        
        for i in range(num_edu):
            with st.expander(f"Education Entry {i+1}"):
                institution = st.text_input(f"Institution Name {i+1}")
                degree = st.text_input(f"Degree/Qualification {i+1}")
                graduation_year = st.text_input(f"Graduation Year {i+1}")
                
                education_entries.append({
                    'institution': institution,
                    'degree': degree,
                    'graduation_year': graduation_year
                })
        return education_entries

    def work_experience_section(self):
        st.header("Work Experience")
        work_experiences = []
        num_jobs = st.number_input("Number of Work Experiences", min_value=1, max_value=5, value=1)
        
        for i in range(num_jobs):
            with st.expander(f"Job Entry {i+1}"):
                company = st.text_input(f"Company Name {i+1}")
                job_title = st.text_input(f"Job Title {i+1}")
                start_date = st.date_input(f"Start Date {i+1}")
                end_date = st.date_input(f"End Date {i+1}")
                responsibilities = st.text_area(f"Key Responsibilities {i+1}")
                
                work_experiences.append({
                    'company': company,
                    'job_title': job_title,
                    'start_date': start_date,
                    'end_date': end_date,
                    'responsibilities': responsibilities.split('\n')
                })
        return work_experiences

    def references_section(self):
        st.header("Professional References")
        references = []
        for i in range(3):
            with st.expander(f"Reference {i+1}"):
                name = st.text_input(f"Reference Name {i+1}")
                company = st.text_input(f"Reference Company {i+1}")
                phone = st.text_input(f"Reference Phone {i+1}")
                email = st.text_input(f"Reference Email {i+1}")
                
                references.append({
                    'name': name,
                    'company': company,
                    'phone': phone,
                    'email': email
                })
        return references

    def generate_pdf(self, resume_data):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []

        # PDF generation logic would be implemented here
        # This is a placeholder implementation

        return buffer

    def run(self):
        st.title("AI Resume Builder")
        
        personal_info = self.personal_info_section()
        education_history = self.education_section()
        work_experiences = self.work_experience_section()
        references = self.references_section()

        if st.button("Generate Resume PDF"):
            resume_data = {
                'personal_info': personal_info,
                'education': education_history,
                'work_experiences': work_experiences,
                'references': references
            }
            
            pdf_buffer = self.generate_pdf(resume_data)
            st.download_button(
                label="Download Resume PDF",
                data=pdf_buffer.getvalue(),
                file_name=f"{personal_info['name']}_resume.pdf",
                mime="application/pdf"
            )

def main():
    app = ResumeBuilderApp()
    app.run()

if __name__ == "__main__":
    main()

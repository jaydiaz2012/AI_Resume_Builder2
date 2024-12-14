import streamlit as st
import pandas as pd
import io
import re
import PIL.Image
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

class ResumeBuilderApp:
    def __init__(self):
        st.set_page_config(page_title="Resume Builder", page_icon=":memo:")
        self.resume_data = {}

    def personal_info_section(self):
        st.header("Personal Information")
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            phone = st.text_input("Phone Number")
            address = st.text_input("Address")
        
        with col2:
            uploaded_file = st.file_uploader("Upload Profile Picture", type=['jpg', 'jpeg', 'png'])
            profile_pic = None
            
            if uploaded_file is not None:
                profile_image = PIL.Image.open(uploaded_file)
                profile_image = profile_image.resize((150, 150), PIL.Image.LANCZOS)
                profile_pic = f"profile_pic_{name}.png"
                profile_image.save(profile_pic)
                st.image(profile_image, caption="Profile Picture", width=150)
        
        return {
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'profile_pic': profile_pic
        }

    def education_section(self):
        st.header("Educational Background")
        num_edu = st.number_input("Number of Educational Entries", min_value=1, max_value=5, value=1)
        
        education_entries = []
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
        num_jobs = st.number_input("Number of Work Experiences", min_value=1, max_value=5, value=1)
        
        work_experiences = []
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

    def languages_section(self):
        st.header("Languages")
        num_languages = st.number_input("Number of Languages", min_value=1, max_value=5, value=1)
        
        languages = []
        for i in range(num_languages):
            with st.expander(f"Language {i+1}"):
                language = st.text_input(f"Language Name {i+1}")
                proficiency = st.selectbox(f"Proficiency Level {i+1}", 
                    ['Native', 'Fluent', 'Advanced', 'Intermediate', 'Basic'])
                
                languages.append({
                    'language': language,
                    'proficiency': proficiency
                })
        return languages

    def skills_section(self):
        st.header("Professional Skills")
        num_skills = st.number_input("Number of Skills", min_value=1, max_value=10, value=3)
        
        skills = []
        for i in range(num_skills):
            skill = st.text_input(f"Skill {i+1}")
            skills.append(skill)
        return skills

    def references_section(self):
        st.header("Professional References")
        num_references = st.number_input("Number of References", min_value=1, max_value=3, value=3)
        
        references = []
        for i in range(num_references):
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

        # PDF generation logic (placeholder)
        # Add more sophisticated PDF generation here
        
        return buffer

    def run(self):
        st.title("Your Resume Builder")
        
        personal_info = self.personal_info_section()
        education_history = self.education_section()
        work_experiences = self.work_experience_section()
        languages = self.languages_section()
        skills = self.skills_section()
        references = self.references_section()

        resume_data = {
            'personal_info': personal_info,
            'education': education_history,
            'work_experiences': work_experiences,
            'languages': languages,
            'skills': skills,
            'references': references
        }

        if st.button("Generate Resume PDF"):
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

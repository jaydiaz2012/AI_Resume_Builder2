import streamlit as st
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.units import inch
import re
import io
import PIL.Image

class ResumeBuilderApp:
    def __init__(self):
        st.set_page_config(page_title="Resume Builder", page_icon=":memo:")
        self.validate_rules = {
            'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            'phone': r'^\+?1?\d{10,14}$'
        }

    def personal_info_section(self):
        st.header("Personal Information")
        personal_info = {}
        col1, col2 = st.columns(2)
        
        with col1:
            personal_info['name'] = st.text_input("Full Name")
            personal_info['email'] = st.text_input("Email Address")
            personal_info['phone'] = st.text_input("Phone Number")
            personal_info['address'] = st.text_input("Address")
        
        with col2:
            uploaded_file = st.file_uploader("Upload Profile Picture", type=['jpg', 'jpeg', 'png'])
            
            if uploaded_file is not None:
                # Open and resize image
                profile_image = PIL.Image.open(uploaded_file)
                profile_image = profile_image.resize((150, 150), PIL.Image.LANCZOS)
                
                # Save resized image
                image_path = f"profile_pic_{personal_info['name']}.png"
                profile_image.save(image_path)
                personal_info['profile_pic'] = image_path
                
                st.image(profile_image, caption="Profile Picture", width=150)
            else:
                personal_info['profile_pic'] = None
        
        return personal_info

    def generate_pdf(self, resume_data):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []

        # Basic PDF generation with profile picture
        if resume_data['personal_info']['profile_pic']:
            try:
                img = Image(resume_data['personal_info']['profile_pic'], width=1.5*inch, height=1.5*inch)
                elements.append(img)
            except Exception as e:
                st.error(f"Error adding profile picture: {e}")

        # Add more PDF generation logic here
        
        return buffer

    def run(self):
        st.title("AI Resume Builder")
        
        personal_info = self.personal_info_section()

        if personal_info['profile_pic']:
            if st.button("Generate Resume PDF"):
                resume_data = {
                    'personal_info': personal_info
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

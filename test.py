import streamlit as st
import fitz  # PyMuPDF
from docx import Document
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the Streamlit page
st.set_page_config(
    page_title="InterviewBuddy",
    page_icon="🖥️", 
    layout="wide"
)

st.title("InterviewBuddy")

# File uploaders
interview_transcript = st.file_uploader("Upload the Interview Script", type=['pdf', 'docx'], help="Please upload a PDF or DOCX", key=1)
resume = st.file_uploader("Upload Interviewee Resume", type=['pdf', 'docx'], help="Please upload a PDF or DOCX", key=2)
interviewer_requirements = st.file_uploader("Upload Interviewer Requirements and Job Description", type=['pdf', 'docx'], help="Please upload a PDF or DOCX", key=3)

def extract_text(file):
    if file.type == "application/pdf":
        text = []
        with fitz.open(stream=file.getvalue()) as doc:
            for page in doc:
                text.append(page.get_text())
        return "\n".join(text)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

def send_to_api(transcript, resume, requirements):
    # Replace 'API_URL' and 'API_KEY' with your actual API URL and key
    headers = {'Authorization': 'Bearer YOUR_API_KEY'}
    data = {
        "transcript": transcript,
        "resume": resume,
        "requirements": requirements
    }
    response = requests.post('https://api.example.com/analyze', json=data, headers=headers)
    return response.json()

def send_email(content, recipient, subject):
    # Email configuration
    sender_email = "your-email@example.com"
    password = "your-password"
    
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient

    part = MIMEText(content, "plain")
    message.attach(part)
    
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, recipient, message.as_string())
    server.quit()

if st.button("Process Files"):
    if interview_transcript and resume and interviewer_requirements:
        transcript_text = extract_text(interview_transcript)
        resume_text = extract_text(resume)
        requirements_text = extract_text(interviewer_requirements)
        
        # Assuming you replace this with actual API call
        feedback = send_to_api(transcript_text, resume_text, requirements_text)
        
        st.write(feedback)  # Display the feedback
        
        # Manage user decision
        action = st.selectbox("Decision", ["Select", "Reject"])
        if action == "Select":
            st.session_state['summary'] = feedback['summary']  # Store summary
            # Redirect or handle as needed
        elif action == "Reject":
            # Send personalized email
            send_email("Your personalized rejection content here", "candidate@example.com", "Interview Feedback")
            st.success("Feedback sent to candidate.")

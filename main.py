import streamlit as st
from streamlit_option_menu import option_menu
import base64
import io
from dotenv import load_dotenv
load_dotenv()
import os
from PIL import Image
import PyPDF2 as pdf
from fpdf import FPDF
import google.generativeai as genai
import time
import json
from smtplib import SMTP_SSL
from email.message import EmailMessage
from mimetypes import guess_type

company_name = "Apple"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Load environment variables
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

def send_mail(sender_email, receiver_email, password, subject, content, file_name=None, file_data=None):
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(content)

    if file_name and file_data:
        mime_type, _ = guess_type(file_name)
        main_type, sub_type = mime_type.split('/')
        msg.add_attachment(file_data, maintype=main_type, subtype=sub_type, filename=file_name)
    
    with SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, password)
        smtp.send_message(msg)
    
    return "Mail sent successfully!"


def input_pdf_text(interview_transcript, resume, interviewer_requirements):
    # Converting Transcript into text.
    interview_transcript_reader = pdf.PdfReader(interview_transcript)
    interview_transcript_text = ""
    for page in interview_transcript_reader.pages:
        interview_transcript_text += page.extract_text() or ''  # Ensure text is not None
    
    # Converting Resume into text.
    resume_reader = pdf.PdfReader(resume)
    resume_text = ""
    for page in resume_reader.pages:
        resume_text += page.extract_text() or ''  # Ensure text is not None
    
    # Converting Resume into text.
    interviewer_requirements_reader = pdf.PdfReader(interviewer_requirements)
    interviewer_requirements_text = ""
    for page in interviewer_requirements_reader.pages:
        interviewer_requirements_text += page.extract_text() or ''  # Ensure text is not None
        
    return interview_transcript_text, resume_text, interviewer_requirements_text

def generate_feedback_report(interview_transcript_text, resume_text, interviewer_requirements_text):
    # Combine the texts
    # feedback_text = f"Interview Transcript:\n{interview_transcript_text}\n\nResume Details:\n{resume_text}\n\nInterviewer Requirements:\n{interviewer_requirements_text}"
    prompt = f""" 
                As an expert AI assistant designed to assist durin an interview process. Utilise your expertise in analyzing candidates and their performance during interviews according to the interviewer questions. I have provided you with interview_transcript, resume of the candidate and interviewer requirements for this along with information below. Follow that and generate me a clear and detailed feedback report for the interviwer on the following mentioned criteria.
                
                Interview Transcript: {interview_transcript_text}
                Interviwee_Resume: {resume_text}
                Interviewer_Requirements: {interviewer_requirements_text} \n
                
                Now utilizing the above content provided, generate a feedback Report based on the following criteria in detail.
                
                **Note: Use clear and simple english and do not helusinate and provide non relavant or incorrect information that is not being provided to you. Favor the interviewer and make sure you take the right decision that favors the company**
                
                Make sure the formatting ans structure of these should be neat and clean. Don't use unnecessary special characters.
                
                Criteria: I need the text to be in the following format with the same headings.
                Name: {name}
                Date: date in the transcript
                position: {position}
                
                - Overview:\n Concise overview on how well the candidate performed in the interview.
                
                - Provide interviewers question and the candidates response, along analyzing with how well the candidate answered or how he/she could've answered it better. (Give everything in the following format)
                Interviewr Question: ....\n
                Interviewee Response: ....\n
                Analysis: ....\n
            
                - Candidate Profile Matching: Analysis of how the candidate’s qualifications and experience align with the job description.
                
                - Answer Alignment: Evaluation of how the candidate’s answers match the interviewer's questions and the required job competencies.
                
                - Potential Red Flags: Highlight any potential concerns or discrepancies noted during the interview. 
                
                - Recommendations: Suggest whether the candidate should proceed to the next round, based on the analysis.
                
                """
    
    feedback_text = get_gemini_response(prompt)
    # Create a PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 11)
    
    # Add the combined text to the PDF, wrapping long lines
    for line in feedback_text.split('\n'):
        pdf.multi_cell(180, 5, txt=line, ln=True)
    
    # Save the PDF in a temporary buffer
    feedback_pdf = io.BytesIO()
    pdf.output(feedback_pdf, 'F')
    feedback_pdf.seek(0)
    
    feedback_pdf_base64 = base64.b64encode(feedback_pdf.getvalue()).decode('utf-8')
    return feedback_text, feedback_pdf_base64


def generate_candidate_feedback_report(interview_transcript_text, resume_text, interviewer_requirements_text):
    # Combine the texts
    # feedback_text = f"Interview Transcript:\n{interview_transcript_text}\n\nResume Details:\n{resume_text}\n\nInterviewer Requirements:\n{interviewer_requirements_text}"
    email_prompt = f""" 
                Generate a personalized rejection email for a candidate who was not selected for the position. The email should be empathetic, professional, and provide constructive feedback based on the candidate's interview performance.
                **Subject**: Update on Your Application for {position} at {company_name}

                **Email Content**:
                - **Greeting**:
                - "Dear {name},"

                - **Thank You and Appreciation**:
                - "Thank you very much for your interest in the {position} role at {company_name} and for the time and effort you put into the interview process."

                - **Decision Notification**:
                - "After careful consideration, we have decided to move forward with another candidate. This decision was not easy due to the strong qualifications of all our candidates."

                - **Feedback for Improvement**:
                - **Performance Highlights**: "We were impressed by your expertise in (specific_skill_or_achievement). Your ability to (positive_aspect_from_interview) was particularly noteworthy."
                - **Areas for Improvement**: "We believe that enhancing your (specific_area_for_improvement) could strengthen your future applications. For example, (constructive_suggestion), such as (recommended_course_or_certification), might be beneficial."

                - **Encouragement**:
                - "We encourage you to apply for future opportunities at {company_name} that align with your skills and career goals."

                - **Closing Remarks**:
                - "We wish you all the best in your job search and future professional endeavors. Please feel free to reach out if you need more detailed feedback."

                - **Signature**:
                - "Warm regards,\n[Your Name]\n[Your Job Title]\n{company_name}\n[Contact Information]"

                
                """
    
    personalised_email = get_gemini_response(email_prompt)
    
    candidate_feedback = f""" 
                Generate a detailed feedback report for a candidate after the final interview round. The report should be structured to clearly summarize the candidate's performance, highlight their strengths, identify areas for improvement, and provide personalized development tips.

                **Feedback Report to the Interviewee:**

                **Candidate Name**: {name}
                **Position Applied For**: {position}
                **Date of interview**: date in transcript
                **Interviewing Company**: {company_name}

                **Performance Overview**:
                - Provide a detailed summary of the candidate's performance, focusing on key areas such as communication skills, technical knowledge, and problem-solving abilities. Highlight how these skills were demonstrated during the interview.

                **Strengths**:
                - Clearly outline the areas where the candidate excelled during the interview process. Examples might include proficiency in specific technical skills, effectiveness in communication, or the ability to think critically under pressure.

                **Areas for Improvement**:
                - Offer specific and actionable feedback on aspects of the candidate's performance that could be improved. Avoid generalizations; instead, reference particular moments or responses from the interview that could have been better handled. For instance, mention if the candidate needs to enhance their knowledge in a particular technology or suggest improving presentation skills for clearer articulation of ideas.

                **Personal Development Tips**:
                - Provide personalized advice tailored to the candidate's career aspirations and the job requirements they are aiming to meet. Recommend resources such as online courses, books, workshops, or professional groups that could help the candidate develop the skills that need improvement.

                **Closing Remarks**:
                - Encourage the candidate to continue refining their skills and to consider applying again in the future as they grow professionally. Express appreciation for the effort they put into the interview process and wish them success in their ongoing career journey.

                **Signature**:
                - "Best regards,\n[Interviewer's Name]\n[Interviewer's Job Title]\n[Company Name]"
                """
                
    
    candidate_feedback_text = get_gemini_response(candidate_feedback)
    
    # Create a PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 11)
    
    # Add the combined text to the PDF, wrapping long lines
    for line in candidate_feedback_text.split('\n'):
        pdf.multi_cell(180, 5, txt=line, ln=True)
    
    # Save the PDF in a temporary buffer
    candidate_feedback_pdf = io.BytesIO()
    pdf.output(candidate_feedback_pdf, 'F')
    candidate_feedback_pdf.seek(0)
    
    candidate_feedback_pdf_base64 = base64.b64encode(candidate_feedback_pdf.getvalue()).decode('utf-8')
    return personalised_email, candidate_feedback_text, candidate_feedback_pdf_base64


# Store feedback in a file-based system
def store_feedback(name, feedback_text, feedback_pdf_base64):
    if not os.path.exists('feedback_data.json'):
        with open('feedback_data.json', 'w') as file:
            json.dump({}, file)
    
    with open('feedback_data.json', 'r+') as file:
        data = json.load(file)
        data[name] = {
            "feedback_text": feedback_text,
            "feedback_pdf_base64": feedback_pdf_base64
        }
        file.seek(0)
        json.dump(data, file, indent=4)

# Load feedback using candidate name
def load_feedback(name):
    with open('feedback_data.json', 'r') as file:
        data = json.load(file)
        return data.get(name, {})

st.set_page_config(
    page_title="InterviewBuddy",
    page_icon="🖥️", 
    layout="wide"
)

# Initialize session state variables for button clicks
if 'submit1_clicked' not in st.session_state:
    st.session_state['submit1_clicked'] = False
if 'show_form' not in st.session_state:
    st.session_state['show_form'] = False
if 'candidates' not in st.session_state:
    st.session_state.candidates = []

# Define button click callbacks to set state
def on_submit1_clicked():
    st.session_state['submit1_clicked'] = True



selected = option_menu(
        menu_title = None,  #required
        options = ["Home", "Dashboard","About"], #required
        icons = ['house','star','person'],
        menu_icon = "cast",
        default_index=0,
        orientation="horizontal",
        styles={
        "container": {"padding": "0!important"},
        "icon": {"color": "White", "font-size": "13px"},
        "nav-link": {"font-size": "13px", "text-align": "middle", "margin":"0px","--hover-color": "#3d3d3d"},
        "nav-link-selected": {"background-color": "saffron"},
        }
        )

st.markdown("<h1 style='text-align:center; font-size:55px; color:#FF4B4B'>InterviewBuddy</h1>",unsafe_allow_html=True)
st.write('\n')
st.write('\n')

if selected == 'Home':
    col = st.columns([2,3])
    with col[0]:
        st.image('./assets/interview.jpg',use_column_width=True, output_format="JPG")
    with col[1]:
        with st.container():
            st.markdown("<h6 style='text-align:justify; font-size:20px; color:#FFFFFF'>Welcome to Interview Buddy, where we transform interview feedback into actionable growth using cutting-edge AI technology. Our platform offers a seamless integration of AI-enhanced tools to provide deep insights from your interviews. From automatic transcription using popular platforms like Google Meet and Zoom to detailed analysis with the Google Gemini Pro LLM, we ensure every aspect of your interview is captured and evaluated. Our comprehensive feedback reports not only highlight a candidate's strengths and areas for improvement but also align their responses with the job's requirements. Whether you're an interviewer looking to refine your hiring process or a candidate striving for self-improvement, Interview Buddy is your go-to resource for fostering professional development through precise, personalized feedback. Start your journey towards effective interviewing with us today!</h6>",unsafe_allow_html=True)
            
            st.subheader(" ")

if selected == "Dashboard":
    st.write('---')
    st.subheader("Create New Candidate")
    # button = st.button("Create New", type='primary')
    with st.expander("Ceate New Candidate Profile"):
        with st.form("new_candidate", clear_on_submit=True):
            
            name = st.text_input("Interview Full Name", placeholder="Raviteja Tanikella" )
            position = st.text_input("Position Applied", placeholder="Machine Learning Engineer")
            application_date = st.date_input("Date of Application")
            linkedin_url = st.text_input("LinkedIn Profile URL")
            email = st.text_input("Email ID",placeholder="ravi@uw.edu")
            
            interview_transcript = st.file_uploader("Upload Interview Script", type=['pdf', 'docx'], help="Please Upload a PDF or DOCX", key=1)
            
            resume = st.file_uploader("Upload Interviewee Resume", type=['pdf', 'docx'], help="Please Upload a PDF or DOCX", key=2)
            
            interviewer_requirements = st.file_uploader("Upload Interviewer Requirements and Job Description", type=['pdf', 'docx'], help="Please Upload a PDF or DOCX", key=3)
            
            remarks = st.text_input("Remarks", placeholder="Remarks on interviewee", help="Enter remarks if any")
            
            create = st.form_submit_button("Create Candidate Profile")

            if create:
                interview_transcript_text, resume_text, interviewer_requirements_text = input_pdf_text(interview_transcript, resume, interviewer_requirements)
                
                feedback_text, feedback_pdf_base64  = generate_feedback_report(interview_transcript_text, resume_text, interviewer_requirements_text)
                store_feedback(name, feedback_text, feedback_pdf_base64)
                
                candidate_info = {
                    "name": name,
                    "position": position,
                    "date": application_date,
                    "linkedin": linkedin_url,
                    "email": email,
                    "remarks": remarks,
                    "feedback_text": feedback_text,
                    "feedback_pdf_base64": feedback_pdf_base64
                }
                st.session_state.candidates.append(candidate_info)
        
    st.write('\n')
    st.markdown("<h1 style=' font-size:50px; color:#FF4B4B'; align='center'>Candidate Profiles</h1>",unsafe_allow_html=True)
    st.write("---")
    # Display all candidates
    for index, candidate in enumerate(st.session_state.candidates):
        with st.container(border=True):
            c = st.columns([1, 3])
            with c[0]:
                st.image('./assets/user.png', use_column_width=True)
            with c[1]:
                st.markdown(f"<h3 style='font-size:35px; color:#FF4B4B;'>{candidate['name']}</h3>", unsafe_allow_html=True)
                st.markdown(f"<h6 style='font-size:20px; color:#FFFFFF;'>Position Applied: {candidate['position']}</h6>", unsafe_allow_html=True)
                st.markdown(f"<h6 style='font-size:20px; color:#FFFFFF;'>Date of application: {candidate['date']}</h6>", unsafe_allow_html=True)
                st.markdown(f"<h6 style='font-size:20px; color:#FFFFFF;'>LinkedIn Profile: <a href='{candidate['linkedin']}' target='_blank'>{candidate['linkedin']}</a></h6>", unsafe_allow_html=True)
                
                st.markdown(f"<h6 style='font-size:20px; color:#FFFFFF;'>Email ID: {candidate['email']}</h6>", unsafe_allow_html=True)
                with st.expander("Read More"):
                    st.markdown(f"<h6 style='font-size:18px; color:#FFFFFF;'>Remarks: {candidate['remarks']}</h6>", unsafe_allow_html=True)
                    
                    feedback_data = load_feedback(name)
                    st.text_area("Feedback Text", value=feedback_data.get("feedback_text", ""), height=350, key=candidate['name'])
                    # Download button for feedback PDF
                    feedback_pdf_bytes = base64.b64decode(feedback_data.get("feedback_pdf_base64", ""))
                    #Button to download the feedback report.
                    st.download_button(
                        label="Download Feedback Report",
                        data=feedback_pdf_bytes,
                        file_name=f"{candidate['name']}_feedback_report.pdf",
                        mime="application/pdf"
                    )
                
                # Reject and Accept options
                # Add two buttons - Reject and Select
                # When select - display st.success --> profile saved for further rounds.
                
                #When reject
                # - Generate a specific feedback form for the user
                # - Generate and send a personalised mail to the user attaching report.
                # - update session of the reject button and display info that its been sent already.
                
                # Select button
                if st.button('Select', key=f"select_{index}", type='primary'):
                    st.success(f"Profile of {candidate['name']} saved for further rounds.")

                # Reject button
                if st.button('Reject', key=f"reject_{index}", type='primary'):
                    # Generate and send feedback
                    interview_transcript_text, resume_text, interviewer_requirements_text = input_pdf_text(interview_transcript, resume, interviewer_requirements)
                    personalised_email, candidate_feedback_text, candidate_feedback_pdf_base64 = generate_candidate_feedback_report(interview_transcript_text, resume_text, interviewer_requirements_text)
                    
                    receiver_email = "otpsender2084@gmail.com" #candidate['email']  # Need to change this
                    subject = "Thanks For Your Applictaion"
                    personalised_email = f"Dear {candidate['name']},{personalised_email}"
                    candidate_feedback_pdf_bytes = base64.b64decode(feedback_data.get("feedback_pdf_base64", ""))
                    # Send the mail with the attached PDF
                    send_mail(SENDER_EMAIL, receiver_email, MAIL_PASSWORD, subject, personalised_email, file_name=f"{candidate['name']}_feedback.pdf", file_data=candidate_feedback_pdf_bytes)
                    st.info(f"Feedback sent to {candidate['name']}'s email.")
            
if selected == "About":
    st.subheader("About the App")

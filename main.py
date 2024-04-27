import streamlit as st
from streamlit_option_menu import option_menu
import pybase64
import io
from dotenv import load_dotenv

load_dotenv()
import os
from PIL import Image
import PyPDF2 as pdf
import google.generativeai as genai
import time

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

st.set_page_config(
    page_title="InterviewBuddy",
    page_icon="🖥️", 
    layout="wide"
)

selected = option_menu(
        menu_title = None,  #required
        options = ["Home", "Dashboard","About"], #required
        icons = ['house','star','person'],
        menu_icon = "cast",
        default_index=0,
        orientation="horizontal",
        styles={
        "container": {"padding": "0!important"},
        "icon": {"color": "White", "font-size": "15px"},
        "nav-link": {"font-size": "15px", "text-align": "middle", "margin":"0px","--hover-color": "#3d3d3d"},
        "nav-link-selected": {"background-color": "saffron"},
        }
        )

st.markdown("<h1 style='text-align:center; font-size:55px; color:#FF4B4B'>InterviewBuddy</h1>",unsafe_allow_html=True)
st.write('\n')
st.write('\n')

if selected == 'Home':
    col = st.columns(2)
    with col[0]:
        st.image('./assets/interview.jpg',use_column_width=True, output_format="JPG")
    with col[1]:
        with st.container(border=True):
            st.write("Short Introduction of App")

if selected == "Dashboard":
    cols = st.columns([1,3,1])
    with cols[1]:    
        st.subheader("Upload Interview Script")
        interview_transcript = st.file_uploader("Choose your file", type=['pdf', 'docx'], help="Please Upload a PDF or DOCX", key=1)

        st.subheader("Upload Interviewee Resume")
        resume = st.file_uploader("Choose your file", type=['pdf', 'docx'], help="Please Upload a PDF or DOCX", key=2)

        st.subheader("Upload Interviewer Requirements and Job Description")
        interviewer_requirements = st.file_uploader("Choose your file", type=['pdf', 'docx'], help="Please Upload a PDF or DOCX", key=3)
        

if selected == "About":
    st.subheader("About the App")
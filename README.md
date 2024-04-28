# InterviewBuddy 👨🏻‍💻📄🚀

InterviewBuddy is an advanced interview assistance tool designed to enhance hiring quality and productivity by utilizing AI to provide deep insights into each interview process. Our system automatically generates a transcript from interviews conducted on Google Meet, analyzes it alongside the candidate's resume and interviewer requirements, and seamlessly integrates this information into a newly created candidate profile. Once the interview concludes, InterviewBuddy crafts a detailed feedback report for the interviewer, assessing how well the candidate's responses and profile align with the job role. This analysis aids interviewers in making informed decisions by highlighting strengths and areas for potential improvement. Additionally, if a candidate is not selected, InterviewBuddy generates a personalized feedback report and an email tailored to the candidate, offering constructive feedback on their performance and specific advice on areas to enhance. This feedback is crucial for candidates as it provides clear, actionable insights that can significantly aid in their job search journey, helping them understand and improve on aspects critical to their career progression.


## Sections
- [Model Arcitecture](#model-architecture)
- [Why is it Highly Essential?](#why-is-it-highly-essential)
- [What Motivated Us?](#what-motivated-us)
- [Key Tools and Technologies](#Key-Tools-and-Technologies)
- [Core Features & Functions](#Core-Features-&-Functions)
- [Personalised Email Communication](#personalised-email-communication)
- [Contributing](#contributing)

## Model Architecture
![architecture](https://github.com/TVR28/InterviewBuddy/assets/91713140/6d739eb6-85e1-437c-a7b4-8eabebfd0ff5)


## Why is it Highly Essential?
In today's highly competitive job market, the demand for precise and constructive feedback is more critical than ever. InterviewBuddy elevates the interview process by integrating advanced AI technologies to analyze interviews comprehensively. This approach not only refines hiring decisions but also enhances the developmental aspects of interviews. For interviewers, it offers deep insights into a candidate’s suitability, helping to identify the best fit for the organization and reduce the likelihood of costly hiring mistakes. For candidates, it provides clear and actionable feedback, which is vital for personal development and future interview preparations. By fostering a culture of feedback and learning, InterviewBuddy ensures that both parties can grow from each interaction, thereby making the entire recruitment process more transparent, effective, and equitable.

## What Motivated Us?
The inspiration for InterviewBuddy was driven by a glaring need to bridge the significant communication gap often found between interviewers and candidates. Traditional interviewing methods can leave both parties with unanswered questions and unclear evaluations, which can lead to ineffective hiring decisions and missed opportunities for candidates. We envisioned a tool that not only facilitates but also enriches the dialogue between the two parties. By providing detailed insights and structured feedback based on AI analysis of interview transcripts and related documents, InterviewBuddy aims to create a more informed and fair hiring process. Our goal is to transform how feedback is given and received in interviews, turning every interview into a valuable learning experience that aids in the professional growth of candidates and sharpens the decision-making skills of recruiters. This foundation of understanding and clarity is what we believe will ultimately lead to more successful employment outcomes and foster a more transparent job market.

## Key Tools and Technologies
- **PyPDF2**
- **Streamlit**
- **EmailMessage**
- **FPDF**
- **SMTPLib**
- **Google Gemini Pro API**
- **React**
- **RSuite**

## Core Features & Functions
### 1. Transcription of the Interview
- **Tools:** Use APIs or integrations available for platforms like Google Meet and Zoom to automatically transcribe the audio from the interviews.
- **Storage:** Save the transcriptions in a document format (like .txt or .docx) for easy processing.

### 2. Data Collection
- **Resume and Interviewer Requirements:** Collect the candidate’s resume and the interviewer's checklist or requirements for the position.
- **Job Description:** Include a detailed job description to compare against the candidate's responses.

### 3. Analysis Using Google Gemini Pro LLM
- **Input Data:** Provide the interview transcription, candidate’s resume, interviewer's requirements, and job description to the LLM.
- **Processing:** The LLM analyses how well the candidate's responses align with the job requirements and generates feedback based on the input data.

### 4. Feedback Reports
#### Feedback Report to the Interviewer (After every round)
- **Candidate Profile Matching:** Analysis of how the candidate’s qualifications and experience align with the job description.
- **Answer Alignment:** Evaluation of how the candidate’s answers match the interviewer's questions and the required job competencies.
- **Potential Red Flags:** Highlight any potential concerns or discrepancies noted during the interview.
- **Recommendations:** Suggest whether the candidate should proceed to the next round, based on the analysis.

#### Feedback Report to the Interviewee (After the final round)
- **Performance Overview:** Summarise the candidate's performance across different areas like communication skills, technical knowledge, and problem-solving abilities.
- **Strengths:** Highlight the areas where the candidate performed well.
- **Areas for Improvement:** Provide constructive feedback on areas where the candidate could improve, based on the job requirements and interview responses.
- **Personal Development Tips:** Offer personalised advice or resources to help the candidate improve their skills.

## Personalised Email Communication
### Personalised Rejection Email
1. **Greeting**
   - Address the candidate by name to personalise the message.
2. **Thank You and Appreciation**
   - Express gratitude for the candidate’s time, effort, and interest in the position.
   - Acknowledge the effort they put into the application and interview process.
3. **Decision Notification**
   - Clearly but gently inform them that they have not been selected for the position.
   - Be straightforward to avoid any ambiguity.
4. **Feedback for Improvement**
   - Performance Highlights: Start with positive feedback, noting what the candidate did well during the interview(s).
   - Areas for Improvement: Offer specific feedback based on their interview performance. Avoid generalizations; instead, point out specific moments or responses that could be improved.
5. **Encouragement**
   - Encourage the candidate to apply for future positions that match their skill set.
   - Suggest that they continue developing specific skills relevant to the industry or role they are interested in.
6. **Offer Additional Resources** (optional)
   - If possible, provide resources or recommendations that could help them improve. For example, suggest online courses, workshops, or books that focus on areas they need to strengthen.
7. **Closing Remarks**
   - Wish them success in their job search and future professional endeavours.
   - Keep the door open for future interactions, reinforcing that the rejection is not a reflection of their overall capabilities but rather a mismatch for the specific role.
8. **Signature**
   - End with a professional closing and include the interviewer’s name, position, and contact information.

## Sample Mail
```Mail
Subject: Update on Your Application for [Job Title] at [Company Name]

Dear [Candidate's Name],

Thank you very much for taking the time to interview for the position of [Job Title] with us. We truly appreciate your interest in [Company Name] and the effort you invested in the interview process.

After thorough deliberation, we have decided to proceed with another candidate for this role. This was a challenging decision due to the high caliber of applicants like yourself.

During our discussions, we were particularly impressed by your expertise in [specific skill or achievement]. Your ability to [mention a specific positive aspect from the interview, e.g., articulate complex ideas or lead project discussions] stood out to us.

However, we noted that enhancing your [specific area for improvement, e.g., familiarity with certain software, managerial experience, etc.] could further strengthen your candidacy for future roles of this nature. For instance, [provide a specific instance or constructive suggestion], such as engaging in [recommended course or certification] might offer valuable insights and hands-on experience.

We sincerely hope you will consider applying for future positions at [Company Name] as your career progresses, particularly those that align more closely with your remarkable skills and experiences.

We wish you success in all your professional endeavors and encourage you to continue pursuing opportunities in this field. If you have any questions or would like further feedback, please feel free to reach out.

Thank you once again for your interest in [Company Name] and for the vibrant conversation during your interviews.

Warm regards,

[Your Name]  
[Your Job Title]  
[Company Name]  
[Contact Information]
```
## Contributing

Contributions to ATSPro are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository to your own GitHub account.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a clear description of your changes.

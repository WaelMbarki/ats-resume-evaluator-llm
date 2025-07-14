import streamlit as st
import fitz  # PyMuPDF
import ollama

#conda activate "C:\Users\MSI\Documents\ml\deep learning\ats\venv"
#  PDF Text Extractor
def extract_text_from_pdf(uploaded_file):
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc: # stream tells PyMuPDF to load the PDF from memory instead of from disk.
        text = ""
        for page in doc:#loop through all the pages
            text += page.get_text() #extract text
    return text

# LLM Response from DeepSeek 
def get_ollama_response(job_description, resume_text, prompt):
    full_prompt = f"{prompt}\n\nJob Description:\n{job_description}\n\nResume:\n{resume_text}"
    
    response = ollama.chat(
        model='deepseek-r1:1.5b',
        messages=[
            {"role": "system", "content": "You are an expert technical recruiter."}, #This is the system message that sets the context or behavior of the AI.
            {"role": "user", "content": full_prompt} #The user message tells the AI what to do this time and provides specific info
        ]
    )
    return response['message']['content']

# Clean DeepSeek response , removing the thinking part
def clean_response(response):
    # Separate final report from thought process
    if "<think>" in response and "</think>" in response:
        reasoning = response.split("<think>")[1].split("</think>")[0]
        final_output = response.split("</think>")[1].strip()
    else:
        reasoning = ""
        final_output = response
    return final_output

#  Streamlit UI 
st.set_page_config(page_title="ATS Resume Expert")
st.header("🔍 ATS Resume Matching System")

input_text = st.text_area("🧾 Job Description:", key="input")
uploaded_file = st.file_uploader("📄 Upload your resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    st.success("✅ PDF Uploaded Successfully")

submit1 = st.button("🔎 Evaluate Resume Fit")
submit3 = st.button("📊 Get Match Percentage")

#  Prompts 
input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

# Evaluation Logic 
if submit1:
    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        response = get_ollama_response(input_text, resume_text, input_prompt1)
        st.subheader("📋 ATS Evaluation")
        st.write(clean_response(response))
    else:
        st.warning("⚠️ Please upload a resume.")

elif submit3:
    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        response = get_ollama_response(input_text, resume_text, input_prompt3)
        st.subheader("📈 Match Result")
        st.write(clean_response(response))
    else:
        st.warning("⚠️ Please upload a resume.")

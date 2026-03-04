import streamlit as st
import fitz
import spacy
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load NLP model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    st.error("Model not found.")

def extract_text(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    return "".join([page.get_text() for page in doc])

def extract_contact_info(text):
    email = re.findall(r'\S+@\S+', text)
    phone = re.findall(r'\+?\d[\d -]{8,12}\d', text)
    return email[0] if email else "Not found", phone[0] if phone else "Not found"

# --- UI Setup ---
st.set_page_config(page_title="Pro Resume Parser", layout="wide")
st.title("🚀 High-Value AI Resume Parser & Matcher")

# Sidebar for Job Description
st.sidebar.header("Target Job Description")
jd_text = st.sidebar.text_area("Paste the Job Description here...", height=300)

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file and jd_text:
    resume_text = extract_text(uploaded_file)
    email, phone = extract_contact_info(resume_text)
    
    # --- SMART MATCHING LOGIC ---
    # We compare the Resume text vs the Job Description text
    match_docs = [resume_text, jd_text]
    vectorizer = TfidfVectorizer()
    count_matrix = vectorizer.fit_transform(match_docs)
    
    # Calculate Similarity Score
    match_percentage = cosine_similarity(count_matrix)[0][1] * 100
    
    # --- DISPLAY RESULTS ---
    st.metric(label="Match Score", value=f"{round(match_percentage, 2)}%")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("📌 Candidate Details")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {phone}")
        
    with col2:
        if match_percentage > 70:
            st.success("🔥 Strong Candidate!")
        elif match_percentage > 40:
            st.warning("⚖️ Average Match")
        else:
            st.error("❌ Low Match")

    st.divider()
    with st.expander("View Extracted Resume Content"):
        st.write(resume_text)
else:
    st.info("Please paste a Job Description in the sidebar and upload a resume to see the match score!")
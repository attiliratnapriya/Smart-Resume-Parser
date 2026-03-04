# 🤖 Smart AI Resume Parser
A high-value project built to automate resume screening using Machine Learning and NLP.

## 🚀 Key Features
* **PDF Processing:** Extracts clean text from resumes using `PyMuPDF`.
* **Contact Extraction:** Identifies emails and phone numbers using `Regex`.
* **Smart Matcher:** Uses **TF-IDF** and **Cosine Similarity** to compare resumes against Job Descriptions.
* **Interactive UI:** A real-time dashboard built with `Streamlit`.

## 🛠️ Installation
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Download the NLP model: `python -m spacy download en_core_web_sm`
4. Run the app: `streamlit run app.py`

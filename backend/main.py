from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import docx
import tempfile
import re

app = FastAPI(title="ATS Resume Scorer")

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def extract_pdf_text(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + " "

    return text


def extract_docx_text(file_path):
    doc = docx.Document(file_path)

    text = ""

    for para in doc.paragraphs:
        text += para.text + " "

    return text


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)

    return text


def calculate_ats_score(resume_text, jd_text):

    resume_text = clean_text(resume_text)
    jd_text = clean_text(jd_text)

    jd_keywords = set(jd_text.split())

    if len(jd_keywords) == 0:
        return 0

    matched_keywords = 0

    for word in jd_keywords:
        if word in resume_text:
            matched_keywords += 1

    score = (matched_keywords / len(jd_keywords)) * 100

    return round(score)


@app.get("/")
def home():
    return {"message": "ATS Resume Scoring API Running"}


@app.post("/predict")
async def predict(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    suffix = resume.filename.split(".")[-1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=f".{suffix}"
    ) as temp_file:

        content = await resume.read()
        temp_file.write(content)

        temp_path = temp_file.name

    resume_text = ""

    if suffix.lower() == "pdf":
        resume_text = extract_pdf_text(temp_path)

    elif suffix.lower() in ["doc", "docx"]:
        resume_text = extract_docx_text(temp_path)

    else:
        return {"error": "Only PDF and DOCX files supported"}

    score = calculate_ats_score(
        resume_text,
        job_description
    )

    return {
        "ats_score": score
    }
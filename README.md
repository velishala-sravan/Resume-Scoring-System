# Resume-Scoring-System
Full-stack ATS Resume Scoring application using FastAPI for resume parsing and job description analysis.
# AI-Powered ATS Resume Scoring System

## Overview

This project is a full-stack ATS (Applicant Tracking System) Resume Scoring application built using FastAPI, HTML, CSS, and JavaScript.

The system allows users to upload a resume and provide a job description. It analyzes the resume against the job description and generates an ATS compatibility score based on keyword matching.

## Features

* Resume Upload (PDF/DOCX)
* Job Description Input
* ATS Score Prediction
* FastAPI Backend
* Responsive Frontend
* REST API Integration

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* FastAPI
* Python

### Libraries

* pdfplumber
* python-docx
* python-multipart

## Project Flow

User Uploads Resume
→ Resume Parsing
→ Job Description Analysis
→ Keyword Matching
→ ATS Score Calculation
→ Score Display

## Run Locally

Install dependencies:

pip install -r requirements.txt

Start the server:

python -m uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs

## Future Enhancements

* NLP-based semantic matching
* Resume ranking system
* Skill gap analysis
* Authentication and user accounts
* Cloud deployment
* Database integration


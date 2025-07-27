#  Adobe Hackathon - Round 1A: PDF Outline Extraction

## Overview
This is the submission for Round 1A of the Adobe India Hackathon 2025. It extracts clean hierarchical outlines (H1, H2, H3) from PDF documents, helping users to navigate large and unstructured PDFs.

## Features
- Automatically detects section titles using font size/layout
- Outputs document structure in JSON format
- Works offline, fast processing of large documents
- Built using PyMuPDF and Flask

## Tech Stack
- Python 3.9
- Flask
- PyMuPDF (`fitz`)
- Docker (for containerized setup)

## Folder Structure
.
├── app.py # Flask API route for /extract-outline
├── extract_outline.py # Core heading extraction logic
├── utils/
│ └── pdf_helper.py # PDF text block and layout utilities
├── Dockerfile # Docker configuration
├── requirements.txt # Python libraries
└── README.md # Documentatio

## How to Run

### Option 1: Run with Docker (Recommended)
```bash
docker build --platform linux/amd64 -t adobe-round1a .
docker run -p 5000:5000 --rm adobe-round1a

Option 2: Run Locally (Python)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
python app.py
API Usage
POST /extract-outline
Accepts one or more PDF files

Returns heading hierarchy

Example via Postman:
Method: POST

URL: http://localhost:5000/extract-outline

Body → form-data:

pdfs: [Upload one PDFs]

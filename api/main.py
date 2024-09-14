import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import PyPDF2
import openai

app = FastAPI()


def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    extracted_text = ""
    for page in reader.pages:
        extracted_text += page.extract_text()
    return extracted_text


def generate_resume_html(pdf_text, api_key):
    openai.api_key = api_key

    system_prompt = (
        "You are an expert resume generator. Given a LinkedIn resume text, extract details like "
        "Name, Summary, Experience, Education, Skills, and Contact Information. Then, convert "
        "this information into a clean and structured HTML resume format."
    )

    user_prompt = (
        f"Extract the following details and format them into HTML: Name, Summary, "
        f"Experience, Education, Skills, and Contact Information.\n\nResume Text:\n{pdf_text}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=2000,
        temperature=0.5
    )

    return response['choices'][0]['message']['content']


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    pdf_text = extract_text_from_pdf(file.file)
    resume_html = generate_resume_html(pdf_text)
    return HTMLResponse(content=resume_html)

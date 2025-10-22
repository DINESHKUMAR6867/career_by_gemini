import openai
from django.conf import settings
from io import BytesIO
from docx import Document
from PyPDF2 import PdfReader

openai.api_key = settings.OPENAI_API_KEY  # store in settings not hardcoded

# def extract_text_from_resume(resume_file):
#     """Extract text from PDF, DOCX, or TXT resume."""
#     filename = resume_file.name.lower()

#     if filename.endswith('.txt'):
#         return resume_file.read().decode('utf-8')

#     elif filename.endswith('.pdf'):
#         reader = PdfReader(BytesIO(resume_file.read()))
#         text = ""
#         for page in reader.pages:
#             text += page.extract_text() or ""
#         return text

#     elif filename.endswith('.docx'):
#         doc = Document(BytesIO(resume_file.read()))
#         text = "\n".join([p.text for p in doc.paragraphs])
#         return text

#     else:
#         raise ValueError("Unsupported file format. Please upload PDF, DOCX, or TXT.")

def extract_text_from_resume(career_cast):
    """Extract text from resume stored in database"""
    if not career_cast.resume_file_data:
        return ""
    
    try:
        import base64
        from io import BytesIO
        
        # Decode the base64 data
        file_data = base64.b64decode(career_cast.resume_file_data)
        file_like = BytesIO(file_data)
        
        # Extract text based on file type
        file_extension = os.path.splitext(career_cast.resume_file_name)[1].lower()
        
        if file_extension == '.pdf':
            # PDF extraction logic
            text = extract_text_from_pdf(file_like)
        elif file_extension in ['.docx', '.doc']:
            # DOCX extraction logic  
            text = extract_text_from_docx(file_like)
        elif file_extension == '.txt':
            # TXT extraction logic
            text = file_like.read().decode('utf-8')
        else:
            text = ""
            
        return text
        
    except Exception as e:
        print(f"Error extracting text from resume: {e}")
        return ""


def generate_teleprompter_text(job_title, job_description, resume_text):
    """Generate a full 2–3 minute teleprompter script based on resume, job title, and description."""
    try:
        messages = [
            {
                "role": "system",
                "content": "You are an expert career coach and script writer. "
                           "Generate a professional, natural, conversational self-introduction teleprompter script."
            },
            {
                "role": "user",
                "content": f"""
Job Title: {job_title}
Job Description: {job_description}
Resume:
{resume_text}

Using the above information, write a 2–3 minute teleprompter script for a video introduction.
The script should:
- Sound like the candidate is speaking naturally
- Highlight key experiences, skills, and achievements from the resume
- Align the strengths to the job description
- Maintain a friendly but professional tone
- Include a short closing line
                """
            }
        ]

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=900,  # 👈 enough for 2–3 minutes of text
            temperature=0.7
        )

        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"Error generating teleprompter text: {e}"


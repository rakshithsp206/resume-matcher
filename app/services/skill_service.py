from utils.text_extracter import extract_text_from_pdf
from utils.text_preprocessor import preprocess_text
from services.skill_extractor import extract_skills
from services.skill_comparator import compare_skills

def get_skills_compared(pdf_bytes, job_desc):
    # Extract text from the uploaded resume PDF
    resume_text = extract_text_from_pdf(pdf_bytes)

    # Preprocess the extracted text and job description
    preprocessed_resume = preprocess_text(resume_text)
    preprocessed_job_desc = preprocess_text(job_desc)

    # Extract skills from the preprocessed resume and job description
    resume_skills = extract_skills(preprocessed_resume)
    job_desc_skills = extract_skills(preprocessed_job_desc)

    # Compare the extracted skills
    skill_comparison = compare_skills(resume_skills, job_desc_skills)

    return skill_comparison
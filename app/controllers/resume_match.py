from services.resume_service import get_similarity_score
from services.skill_service import get_skills_compared

async def match_resume(file, job_desc):
    pdf_bytes = await file.read()  # Read the uploaded file as bytes
    similarity_score = get_similarity_score(pdf_bytes, job_desc)

    skill_comparison = get_skills_compared(pdf_bytes, job_desc)
    
    return {
        "similarity_score": similarity_score,
        "skills": skill_comparison
    }
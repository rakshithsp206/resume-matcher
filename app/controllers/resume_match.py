from app.services.resume_service import get_similarity_score
from app.services.skill_service import get_skills_compared
from app.services.match_engine import match_percentage
from app.schemas.response import ResumeMatchResponse

async def match_resume(file: UploadFile, job_desc: str)-> ResumeMatchResponse:
    pdf_bytes = await file.read()  # Read the uploaded file as bytes
    
    semantic_similarity_percent = get_similarity_score(pdf_bytes, job_desc)

    skill_comparison = get_skills_compared(pdf_bytes, job_desc)
    
    overall_match_percentage = match_percentage(semantic_similarity_percent, skill_comparison.skill_match_percentage)

    return ResumeMatchResponse(
        semantic_match_percentage=semantic_similarity_percent,
        skills=skill_comparison,
        overall_match_percentage=overall_match_percentage
    )
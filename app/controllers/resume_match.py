from app.services.resume_service import get_similarity_score
from app.services.skill_service import get_skills_compared
from app.services.match_engine import match_percentage
from app.schemas.response import ResumeMatchResponse
from app.services.project_service import get_projects_data
from app.services.project_relevance import get_avg_relevance
from fastapi import HTTPException, status, UploadFile

async def match_resume(file: UploadFile, job_description: JobDescription)-> ResumeMatchResponse:
    try:
        pdf_bytes = await file.read()  # Read the uploaded file as bytes
        job_desc = job_description.job_description  # Extract the job description text from the JobDescription object

        semantic_similarity_percent = get_similarity_score(pdf_bytes, job_desc)

        skill_comparison = get_skills_compared(pdf_bytes, job_desc)
        
        projects_data = get_projects_data(pdf_bytes, job_desc)

        overall_match_percentage = match_percentage(semantic_similarity_percent, skill_comparison.skill_match_percentage,get_avg_relevance(projects_data))

        return ResumeMatchResponse(
            job_title=job_description.job_title,
            company_name=job_description.company_name,
            semantic_match_percentage=semantic_similarity_percent,
            skills=skill_comparison,
            projects=projects_data,
            overall_match_percentage=overall_match_percentage
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing the resume: {str(e)}"
        )

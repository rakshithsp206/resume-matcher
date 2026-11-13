from app.services.resume_service import get_similarity_score
from app.services.skill_service import get_skills_compared
from app.services.match_engine import match_percentage
from app.schemas.response import ResumeMatchResponse
from app.services.project_service import get_projects_data
from app.services.project_relevance import get_avg_relevance
from app.utils.text_extracter import extract_text_from_pdf
from app.utils.pdf_validator import validate_pdf_file
from fastapi import HTTPException, status, UploadFile
import logging
logger = logging.getLogger(__name__)

async def match_resume(file: UploadFile, job_description: JobDescription, user: dict)-> ResumeMatchResponse:
    try:
        MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

        file_bytes = await file.read(MAX_FILE_SIZE + 1)

        if len(file_bytes) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                detail="File size cannot exceed 5 MB."
            )
        
        validate_pdf_file(file, file_bytes)  # Validate the uploaded PDF file
        resume_text = extract_text_from_pdf(file_bytes)  # Extract text from the PDF bytes
        job_desc = job_description.job_description  # Extract the job description text from the JobDescription object

        semantic_similarity_percent = get_similarity_score(resume_text, job_desc)

        skill_comparison = get_skills_compared(resume_text, job_desc)

        projects_data = get_projects_data(resume_text, job_desc)

        overall_match_percentage = match_percentage(semantic_similarity_percent, skill_comparison.skill_match_percentage,get_avg_relevance(projects_data))

        return ResumeMatchResponse(
            job_title=job_description.job_title,
            company_name=job_description.company_name,
            semantic_match_percentage=semantic_similarity_percent,
            skills=skill_comparison,
            projects=projects_data,
            overall_match_percentage=overall_match_percentage
        )
    except ValueError as ve:
        logger.error(f"ValueError: {ve}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ve)
        )
    except Exception as e:
        logger.exception("An error occurred while processing the resume.")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing the resume"
        )

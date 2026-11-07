from fastapi import APIRouter, UploadFile, File, Form
from app.controllers.resume_match import match_resume
from app.schemas.request import JobDescription
from app.schemas.response import ResumeMatchResponse
router = APIRouter()

@router.post("/resume")
async def upload_resume(file: UploadFile = File(...), job_desc: JobDescription = Form(...))-> ResumeMatchResponse:
    return await match_resume(file, job_desc.job_description)
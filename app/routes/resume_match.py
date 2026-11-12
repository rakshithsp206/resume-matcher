from fastapi import APIRouter, UploadFile, File, Form, Depends
from app.dependencies.auth_dependency import get_current_user
from app.controllers.resume_match import match_resume
from app.schemas.request import JobDescription
from app.schemas.response import ResumeMatchResponse

router = APIRouter()

@router.post("/resume")
async def upload_resume(file: UploadFile = File(...), job_desc: JobDescription = Form(...),user:dict = Depends(get_current_user))-> ResumeMatchResponse:
    return await match_resume(file, job_desc)
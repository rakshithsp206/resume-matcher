from fastapi import APIRouter, UploadFile, File, Form
from controllers.resume_match import match_resume

router = APIRouter()

@router.post("/resume")
async def upload_resume(file: UploadFile = File(...),job_desc: str = Form(...)):
    return await match_resume(file, job_desc);
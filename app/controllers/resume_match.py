from services.resume_service import get_similarity_score

async def match_resume(file, job_desc):
    pdf_bytes = await file.read()  # Read the uploaded file as bytes
    similarity_score = get_similarity_score(pdf_bytes, job_desc)
    return {"similarity_score": similarity_score}
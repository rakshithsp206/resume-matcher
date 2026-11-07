from fastapi.responses import JSONResponse

def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"success": False, "message": "Job description validation failed : "+exc.errors()[0]['msg']},
    )
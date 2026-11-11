from fastapi import FastAPI 
from app.routes.resume_match import router as resume_router
from app.routes.auth_route import router as auth_router
from app.exception_handler.job_desc_validation_error import validation_exception_handler
from fastapi.exceptions import RequestValidationError

app = FastAPI()

app.include_router(resume_router, prefix="/api")
app.include_router(auth_router, prefix="/api/auth")

app.add_exception_handler(RequestValidationError, validation_exception_handler)
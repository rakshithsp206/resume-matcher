from fastapi import FastAPI 
from app.routes.resume_match import router
from app.exception_handler.job_desc_validation_error import validation_exception_handler
from fastapi.exceptions import RequestValidationError

app = FastAPI()

app.include_router(router, prefix="/api")

app.add_exception_handler(RequestValidationError, validation_exception_handler)
from fastapi import FastAPI 
from routes.resume_match import router
app = FastAPI()

app.include_router(router, prefix="/api")
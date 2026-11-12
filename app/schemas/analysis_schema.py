from pydantic import Field
from app.schemas.response import ResumeMatchResponse
from datetime import datetime

class AnalysisSchema(ResumeMatchResponse):
    user_id: str = Field(..., description="The ID of the user who uploaded the resume.")
    created_at: datetime = Field(..., description="The timestamp when the analysis was created.")
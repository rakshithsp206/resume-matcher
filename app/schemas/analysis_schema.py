from pydantic import Field,BaseModel
from app.schemas.response import ResumeMatchResponse
from datetime import datetime
from typing import List

class AnalysisSchema(ResumeMatchResponse):
    user_id: str = Field(..., description="The ID of the user who uploaded the resume.")
    created_at: datetime = Field(..., description="The timestamp when the analysis was created.")

class AnalysisListResponse(BaseModel):
    page: int
    limit: int
    total: int
    total_pages: int
    analyses: List[AnalysisSchema]
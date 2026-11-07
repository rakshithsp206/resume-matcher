from pydantic import BaseModel, Field

class JobDescription(BaseModel):
    job_description: str = Field(min_length=20, description="The job description text to match against the resume.")
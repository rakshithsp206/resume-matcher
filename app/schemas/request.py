from pydantic import BaseModel, Field

class JobDescription(BaseModel):
    job_title: str = Field(min_length=5, description="The title of the job for which the resume is being matched.")
    company_name: str = Field(min_length=2, description="The name of the company offering the job.")
    job_description: str = Field(min_length=20, description="The job description text to match against the resume.")
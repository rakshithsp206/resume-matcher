from pydantic import BaseModel, Field

class SkillComparisonResponse(BaseModel):
    matched_skills: list[str] = Field(..., description="List of skills that match between the resume and job description.")
    missing_skills: list[str] = Field(..., description="List of skills that are present in the job description but missing in the resume.")
    additional_skills: list[str] = Field(..., description="List of skills that are present in the resume but not required by the job description.")
    skill_match_percentage: float = Field(ge=0, le=100, description="Percentage of skills matched between the resume and job description.")

class ProjectsResponse(BaseModel):
    name: str = Field(..., description="Name of the project.")
    description: str = Field(..., description="Description of the project.")
    skills: dict = Field(..., description="Skills extracted from the project description.")
    relevance: float = Field(ge=0, le=100, description="Relevance score of the project to the job description.")
    
class ResumeMatchResponse(BaseModel):
    job_title: str = Field(..., description="The title of the job for which the resume is being matched.")
    company_name: str = Field(..., description="The name of the company offering the job.")
    semantic_match_percentage: float = Field(ge=0, le=100, description="Percentage of semantic similarity between the resume and job description.")
    skills: SkillComparisonResponse = Field(..., description="Detailed skill comparison between the resume and job description.")
    projects: list[ProjectsResponse] = Field(..., description="List of projects extracted from the resume.")
    overall_match_percentage: float = Field(ge=0, le=100, description="Overall match percentage considering both semantic similarity and skill comparison.")
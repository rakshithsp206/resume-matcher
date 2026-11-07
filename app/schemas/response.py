from pydantic import BaseModel, Field

class SkillComparisonResponse(BaseModel):
    matched_skills: list[str] = Field(..., description="List of skills that match between the resume and job description.")
    missing_skills: list[str] = Field(..., description="List of skills that are present in the job description but missing in the resume.")
    additional_skills: list[str] = Field(..., description="List of skills that are present in the resume but not required by the job description.")
    skill_match_percentage: float = Field(ge=0, le=100, description="Percentage of skills matched between the resume and job description.")

class ResumeMatchResponse(BaseModel):
    semantic_match_percentage: float = Field(ge=0, le=100, description="Percentage of semantic similarity between the resume and job description.")
    skills: SkillComparisonResponse = Field(..., description="Detailed skill comparison between the resume and job description.")
    overall_match_percentage: float = Field(ge=0, le=100, description="Overall match percentage considering both semantic similarity and skill comparison.")
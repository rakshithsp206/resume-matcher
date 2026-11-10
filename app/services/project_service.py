from app.services.project_extractor import extract_individual_projects
from app.services.project_skill_extractor import extract_skills_from_projects
from app.services.project_relevance import calculate_projects_relevance
from app.utils.text_extracter import extract_text_from_pdf
from app.utils.text_preprocessor import preprocess_text

def get_projects_data(pdf_bytes: bytes, job_description: str) -> list[dict[str, str]]:
    resume_text = extract_text_from_pdf(pdf_bytes)
    job_description = preprocess_text(job_description)

    projects = extract_individual_projects(resume_text)
    projects_with_skills = extract_skills_from_projects(projects)
    projects_with_relevance = calculate_projects_relevance(projects_with_skills, job_description)

    return projects_with_relevance
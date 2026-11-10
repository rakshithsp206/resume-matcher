from app.services.skill_extractor import extract_skills

def extract_skills_from_projects(projects: list[dict[str, str]]) -> list[dict[str, str]]:
    for project in projects:
        project_description = project.get("description", "")
        project_skills = extract_skills(project_description)
        project["skills"] = project_skills
    return projects
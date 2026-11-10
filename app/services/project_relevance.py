from app.services.skill_extractor import extract_skills
from app.services.skill_comparator import compare_skills
from app.models.semantic_model import get_embeddings
from app.models.similarity_model import calculate_similarity

def calculate_projects_relevance(projects: list[dict[str, str]], job_desc: str) -> list[dict[str, str]]:
    job_disc_skills = extract_skills(job_desc)
    for project in projects:
        project_skills = project.get("skills", {})
        skill_relevance = compare_skills(project_skills, job_disc_skills).get("skill_match_percentage", 0)

        documents = [project.get("description", ""), job_desc]
        embeddings = get_embeddings(documents)
        semantic_relevance = round(calculate_similarity(embeddings)*100, 2)

        project["relevance"] = round(skill_relevance*0.5 + semantic_relevance*0.5, 2)
    return projects

def get_avg_relevance(projects: list[dict[str, str]]) -> float:
    if not projects:
        return 0.0
    total_relevance = sum(project.get("relevance", 0) for project in projects)
    avg_relevance = total_relevance / len(projects)
    return round(avg_relevance, 2)
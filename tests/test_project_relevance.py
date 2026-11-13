
from app.services.project_relevance import (
    calculate_projects_relevance,
    get_avg_relevance
)


def test_calculate_project_relevance(monkeypatch):
    # Mock semantic embeddings and similarity.
    monkeypatch.setattr(
        "app.services.project_relevance.get_embeddings",
        lambda documents: [[1], [2]]
    )

    monkeypatch.setattr(
        "app.services.project_relevance.calculate_similarity",
        lambda embeddings: 0.8
    )

    projects = [
        {
            "name": "Resume Matcher",
            "description": "Built using Python and FastAPI",
            "skills": {
                "programming_languages": ["Python"],
                "frameworks_and_libraries": ["FastAPI"]
            }
        }
    ]

    job_desc = "Python FastAPI developer"

    result = calculate_projects_relevance(projects, job_desc)

    # Skill relevance = 100%
    # Semantic relevance = 80%
    # Final relevance = 90%
    assert result[0]["relevance"] == 90.0


def test_project_with_no_matching_skills(monkeypatch):
    monkeypatch.setattr(
        "app.services.project_relevance.get_embeddings",
        lambda documents: [[1], [2]]
    )

    monkeypatch.setattr(
        "app.services.project_relevance.calculate_similarity",
        lambda embeddings: 0.6
    )

    projects = [
        {
            "name": "Java Project",
            "description": "Built using Java",
            "skills": {
                "programming_languages": ["Java"]
            }
        }
    ]

    result = calculate_projects_relevance(
        projects,
        "Python developer"
    )

    # Skill relevance = 0%
    # Semantic relevance = 60%
    # Final relevance = 30%
    assert result[0]["relevance"] == 30.0


def test_empty_projects():
    result = calculate_projects_relevance([], "Python developer")

    assert result == []


def test_average_project_relevance():
    projects = [
        {"name": "Project 1", "relevance": 80.0},
        {"name": "Project 2", "relevance": 60.0},
        {"name": "Project 3", "relevance": 90.0}
    ]

    result = get_avg_relevance(projects)

    assert result == 76.67


def test_average_relevance_with_empty_projects():
    result = get_avg_relevance([])

    assert result == 0.0


def test_average_relevance_with_missing_score():
    projects = [
        {"name": "Project 1", "relevance": 80.0},
        {"name": "Project 2"}
    ]

    result = get_avg_relevance(projects)

    assert result == 40.0

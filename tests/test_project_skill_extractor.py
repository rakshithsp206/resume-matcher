
from app.services.project_skill_extractor import (
    extract_skills_from_projects
)


def test_extract_skills_from_single_project():
    projects = [
        {
            "name": "Resume Matcher",
            "description": "Built using Python, FastAPI and MongoDB"
        }
    ]

    result = extract_skills_from_projects(projects)

    assert len(result) == 1
    assert "Python" in result[0]["skills"]["programming_languages"]
    assert "FastAPI" in result[0]["skills"]["frameworks_and_libraries"]
    assert "MongoDB" in result[0]["skills"]["databases"]


def test_extract_skills_from_multiple_projects():
    projects = [
        {
            "name": "Project 1",
            "description": "Developed using Python and Django"
        },
        {
            "name": "Project 2",
            "description": "Developed using Java and MySQL"
        }
    ]

    result = extract_skills_from_projects(projects)

    assert len(result) == 2

    assert "Python" in result[0]["skills"]["programming_languages"]
    assert "Django" in result[0]["skills"]["frameworks_and_libraries"]

    assert "Java" in result[1]["skills"]["programming_languages"]
    assert "MySQL" in result[1]["skills"]["databases"]


def test_project_with_no_skills():
    projects = [
        {
            "name": "Reading Tracker",
            "description": "A simple application for tracking books"
        }
    ]

    result = extract_skills_from_projects(projects)

    assert result[0]["skills"] == {}


def test_empty_project_description():
    projects = [
        {
            "name": "Empty Project",
            "description": ""
        }
    ]

    result = extract_skills_from_projects(projects)

    assert result[0]["skills"] == {}


def test_empty_project_list():
    result = extract_skills_from_projects([])

    assert result == []


def test_original_project_data_is_preserved():
    projects = [
        {
            "name": "Resume Matcher",
            "description": "Built using Python"
        }
    ]

    result = extract_skills_from_projects(projects)

    assert result[0]["name"] == "Resume Matcher"
    assert result[0]["description"] == "Built using Python"
    assert "skills" in result[0]

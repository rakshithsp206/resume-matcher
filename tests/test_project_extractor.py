
from app.services.project_extractor import (
    extract_project_section,
    is_project_title,
    extract_individual_projects
)


SAMPLE_RESUME = """
Education
B.Tech Computer Science

Projects

Resume Matcher
Built an AI resume matching system using Python,
FastAPI and Sentence Transformers.

College Management System
Developed a desktop application using Java,
JDBC and MySQL.

Quiz Application
Created a quiz application using Java Swing.

Skills
Python, Java, SQL
"""


def test_extract_project_section():
    result = extract_project_section(SAMPLE_RESUME)

    assert "Resume Matcher" in result
    assert "College Management System" in result
    assert "Quiz Application" in result
    assert "Skills" not in result


def test_no_project_section():
    resume = """
    Education
    B.Tech Computer Science

    Skills
    Python, Java
    """

    result = extract_project_section(resume)

    assert result == ""


def test_extract_individual_projects():
    projects = extract_individual_projects(SAMPLE_RESUME)

    assert len(projects) == 3

    assert projects[0]["name"] == "Resume Matcher"
    assert projects[1]["name"] == "College Management System"
    assert projects[2]["name"] == "Quiz Application"


def test_project_descriptions():
    projects = extract_individual_projects(SAMPLE_RESUME)

    assert "Python" in projects[0]["description"]
    assert "Java" in projects[1]["description"]
    assert "Java Swing" in projects[2]["description"]


def test_is_project_title():
    assert is_project_title("Resume Matcher") is True
    assert is_project_title("College Management System") is True


def test_action_verb_line_is_not_project_title():
    assert is_project_title("Developed an application") is False


def test_bullet_point_is_not_project_title():
    assert is_project_title("- Built an application") is False


def test_empty_resume():
    projects = extract_individual_projects("")

    assert projects == []

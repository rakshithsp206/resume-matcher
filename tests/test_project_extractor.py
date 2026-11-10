from app.services.project_extractor import (
    extract_project_section,
    extract_individual_projects
)
from app.services.project_skill_extractor import extract_skills_from_projects
from app.services.project_relevance import calculate_projects_relevance

resume_text = """
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


#project_section = extract_project_section(resume_text)

projects = extract_individual_projects(resume_text)

# for project in projects:
#     print(project)

projects = extract_skills_from_projects(projects)

projects = calculate_projects_relevance(projects, "Python, FastAPI, SQL")

for project in projects:    
    print(project)
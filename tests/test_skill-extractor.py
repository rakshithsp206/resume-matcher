
from app.services.skill_extractor import extract_skills

resume_text = """
Developed applications using Python, Java and FastAPI.
Experienced with MySQL, MongoDB and Git.
Knowledge of Machine Learning, Deep Learning and NLP.
Strong understanding of DSA and OOP.
"""

result = extract_skills(resume_text)

print(result)

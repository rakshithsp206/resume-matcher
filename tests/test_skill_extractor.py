
from app.services.skill_extractor import extract_skills


def test_extract_programming_languages():
    text = "Experienced in Python, Java and C++."

    result = extract_skills(text)

    assert "programming_languages" in result
    assert "Python" in result["programming_languages"]
    assert "Java" in result["programming_languages"]
    assert "C++" in result["programming_languages"]


def test_extract_frameworks_and_libraries():
    text = "Developed applications using FastAPI and React."

    result = extract_skills(text)

    assert "FastAPI" in result["frameworks_and_libraries"]
    assert "React" in result["frameworks_and_libraries"]


def test_extract_databases():
    text = "Worked with MySQL and MongoDB."

    result = extract_skills(text)

    assert "MySQL" in result["databases"]
    assert "MongoDB" in result["databases"]


def test_extract_ai_ml_skills():
    text = "Knowledge of Machine Learning, Deep Learning and NLP."

    result = extract_skills(text)

    assert "Machine Learning" in result["ai_ml"]
    assert "Deep Learning" in result["ai_ml"]
    assert "Natural Language Processing" in result["ai_ml"]


def test_case_insensitive_extraction():
    text = "PYTHON FASTAPI MONGODB"

    result = extract_skills(text)

    assert "Python" in result["programming_languages"]
    assert "FastAPI" in result["frameworks_and_libraries"]
    assert "MongoDB" in result["databases"]


def test_alias_extraction():
    text = "I know cpp, sklearn, vscode and golang."

    result = extract_skills(text)

    assert "C++" in result["programming_languages"]
    assert "Scikit-learn" in result["frameworks_and_libraries"]
    assert "VS Code" in result["tools"]
    assert "Go" in result["programming_languages"]


def test_no_skills_found():
    text = "I enjoy reading books and playing football."

    result = extract_skills(text)

    assert result == {}


def test_empty_input():
    result = extract_skills("")

    assert result == {}

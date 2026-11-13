
from app.services.skill_comparator import (
    flatten_skills,
    compare_skills
)


def test_flatten_skills():
    skills = {
        "programming_languages": ["Python", "Java"],
        "databases": ["MySQL", "MongoDB"]
    }

    result = flatten_skills(skills)

    assert result == {"Python", "Java", "MySQL", "MongoDB"}


def test_compare_matching_skills():
    resume_skills = {
        "programming_languages": ["Python", "Java"],
        "databases": ["MySQL"]
    }

    job_skills = {
        "programming_languages": ["Python", "C++"],
        "databases": ["MySQL"]
    }

    result = compare_skills(resume_skills, job_skills)

    assert result["matched_skills"] == ["MySQL", "Python"]
    assert result["missing_skills"] == ["C++"]
    assert result["additional_skills"] == ["Java"]
    assert result["skill_match_percentage"] == 66.67


def test_all_skills_match():
    skills = {
        "programming_languages": ["Python", "Java"]
    }

    result = compare_skills(skills, skills)

    assert result["matched_skills"] == ["Java", "Python"]
    assert result["missing_skills"] == []
    assert result["additional_skills"] == []
    assert result["skill_match_percentage"] == 100.0


def test_no_matching_skills():
    resume_skills = {
        "programming_languages": ["Python"]
    }

    job_skills = {
        "databases": ["MongoDB"]
    }

    result = compare_skills(resume_skills, job_skills)

    assert result["matched_skills"] == []
    assert result["missing_skills"] == ["MongoDB"]
    assert result["additional_skills"] == ["Python"]
    assert result["skill_match_percentage"] == 0.0


def test_empty_job_skills():
    resume_skills = {
        "programming_languages": ["Python"]
    }

    job_skills = {}

    result = compare_skills(resume_skills, job_skills)

    assert result["matched_skills"] == []
    assert result["missing_skills"] == []
    assert result["additional_skills"] == ["Python"]
    assert result["skill_match_percentage"] == 0.0


def test_both_skill_sets_empty():
    result = compare_skills({}, {})

    assert result["matched_skills"] == []
    assert result["missing_skills"] == []
    assert result["additional_skills"] == []
    assert result["skill_match_percentage"] == 0.0


def flatten_skills(skills: dict) -> set:
    """
    Convert categorized skills into a flat set.
    """

    result = set()

    for category_skills in skills.values():
        result.update(category_skills)

    return result


def compare_skills(resume_skills: dict, job_skills: dict):

    resume_set = flatten_skills(resume_skills)
    job_set = flatten_skills(job_skills)

    # Skills present in both
    matched = resume_set & job_set

    # Skills required by job but absent in resume
    missing = job_set - resume_set

    # Skills in resume but not required by job
    additional = resume_set - job_set

    # Calculate match percentage
    if not job_set:
        match_percentage = 0.0
    else:
        match_percentage = (
            len(matched) / len(job_set)
        ) * 100

    return {
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
        "additional_skills": sorted(additional),
        "match_percentage": round(match_percentage, 2)
    }

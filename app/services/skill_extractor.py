
import re

from models.skill_data import SKILL_DATA


def extract_skills(text: str):

    text = text.lower()

    extracted_skills = {}

    for category, skills in SKILL_DATA.items():

        category_skills = []

        for skill, aliases in skills.items():

            for alias in aliases:

                # Escape special regex characters
                pattern = r"(?<!\w)" + re.escape(alias.lower()) + r"(?!\w)"

                if re.search(pattern, text):
                    category_skills.append(skill)
                    break

        if category_skills:
            extracted_skills[category] = category_skills

    return extracted_skills

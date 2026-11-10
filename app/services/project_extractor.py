
import re


PROJECT_HEADINGS = [
    "projects",
    "academic projects",
    "personal projects",
    "key projects",
    "relevant projects",
    "project experience"
]

NEXT_SECTION_HEADINGS = [
    "education",
    "experience",
    "work experience",
    "internships",
    "skills",
    "technical skills",
    "certifications",
    "achievements",
    "positions of responsibility"
]


def extract_project_section(text:str) -> str:

    lines = text.splitlines()

    start_index = None
    end_index = len(lines)

    for i, line in enumerate(lines):

        heading = line.strip().lower()

        heading = re.sub(r"[:\-\s]+$", "", heading)

        if heading in PROJECT_HEADINGS:
            start_index = i + 1
            break

    if start_index is None:
        return ""

    for i in range(start_index, len(lines)):

        heading = lines[i].strip().lower()
        heading = re.sub(r"[:\-\s]+$", "", heading)

        if heading in NEXT_SECTION_HEADINGS:
            end_index = i
            break

    project_text = "\n".join(lines[start_index:end_index])

    return project_text.strip()



ACTION_VERBS = {
    "built", "developed", "created", "designed",
    "implemented", "engineered", "implemented",
    "integrated", "worked", "used", "programmed",
    "created", "deployed", "analyzed", "automated",
    "applied", "optimized", "enhanced", "tested",
}


def is_project_title(line: str) -> bool:

    line = line.strip()

    if not line:
        return False

    # Ignore bullet points
    if line.startswith(("-", "•", "*", "▪")):
        return False

    # Project titles are generally short
    if len(line) > 100:
        return False

    # Ignore sentence-like lines
    if line.endswith((".", "!", "?", ";")):
        return False

    first_word = re.split(r"\s+", line.lower())[0]

    if first_word in ACTION_VERBS:
        return False

    return True


def extract_individual_projects(resume_text: str) -> list[dict[str, str]]:

    project_text = extract_project_section(resume_text)
    lines = project_text.splitlines()

    projects = []
    current_project = None

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if is_project_title(line):

            if current_project:
                projects.append(current_project)

            current_project = {
                "name": line,
                "description": ""
            }

        elif current_project:

            current_project["description"] += " " + line.lstrip("-•*▪").strip()

    if current_project:
        projects.append(current_project)

    return projects

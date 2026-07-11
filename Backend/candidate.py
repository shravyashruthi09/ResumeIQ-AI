import re


# ==========================================================
# FULL-TIME JOB TITLES
# ==========================================================

FULL_TIME_ROLES = [

    "software engineer",
    "software developer",
    "python developer",
    "backend developer",
    "frontend developer",
    "full stack developer",

    "data scientist",
    "data analyst",
    "machine learning engineer",

    "devops engineer",
    "cloud engineer",

    "senior",
    "lead",
    "associate"

]


# ==========================================================
# FRESHER EXPERIENCE
# ==========================================================

FRESHER_KEYWORDS = [

    "intern",
    "internship",

    "training",
    "foundation",

    "bootcamp",

    "student",

    "academic project",
    "college project",

    "capstone",

    "code unnati",

    "virtual internship"

]


# ==========================================================
# DETECT CANDIDATE TYPE
# ==========================================================

import re

def detect_candidate_type(resume_text: str):

    text = resume_text.lower()

    # --------------------------------------------------
    # Strong indicators of a full-time experienced candidate
    # --------------------------------------------------

    experience_titles = [
        "software engineer",
        "software developer",
        "backend developer",
        "frontend developer",
        "full stack developer",
        "data scientist",
        "data analyst",
        "machine learning engineer",
        "senior",
        "lead engineer"
    ]

    experience_score = 0

    # Experience section exists
    if "experience" in text:
        experience_score += 1

    # Professional job titles
    for title in experience_titles:

        if title in text:
            experience_score += 2

    # Multiple companies usually indicate experience
    company_keywords = [
        "private limited",
        "technologies",
        "solutions",
        "corporation",
        "pvt",
        "ltd"
    ]

    company_count = 0

    for word in company_keywords:

        company_count += text.count(word)

    if company_count >= 2:
        experience_score += 3

    # Employment duration like 2021-2024
    if re.search(r"20\d{2}\s*[-–]\s*(20\d{2}|present)", text):
        experience_score += 2

    # --------------------------------------------------
    # Fresher indicators
    # --------------------------------------------------

    fresher_score = 0

    fresher_keywords = [
        "intern",
        "internship",
        "training",
        "student",
        "bachelor",
        "university",
        "college",
        "cgpa",
        "academic project",
        "project"
    ]

    for word in fresher_keywords:

        if word in text:
            fresher_score += 1

    # --------------------------------------------------
    # Final Decision
    # --------------------------------------------------

    if fresher_score >= experience_score:
        return "Fresher"

    return "Experienced"
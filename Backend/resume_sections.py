import re

# ==========================================================
# SECTION HEADINGS
# ==========================================================

SECTION_PATTERNS = {

    "contact": [
        "contact"
    ],

    "summary": [
        "summary",
        "professional summary",
        "profile",
        "objective",
        "career objective",
        "about me"
    ],

    "skills": [
        "skills",
        "technical skills",
        "technical expertise",
        "core competencies",
        "competencies"
    ],

    "projects": [
        "projects",
        "project",
        "academic projects",
        "personal projects",
        "major projects",
        "project experience",
        "key projects",
        "technical projects"
    ],
    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "internship",
        "internships"
    ],

    "education": [
        "education",
        "academic qualifications",
        "qualifications",
        "academic background"
    ],

    "certifications": [
        "certifications",
        "certificates",
        "licenses"
    ],

    "achievements": [
        "achievements",
        "awards",
        "honors"
    ],

    "languages":[
        "spoken languages",
        "language proficiency",
        "known languages",
        "language skills"
    ]
    
}


# ==========================================================
# FIND SECTION
# ==========================================================

def has_section(text: str, keywords: list):

    text = text.lower()

    for keyword in keywords:

        pattern = r"\b" + re.escape(keyword.lower()) + r"\b"

        if re.search(pattern, text):
            return True

    return False


# ==========================================================
# DETECT ALL SECTIONS
# ==========================================================

def detect_sections(resume_text: str):

    detected = {}

    for section, keywords in SECTION_PATTERNS.items():

        detected[section] = has_section(
            resume_text,
            keywords
        )

    return detected


# ==========================================================
# SECTION ANALYSIS
# ==========================================================

def calculate_section_score(sections, candidate_type):

    # -------------------------
    # Essential sections
    # -------------------------

    if candidate_type == "Experienced":

        essential = [
            "summary",
            "skills",
            "experience",
            "education"
        ]

    else:

        essential = [
            "summary",
            "skills",
            "projects",
            "education"
        ]

    # Contact is always expected
    if sections.get("contact"):
        essential_present = ["Contact Information"]
    else:
        essential_present = []

    essential_missing = []

    mapping = {
        "summary": "Professional Summary",
        "skills": "Skills",
        "projects": "Projects",
        "experience": "Experience",
        "education": "Education"
    }

    for sec in essential:

        if sections.get(sec):
            essential_present.append(mapping[sec])
        else:
            essential_missing.append(mapping[sec])

    # -------------------------
    # Recommended sections
    # -------------------------

    recommended = [
        "certifications",
        "achievements",
        "languages"
    ]

    recommended_present = []
    recommended_missing = []

    mapping2 = {
        "certifications": "Certifications",
        "achievements": "Achievements",
        "languages": "Languages"
    }

    for sec in recommended:

        if sections.get(sec):
            recommended_present.append(mapping2[sec])
        else:
            recommended_missing.append(mapping2[sec])

    # -------------------------
    # Score
    # -------------------------

    total_essential = len(essential) + 1     # + Contact

    present_essential = len(essential_present)

    score = round(
        (present_essential / total_essential) * 100,
        2
    )

    return {

        "essential_present": essential_present,

        "essential_missing": essential_missing,

        "recommended_present": recommended_present,

        "recommended_missing": recommended_missing,

        "section_score": score

    }
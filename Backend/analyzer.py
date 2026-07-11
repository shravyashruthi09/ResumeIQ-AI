import re

from skills import SKILLS
from resume_sections import (
    detect_sections,
    calculate_section_score,
)
from candidate import detect_candidate_type
from resume_quality import analyze_resume_quality


# ==========================================================
# CLEAN TEXT
# ==========================================================

def clean_text(text: str):

    text = text.lower()
    text = re.sub(r"\s+", " ", text)

    return text


# ==========================================================
# EXTRACT SKILLS
# ==========================================================

def extract_skills(text: str):

    text = clean_text(text)

    found_skills = {}
    category_skills = {}

    for category, skills in SKILLS.items():

        category_skills[category] = []

        for skill in skills:

            skill_name = skill["name"]

            aliases = skill["aliases"]

            for alias in aliases:

                pattern = r"\b" + re.escape(alias.lower()) + r"\b"

                if re.search(pattern, text):

                    found_skills[skill_name] = category

                    category_skills[category].append(skill_name)

                    break

    return found_skills, category_skills


# ==========================================================
# MATCH LEVEL
# ==========================================================

def get_match_level(score):

    if score >= 90:
        return "Excellent"

    elif score >= 75:
        return "Good"

    elif score >= 60:
        return "Average"

    return "Poor"


# ==========================================================
# INTERVIEW PROBABILITY
# ==========================================================

def get_interview_probability(score):

    if score >= 95:
        return "Very High"

    elif score >= 80:
        return "High"

    elif score >= 65:
        return "Medium"

    elif score >= 50:
        return "Low"

    return "Very Low"


# ==========================================================
# HIRING CHANCE
# ==========================================================

def get_hiring_chance(score):

    if score >= 95:
        return "Excellent"

    elif score >= 80:
        return "Good"

    elif score >= 65:
        return "Average"

    return "Needs Improvement"

# ==========================================================
# SKILL GAP ANALYSIS
# ==========================================================

def classify_missing_skills(missing_skills):

    critical_categories = {

        "Programming Languages",
        "Backend",
        "Databases",
        "APIs & Authentication",
        "Cloud Computing",
        "DevOps",
        "Software Engineering",
        "Containers & Orchestration",
        "Artificial Intelligence",
        "Machine Learning Libraries",
        "Natural Language Processing",
        "Data Engineering",
        "Generative AI",
        "Vector Databases"

    }

    critical_missing = []
    nice_to_have_missing = []

    for skill in missing_skills:

        found = False

        for category, skills in SKILLS.items():

            for item in skills:

                if item["name"] == skill:

                    found = True

                    if category in critical_categories:
                        critical_missing.append(skill)
                    else:
                        nice_to_have_missing.append(skill)

                    break

            if found:
                break

    return critical_missing, nice_to_have_missing


# ==========================================================
# ANALYZE RESUME
# ==========================================================

def analyze_resume(resume_text: str, job_description: str):  
# ==========================================================
# Extract Skills
# ==========================================================

    resume_skills,resume_categories = extract_skills(resume_text)
    jd_skills, jd_categories = extract_skills(job_description)

    resume_set = set(resume_skills.keys())
    jd_set = set(jd_skills.keys())

    matched_skills = sorted(list(resume_set & jd_set))
    missing_skills = sorted(list(jd_set - resume_set))
    additional_skills = sorted(list(resume_set - jd_set))

    # ==========================================================
    # Candidate Type
    # ==========================================================

    candidate_type = detect_candidate_type(resume_text)

    # ==========================================================
    # Resume Sections
    # ==========================================================

    detected_sections = detect_sections(resume_text)

    resume_sections = calculate_section_score(
        detected_sections,
        candidate_type
    )

    section_score = resume_sections["section_score"]
    normalized_section_score = round((section_score / 100) * 10,2)

    # ==========================================================
    # Resume Quality
    # ==========================================================

    quality = analyze_resume_quality(resume_text)

    quality_score = quality["quality_score"]

    # ==========================================================
    # Category Scores
    # ==========================================================

    category_scores = {}

    for category, skills in jd_categories.items():

        if len(skills) == 0:
            continue

        matched = len(
            set(skills).intersection(resume_set)
        )

        category_scores[category] = round(
            (matched / len(skills)) * 100,
            2
        )

    # ==========================================================
    # ATS SCORE
    # ==========================================================

    total_jd_skills = len(jd_set)

    if total_jd_skills == 0:

        skills_score = 0

    else:

        skills_score = round(

            (len(matched_skills) / total_jd_skills) * 45,

            2

        )

    # ==========================================================
    # Projects Score
    # ==========================================================

    projects_score = 0
    if detected_sections.get("projects"):

        project_count = len(
            re.findall(
                r"\|\s*(Python|Java|SQL|ML|AI|FastAPI|Flask|React|Node)",
                resume_text,
                flags=re.IGNORECASE
            )
        )
        if candidate_type == "Fresher":
            
            if project_count >= 2:
                projects_score = 25
            else:
                projects_score = 20

        else:
            projects_score = 15
            
    # ==========================================================
    # Experience Score
    # ==========================================================

    experience_score = 0
    if detected_sections.get("experience"):
        if candidate_type == "Experienced":
            experience_score = 10
        else:
        # Fresher with internships
            experience_score = 8

    # ==========================================================
    # Education Score
    # ==========================================================

    education_score = 10 if detected_sections.get("education") else 0

    # ==========================================================
    # Final ATS Score
    # ==========================================================

    ats_score = round(

    skills_score
    + projects_score
    + experience_score
    + education_score
    + quality_score
    + normalized_section_score,

    2)

    ats_score = min(100, ats_score)

    # ==========================================================
    # SKILL GAP ANALYSIS
    # ==========================================================

    critical_missing, nice_to_have_missing = classify_missing_skills(
        missing_skills
    )

    if len(jd_set) == 0:

        matching_percentage = 0

    else:

        matching_percentage = round(

            (len(matched_skills) / len(jd_set)) * 100,

            2

        )

    skill_gap_analysis = {

        "critical_missing": critical_missing,

        "nice_to_have_missing": nice_to_have_missing,

        "matching_percentage": matching_percentage

    }

    # ==========================================================
    # Match Level
    # ==========================================================

    match_level = get_match_level(ats_score)
    # ==========================================================
    # SCORE BREAKDOWN
    # ==========================================================

    score_breakdown = {

    "Skills Match": round(skills_score, 2),

    "Projects": projects_score,

    "Experience": experience_score,

    "Education": education_score,

    "Resume Quality": quality_score,

    "Resume Sections": normalized_section_score

}

    # ==========================================================
    # RESUME STRENGTHS
    # ==========================================================


    resume_strengths = []

    # Strong programming foundation
    if category_scores.get("Programming Languages", 0) >= 80:
        resume_strengths.append(
            "Strong programming and software development fundamentals."
        )

    # Data Science
    if category_scores.get("Data Science", 0) >= 80:
        resume_strengths.append(
            "Hands-on experience in data analysis and machine learning."
        )

    # Artificial Intelligence
    if category_scores.get("Artificial Intelligence", 0) >= 80:
        resume_strengths.append(
            "Experience building AI and machine learning solutions."
        )

    # Backend
    if category_scores.get("Backend", 0) >= 80:
        resume_strengths.append(
            "Experience with backend development using modern frameworks."
        )

    # Resume Quality
    if quality_score >= 8:
        resume_strengths.append(
            "Well-structured resume with professional formatting."
        )

    # Essential Sections
    if not resume_sections["essential_missing"]:
        resume_strengths.append(
            "Includes all essential resume sections."
        )

    # Projects
    if candidate_type == "Fresher" and projects_score >= 20:
        resume_strengths.append(
            "Strong project portfolio demonstrating practical skills."
        )

    # Job Match
    if matching_percentage >= 70:
        resume_strengths.append(
            "Good alignment with the job requirements."
        )

    resume_strengths = resume_strengths[:5]
    
    # ==========================================================
    # RESUME WEAKNESSES
    # ==========================================================

    resume_weaknesses = []

    # Cloud Computing
    if category_scores.get("Cloud Computing", 100) < 40:
        resume_weaknesses.append(
            "Missing experience with cloud platforms such as AWS."
        )

    # Natural Language Processing
    if category_scores.get("Natural Language Processing", 100) < 40:
        resume_weaknesses.append(
            "Limited exposure to Natural Language Processing (NLP)."
        )

    # Computer Vision
    if category_scores.get("Computer Vision", 100) < 40:
        resume_weaknesses.append(
            "Limited exposure to Computer Vision."
        )

    # APIs
    if category_scores.get("APIs & Authentication", 100) < 40:
        resume_weaknesses.append(
            "API development and authentication experience could be strengthened."
        )

    # Soft Skills
    if category_scores.get("Soft Skills", 100) < 50:
        resume_weaknesses.append(
            "Soft skills such as analytical thinking and problem-solving could be highlighted better."
        )

    # Critical Skills
    if critical_missing:
        resume_weaknesses.append(
            "Some important technologies required by the job are not yet demonstrated."
        )

    # Resume Quality
    if quality_score < 8:
        resume_weaknesses.append(
            "Resume formatting and readability can be improved."
        )

    resume_weaknesses = resume_weaknesses[:5]

    # ==========================================================
    # RECOMMENDATIONS
    # ==========================================================
    recommendations = []

    # Missing critical skills
    if critical_missing:

        recommendations.append(

            "Learn or showcase experience with: "

            + ", ".join(critical_missing[:5])

        )

    # Nice-to-have skills
    if nice_to_have_missing:

        recommendations.append(

            "Consider adding: "

            + ", ".join(nice_to_have_missing[:4])

        )

    # Projects
    if candidate_type == "Fresher" and projects_score < 25:

        recommendations.append(

            "Include 2–3 end-to-end projects demonstrating real-world problem solving."

        )

    # Certifications
    if "Certifications" in resume_sections["recommended_missing"]:

        recommendations.append(

            "Add relevant certifications to strengthen credibility."

        )

    # ATS optimization
    if matching_percentage < 80:

        recommendations.append(

            "Tailor your resume keywords to match the job description."

        )

    # Resume quality
    if quality_score < 8:

        recommendations.append(

            "Improve formatting, readability, and quantify achievements."

        )

    recommendations = recommendations[:5]
    
    # ==========================================================
    # INTERVIEW PROBABILITY
    # ==========================================================

    interview_probability = get_interview_probability(
        ats_score
    )

    # ==========================================================
    # HIRING CHANCE
    # ==========================================================

    hiring_chance = get_hiring_chance(
        ats_score
    )

    # ==========================================================
    # STRONGEST & WEAKEST CATEGORY
    # ==========================================================

    if category_scores:

        strongest_area = max(
            category_scores,
            key=category_scores.get
        )

        weakest_area = min(
            category_scores,
            key=category_scores.get
        )

    else:

        strongest_area = "N/A"
        weakest_area = "N/A"

    # ==========================================================
    # RESUME SUMMARY
    # ==========================================================

    resume_summary = {

        "overall_rating": f"{round(ats_score / 10, 1)}/10",

        "candidate_type": candidate_type,

        "ready_for_application": ats_score >= 75,

        "strongest_area": strongest_area,

        "weakest_area": weakest_area,

        "top_missing_skill":
            missing_skills[0] if missing_skills else "None"

    }


    # ==========================================================
    # RETURN RESPONSE
    # ==========================================================

    return {

        # Overall
        "ats_score": ats_score,
        "candidate_type": candidate_type,
        "match_level": match_level,

        # ATS Breakdown
        "score_breakdown": score_breakdown,

        # Skills
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "additional_skills_count": len(additional_skills),
        "additional_skills": additional_skills[:7],

        # Categories
        "category_scores": category_scores,

        # Skill Gap
        "skill_gap_analysis": skill_gap_analysis,

        # Resume Sections
        "resume_sections": resume_sections,

        # Resume Quality
        "resume_quality": quality,

        # Analysis
        "resume_strengths": resume_strengths,
        "resume_weaknesses": resume_weaknesses,

        # Suggestions
        "recommendations": recommendations,

        # Hiring Prediction
        "interview_probability": interview_probability,
        "hiring_chance": hiring_chance,

        # Summary
        "resume_summary": resume_summary

    }

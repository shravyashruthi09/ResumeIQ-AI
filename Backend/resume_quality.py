import re


# ==========================================================
# EMAIL
# ==========================================================

def has_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    return bool(re.search(pattern, text))


# ==========================================================
# PHONE
# ==========================================================

def has_phone(text):

    pattern = r"(\+?\d[\d\s\-]{8,15})"

    return bool(re.search(pattern, text))


# ==========================================================
# LINKEDIN
# ==========================================================

def has_linkedin(text):

    return "linkedin" in text.lower()


# ==========================================================
# GITHUB
# ==========================================================

def has_github(text):

    return "github" in text.lower()


# ==========================================================
# ACTION VERBS
# ==========================================================

ACTION_VERBS = [

    "developed",
    "designed",
    "implemented",
    "created",
    "built",
    "optimized",
    "improved",
    "managed",
    "led",
    "analyzed",
    "automated",
    "deployed",
    "engineered",
    "integrated",
    "maintained",
    "tested",
    "debugged",
    "configured",
    "collaborated",
    "delivered"

]


def count_action_verbs(text):

    text = text.lower()

    count = 0

    for verb in ACTION_VERBS:

        count += text.count(verb)

    return count


# ==========================================================
# QUANTIFIED ACHIEVEMENTS
# ==========================================================

def count_numbers(text):

    pattern = r"\b\d+%?|\b\d+\+"

    return len(re.findall(pattern, text))


# ==========================================================
# BULLET POINTS
# ==========================================================

def count_bullets(text):

    bullets = ["•", "-", "*"]

    count = 0

    for bullet in bullets:

        count += text.count(bullet)

    return count


# ==========================================================
# WORD COUNT
# ==========================================================

def word_count(text):

    return len(text.split())


# ==========================================================
# QUALITY SCORE
# ==========================================================

def analyze_resume_quality(text):

    score = 0

    quality = {}

    quality["email"] = has_email(text)

    quality["phone"] = has_phone(text)

    quality["linkedin"] = has_linkedin(text)

    quality["github"] = has_github(text)

    quality["action_verbs"] = count_action_verbs(text)

    quality["numbers"] = count_numbers(text)

    quality["bullets"] = count_bullets(text)

    quality["word_count"] = word_count(text)

    # ------------------------------------
    # CONTACT
    # ------------------------------------

    if quality["email"]:
        score += 1

    if quality["phone"]:
        score += 1

    if quality["linkedin"]:
        score += 1

    if quality["github"]:
        score += 1

    # ------------------------------------
    # ACTION VERBS
    # ------------------------------------

    if quality["action_verbs"] >= 10:
        score += 2

    elif quality["action_verbs"] >= 5:
        score += 1

    # ------------------------------------
    # QUANTIFIED ACHIEVEMENTS
    # ------------------------------------

    if quality["numbers"] >= 5:
        score += 2

    elif quality["numbers"] >= 2:
        score += 1

    # ------------------------------------
    # BULLET POINTS
    # ------------------------------------

    if quality["bullets"] >= 10:
        score += 2

    elif quality["bullets"] >= 5:
        score += 1

    # ------------------------------------
    # WORD COUNT
    # ------------------------------------

    if 350 <= quality["word_count"] <= 700:
        score += 1

    score = min(score, 10)

    quality["quality_score"] = score

    return quality
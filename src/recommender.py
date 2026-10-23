
def calculate_similarity(user_skills, required_skills):
    """Calculate the percentage of required skills matched."""

    user_set = {
        skill.strip().lower()
        for skill in user_skills
        if skill.strip()
    }

    required_set = {
        skill.strip().lower()
        for skill in required_skills
        if skill.strip()
    }

    if not required_set:
        return 0.0

    matched_skills = user_set.intersection(required_set)

    score = len(matched_skills) / len(required_set) * 100

    return round(score, 2)


def recommend_jobs(user_skills, jobs):
    """Rank job profiles according to the user's skill match."""

    recommendations = []

    normalized_user_skills = {
        skill.strip().lower()
        for skill in user_skills
        if skill.strip()
    }

    for job in jobs:
        required_skills = job["skills"]

        matched_skills = [
            skill
            for skill in required_skills
            if skill.strip().lower() in normalized_user_skills
        ]

        missing_skills = [
            skill
            for skill in required_skills
            if skill.strip().lower() not in normalized_user_skills
        ]

        score = calculate_similarity(
            user_skills,
            required_skills
        )

        recommendations.append({
            "title": job["title"],
            "description": job["description"],
            "score": score,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        })

    recommendations.sort(
        key=lambda job: job["score"],
        reverse=True
    )

    return recommendations

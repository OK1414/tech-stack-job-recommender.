
from src.recommender import calculate_similarity, recommend_jobs


def test_similarity():
    user_skills = ["Python", "SQL", "Node.js"]
    required_skills = [
        "Python", "SQL", "Node.js", "Express", "REST API", "Git"
    ]

    score = calculate_similarity(user_skills, required_skills)

    assert score == 50.0


def test_recommend_jobs():
    jobs = [
        {
            "title": "Backend Developer",
            "description": "Builds APIs",
            "skills": ["Python", "SQL", "Node.js"]
        },
        {
            "title": "Data Analyst",
            "description": "Analyzes data",
            "skills": ["Excel", "Power BI"]
        }
    ]

    results = recommend_jobs(["Python", "SQL"], jobs)

    assert results[0]["title"] == "Backend Developer"
    assert results[0]["score"] == 66.67
    assert len(results) == 2


if __name__ == "__main__":
    test_similarity()
    test_recommend_jobs()
    print("All recommendation tests passed!")

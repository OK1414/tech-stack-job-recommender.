import json
from pathlib import Path

from flask import Flask, render_template, request
from src.recommender import recommend_jobs

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "jobs.json"


def load_jobs():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    user_skills = ""

    if request.method == "POST":
        user_skills = request.form.get("skills", "")

        skills_list = [
            skill.strip()
            for skill in user_skills.split(",")
            if skill.strip()
        ]

        if skills_list:
            jobs = load_jobs()
            recommendations = recommend_jobs(skills_list, jobs)

    return render_template(
        "index.html",
        recommendations=recommendations,
        user_skills=user_skills
    )


if __name__ == "__main__":
    app.run(debug=True)
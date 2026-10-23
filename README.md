# TechPath — Tech Stack & Job Profile Recommendation System

TechPath is a web-based recommendation system that helps users explore suitable technology job profiles based on their existing technical skills. It compares user-provided skills with sample job profiles and ranks the results by skill-match percentage.

## Features

- **Skill-based recommendations:** Recommends job profiles based on the user's technical skills.
- **Match percentage:** Calculates the percentage of required skills matched for each profile.
- **Matching skills:** Highlights skills the user already knows.
- **Skills to learn:** Identifies skills that are missing from each profile.
- **Interactive interface:** Includes clickable skill suggestions, duplicate-skill handling, input validation, and loading feedback.
- **Responsive design:** Provides a clean interface for desktop and mobile screens.
- **Automated tests:** Tests the recommendation algorithm and ranking logic.

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Data storage:** JSON
- **Testing:** Python test scripts
- **Development tools:** VS Code, Git, GitHub

## Project Structure

```text
tech-stack-job-recommender/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── jobs.json
├── src/
│   ├── __init__.py
│   └── recommender.py
├── static/
│   ├── script.js
│   └── style.css
├── templates/
│   └── index.html
└── tests/
    ├── __init__.py
    └── test_recommender.py
```

## How It Works

1. The user enters technical skills such as Python, SQL, or Node.js.
2. The Flask backend receives the submitted skills.
3. The recommendation module compares the user's skills with each job profile.
4. A match score is calculated using the number of matching skills divided by the number of required skills.
5. Job profiles are sorted from the highest match percentage to the lowest.
6. The interface displays match percentages, matching skills, and skills the user could learn next.

### Match Formula

**Match Percentage = (Number of Matching Skills / Total Required Skills) × 100**

The system uses case-insensitive skill matching and sorts recommendations by score.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/OK1414/tech-stack-job-recommender..git
cd tech-stack-job-recommender
```


### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

### 5. Run the tests

Open a second terminal at the project root and run:

```bash
python -m tests.test_recommender
```

Expected output:

```text
All recommendation tests passed!
```

## Example Input

```text
Python, SQL, Node.js
```

The application ranks the sample profiles, such as Backend Developer, Python Developer, Data Analyst, and Full Stack Developer, according to their matching skills.

## Future Improvements

- Expand the job-profile dataset with more technology roles.
- Add user accounts and saved preferences.
- Improve skill matching with synonyms and semantic similarity.
- Allow administrators to manage job profiles.
- Integrate verified job listings from an appropriate data source.
- Deploy the application online.

## Important Note

The application currently uses sample job profiles stored in a JSON file. Match percentages indicate skill overlap with these profiles; they are not real-time vacancy matches and do not guarantee job eligibility or employment.

## Author

Developed as a project to practise Python, Flask, frontend development, testing, and recommendation-system fundamentals.

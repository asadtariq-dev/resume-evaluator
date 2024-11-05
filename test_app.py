import os
import tempfile
import pytest
from flask import Flask
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["UPLOAD_FOLDER"] = tempfile.gettempdir()
    with app.test_client() as client:
        yield client

# Test index page rendering
def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Resume Evaluator" in response.data

# Test file upload and resume evaluation (using a temporary file)
def test_evaluate_resume(client):
    job_description = "We are looking for a team player with strong communication skills."

    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_resume:
        temp_resume.write(b"This is a test resume content.")
        temp_resume_path = temp_resume.name

    with open(temp_resume_path, "rb") as resume_file:
        data = {
            "job_description": job_description,
            "resume": (resume_file, "test_resume.docx")
        }

        response = client.post("/", data=data, content_type="multipart/form-data")

    assert response.status_code == 200


# Test invalid file upload (using a temporary file)
def test_invalid_file_type(client):
    job_description = "We need a quick thinker with problem solving skills."

    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_invalid_file:
        temp_invalid_file.write(b"This is an invalid file content.")
        temp_invalid_file_path = temp_invalid_file.name

    with open(temp_invalid_file_path, "rb") as invalid_file:
        data = {
            "job_description": job_description,
            "resume": (invalid_file, "invalid_file.txt")
        }

        response = client.post("/", data=data, content_type="multipart/form-data")

    assert response.status_code == 200
    assert b"Please provide job description." in response.data

    os.remove(temp_invalid_file_path)

def test_generate_evaluation_summary():
    from utils.evaluator import generate_evaluation_summary

    summary_insights, conclusion = generate_evaluation_summary(20)
    assert summary_insights[0] == "The candidate does not meet the foundational requirements for the role."
    assert conclusion == "The evaluation suggests that the candidate does not possess the requisite skills and qualities needed for the role."

def test_extract_skills_from_text():
    from utils.evaluator import extract_skills_from_text

    text = "Python Java team player strong communication"
    skills = extract_skills_from_text(text)
    assert "Python" in skills
    assert "Java" in skills
    assert "team" in skills
    assert "player" in skills
    assert len(skills) > 0

@pytest.fixture(autouse=True)
def cleanup():
    yield

if __name__ == "__main__":
    pytest.main()

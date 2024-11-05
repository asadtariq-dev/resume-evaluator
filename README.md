Resume Evaluation App
=====================

This Resume Evaluation App allows users to upload a resume file and input a job description to evaluate the candidate's suitability for a specified role. Using NLP, the app extracts and compares skills, calculates a fitness score, and provides insights into the candidate's alignment with the job's requirements.

Features
--------

-   **File Upload:** Accepts resumes in `.pdf` and `.docx` formats.
-   **Text Parsing:** Extracts skills and keywords from both the resume and job description.
-   **Evaluation Metrics:**
    -   **Core Skills Match** -- Compares skills in the resume against job requirements.
    -   **Exceptional Qualities** -- Identifies standout attributes beneficial for the role.
    -   **Overall Fitness Score** -- Summarizes the candidate's suitability with a score and descriptive insights.
-   **Summary and Conclusion** -- Provides insights based on the candidate's score.

Installation
------------

To get started with this project, clone the repository and follow these instructions.

### Prerequisites

-   Python 3.8+
-   `spacy` and `en_core_web_sm` model
-   Flask

### Install Dependencies

1.  Clone the repository:

    `git clone repo-here
    cd resume-evaluation-app`

2.  Install required Python packages:

    `pip install -r requirements.txt`

3.  Download the `en_core_web_sm` model for spaCy:

    `python -m spacy download en_core_web_sm`

### Configuration

Ensure you have an `uploads/` directory in the root of your project for temporary file storage.

`mkdir uploads`

Usage
-----

1.  **Run the App:**

    `python app.py`

2.  **Navigate to the Web Interface:** Open your browser and go to `http://127.0.0.1:5001` to access the application.

3.  **Evaluate a Resume:**

    -   Upload a resume in `.pdf` or `.docx` format.
    -   Enter the job description in plain text or markdown format.
    -   Click **Evaluate** to view the results.

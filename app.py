from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

from utils.parser import extract_text_from_pdf, extract_text_from_docx, parse_markdown_to_text
from utils.evaluator import evaluate_resume, generate_evaluation_summary

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

ALLOWED_EXTENSIONS = {"pdf", "docx"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        job_description = request.form["job_description"]
        resume_file = request.files["resume"]

        if resume_file and allowed_file(resume_file.filename):
            filename = secure_filename(resume_file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            resume_file.save(file_path)

            try:
                if filename.endswith(".pdf"):
                    resume_text = extract_text_from_pdf(file_path)
                else:
                    resume_text = extract_text_from_docx(file_path)

                job_text = parse_markdown_to_text(job_description)

                result = evaluate_resume(resume_text, job_text)
                os.remove(file_path)

                summary_insights, conclusion = generate_evaluation_summary(result['overall_fitness_score'])

                return render_template(
                    "result.html",
                    result=result,
                    summary_insights=summary_insights,
                    conclusion=conclusion
                )
            except Exception as e:
                return render_template("index.html", error="An error occurred while processing your resume.")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

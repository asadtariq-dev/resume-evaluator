import re

def extract_skills_from_text(text):
    # Use a simple regex to find potential skills (e.g., nouns or proper nouns)
    skills_keywords = set(re.findall(r'\b[A-Z][a-z]*\b|\b[a-z]{3,}\b', text))

    return list(skills_keywords)

def evaluate_resume(resume_text, job_text):
    required_skills = extract_skills_from_text(job_text)
    resume_skills = extract_skills_from_text(resume_text)

    base_score = 0
    exceptional_score = 0

    matched_skills = set(resume_skills).intersection(set(required_skills))
    base_score = len(matched_skills) / len(required_skills) * 100 if required_skills else 0

    exceptional_skills = [
        "team player", "strong communication", "problem solving",
        "motivated", "lead", "mentor", "advanced", "expert",
        "senior", "architecture", "design", "performance",
        "optimization"
    ]

    matched_exceptional_skills = 0
    for skill in exceptional_skills:
        if skill in resume_text.lower():
            exceptional_score += 10
            matched_exceptional_skills += 1


    exceptional_score = matched_exceptional_skills / len(exceptional_skills) * 100 if len(exceptional_skills) else 0

    overall_fitness_score = base_score + exceptional_score

    return {
        "matched_skills": list(matched_skills),
        "required_skills": required_skills,
        "exceptional_skills": exceptional_score,
        "base_score": base_score,
        "exceptional_score": exceptional_score,
        "overall_fitness_score": overall_fitness_score,
    }

def generate_evaluation_summary(overall_fitness_score):
    if overall_fitness_score <= 25:
        summary_insights = [
            "The candidate does not meet the foundational requirements for the role.",
            "Consideration of additional training or experience may be necessary for them to align with the job expectations."
        ]
        conclusion = "The evaluation suggests that the candidate does not possess the requisite skills and qualities needed for the role."
    elif overall_fitness_score < 50:
        summary_insights = [
            "The candidate demonstrates a limited level of essential skills relevant to the job.",
            "Further evaluation of their qualifications may be needed before proceeding."
        ]
        conclusion = "Further evaluation may be needed to confirm the candidate's suitability."
    elif overall_fitness_score < 75:
        summary_insights = [
            "The candidate exhibits some strong capabilities but may require additional development in specific areas.",
            "Exceptional qualities have been identified that could enhance their performance."
        ]
        conclusion = "The candidate's skills and exceptional qualities indicate potential for growth in this role."
    else:
        summary_insights = [
            "The candidate exhibits strong capabilities, aligning well with the job requirements.",
            "They possess remarkable skills that make them a valuable addition to the team."
        ]
        conclusion = "The candidate's skills and strengths make them a highly suitable fit for the role."

    return summary_insights, conclusion

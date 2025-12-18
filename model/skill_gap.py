def analyze_skill_gap(resume_text, required_skills):
    present = []
    missing = []

    resume_text = resume_text.lower()

    for skill in required_skills:
        if skill.lower() in resume_text:
            present.append(skill)
        else:
            missing.append(skill)

    return present, missing

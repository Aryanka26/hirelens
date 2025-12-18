from utils.text_extractor import extract_text_from_pdf, clean_text
from model.matcher import calculate_match_score
from model.skill_gap import analyze_skill_gap
from model.skills import ROLE_SKILLS

# Load resume
resume_text = extract_text_from_pdf("data/sample_resume.pdf")
resume_text = clean_text(resume_text)

# Load job description
with open("data/job_descriptions/sde_intern.txt", "r") as f:
    job_text = f.read()

job_text = clean_text(job_text)

# Match score
score = calculate_match_score(resume_text, job_text)

# Skill gap
present, missing = analyze_skill_gap(
    resume_text,
    ROLE_SKILLS["sde_intern"]
)

print(f"Resume–Job Match Score: {score}%")
print("\nPresent Skills:", present)
print("Missing Skills:", missing)

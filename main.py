from parsers.resume_parser import parse_resume
from ats_engine.ats_scorer import calculate_score

resume = "Python Developer with Django experience"

parsed = parse_resume(resume)
score = calculate_score(parsed["skills"], ["Python", "Django"])

print("ATS Score:", score)

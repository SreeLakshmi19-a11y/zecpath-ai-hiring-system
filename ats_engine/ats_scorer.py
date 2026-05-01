def calculate_score(candidate_skills, job_skills):
    match = set(candidate_skills).intersection(set(job_skills))
    return len(match) / len(job_skills) * 100

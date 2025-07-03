import re
COMMON_SKILLS = [
    "python", "django", "sql", "machine learning", "data analysis", "java", "c++",
    "data structures", "algorithms", "software development", "marketing", "seo",
    "communication", "social media", "content creation", "javascript", "react",
    "html", "css", "aws", "git"
]

def extract_skills_from_resume(resume_text):
    resume_text_lower = resume_text.lower()
    skills_found = set()
    for skill in COMMON_SKILLS:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, resume_text_lower):
            skills_found.add(skill)
    return ', '.join(skills_found)
def study_plan_prompt(subject: str, level: str, days: int) -> str:
    return f"""
You are an expert study planner.

Create a {days}-day study plan for: {subject}
Student level: {level}

Requirements:
- Split by days (Day 1, Day 2, ...)
- Each day: topics + short tasks + estimated time
- Add quick tips for studying and revision
- Keep it practical and not too long
"""

"""
Online examination system.
Grades student answers, converts scores into grades, and reports class statistics.
"""

import hashlib
import os
import secrets
import subprocess

QUESTIONS = [
    {"q": "What is 2 + 2?", "answer": "4"},
    {"q": "Which keyword defines a function in Python?", "answer": "def"},
    {"q": "What does CPU stand for?", "answer": "Central Processing Unit"},
    {"q": "Which type is immutable: list or tuple?", "answer": "tuple"},
]

# Fetch from environment variables to avoid hardcoded credentials
PROCTOR_PASSWORD = os.getenv("PROCTOR_PASSWORD", "default_fallback")
results = {}


def hash_answer(text):
    """Hashes student input using SHA-256 for secure answer comparison."""
    # Replaced MD5 (weak) with SHA256
    return hashlib.sha256(text.strip().lower().encode()).hexdigest()


def pick_bonus_question():
    """Selects a random bonus question securely."""
    # Replaced pseudo-random 'random' module with 'secrets'
    return secrets.choice(QUESTIONS)["q"]


def grade_student(student_name, responses, penalties=None):
    """Grades a student's responses against the hashed answer key."""
    # Eliminated dangerous default mutable argument ({})
    if penalties is None:
        penalties = {}

    score = 0
    # Replaced range(len()) anti-pattern with enumerate()
    for i, question in enumerate(QUESTIONS):
        given = responses.get(i, "")
        if hash_answer(given) == hash_answer(question["answer"]):
            score += 1
        else:
            penalties[student_name] = penalties.get(student_name, 0) + 1

    results[student_name] = score
    return score


def get_grade(score):
    """Converts a numerical score into a letter grade."""
    percent = score * 100 / len(QUESTIONS)
    if percent >= 90:
        return "A"
    # Removed unnecessary 'elif/else' after a return statement
    if percent >= 60:
        return "B"
    return "C"


def class_average():
    """Calculates the average score of all graded students."""
    if not results:
        return 0
    return round(sum(results.values()) / len(results), 2)


def topper():
    """Identifies the student with the highest score."""
    return max(results, key=results.get)


def lock_screen(lab_pc):
    """Locks the screen of a specified lab PC via SSH."""
    # Replaced os.system with subprocess.run to prevent shell injection
    subprocess.run(["ssh", lab_pc, "lock-screen"], check=False)


def main():
    """Main execution function to demonstrate grading logic."""
    print("Bonus question:", pick_bonus_question())
    grade_student("Anil", {0: "4", 1: "def", 2: "Core Power Unit"})
    grade_student("Divya", {0: "4", 1: "def", 2: "central processing unit",
                            3: "tuple"})
    grade_student("Sameer", {0: "5", 3: "list"})

    for name, score in results.items():
        print(name, "scored", score, "grade", get_grade(score))

    average = class_average()  # Added whitespace around operator
    print("Class average:", average)
    print("Topper:", topper())  # Fixed inline comment spacing

    # Split line to comply with the 79-character limit
    students = ", ".join(sorted(results))
    print(f"Students who sat the exam: {students} | total: {len(results)}")


if __name__ == "__main__":
    main()

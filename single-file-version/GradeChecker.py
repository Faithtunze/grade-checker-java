# ============================================================
# Grade Checker Program - Single File with Functions
# ============================================================

def get_student_name():
    """Prompt the user to enter the student's name."""
    name = input("Enter student name: ").strip()
    return name


def get_score():
    """Prompt the user to enter a score and validate it."""
    while True:
        try:
            score = float(input("Enter score (0 - 100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("  Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("  Invalid input. Please enter a numeric value.")


def calculate_grade(score):
    """Determine the letter grade based on the score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def get_remark(grade):
    """Return a remark based on the letter grade."""
    remarks = {
        "A": "Excellent! Outstanding performance.",
        "B": "Good job! Above average performance.",
        "C": "Fair. Average performance.",
        "D": "Poor. Below average — needs improvement.",
        "F": "Failing. Significant improvement required.",
    }
    return remarks[grade]


def display_result(name, score, grade, remark):
    """Display the student's result in a formatted report."""
    print("\n" + "=" * 45)
    print("           GRADE REPORT")
    print("=" * 45)
    print(f"  Student Name : {name}")
    print(f"  Score        : {score:.1f}")
    print(f"  Grade        : {grade}")
    print(f"  Remark       : {remark}")
    print("=" * 45)


def ask_continue():
    """Ask the user if they want to check another grade."""
    answer = input("\nCheck another student? (yes/no): ").strip().lower()
    return answer in ("yes", "y")


def main():
    """Main function — orchestrates the grade checker."""
    print("=" * 45)
    print("      STUDENT GRADE CHECKER")
    print("=" * 45)

    while True:
        name  = get_student_name()
        score = get_score()
        grade = calculate_grade(score)
        remark = get_remark(grade)
        display_result(name, score, grade, remark)

        if not ask_continue():
            print("\nGoodbye!\n")
            break


if __name__ == "__main__":
    main()

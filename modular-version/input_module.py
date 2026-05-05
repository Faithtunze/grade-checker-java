def get_student_name():
    name = input("Enter student name: ").strip()
    return name


def get_score():
    while True:
        try:
            score = float(input("Enter score (0 - 100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("  Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("  Invalid input. Please enter a numeric value.")


def ask_continue():
    answer = input("\nCheck another student? (yes/no): ").strip().lower()
    return answer in ("yes", "y")

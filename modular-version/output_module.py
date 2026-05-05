def display_result(name, score, grade, remark):
    print("\n" + "=" * 45)
    print("           GRADE REPORT")
    print("=" * 45)
    print(f"  Student Name : {name}")
    print(f"  Score        : {score:.1f}")
    print(f"  Grade        : {grade}")
    print(f"  Remark       : {remark}")
    print("=" * 45)


def display_header():
    print("=" * 45)
    print("      STUDENT GRADE CHECKER")
    print("=" * 45)


def display_goodbye():
    print("\nGoodbye!\n")

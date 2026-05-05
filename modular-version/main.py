import input_module
import logic_module
import output_module


def main():
    output_module.display_header()

    while True:
        name  = input_module.get_student_name()
        score = input_module.get_score()

        grade  = logic_module.calculate_grade(score)
        remark = logic_module.get_remark(grade)

        output_module.display_result(name, score, grade, remark)

        if not input_module.ask_continue():
            output_module.display_goodbye()
            break


if __name__ == "__main__":
    main()

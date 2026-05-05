def calculate_grade(score):
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
    remarks = {
        "A": "Excellent! Outstanding performance.",
        "B": "Good job! Above average performance.",
        "C": "Fair. Average performance.",
        "D": "Poor. Below average — needs improvement.",
        "F": "Failing. Significant improvement required.",
    }
    return remarks[grade]

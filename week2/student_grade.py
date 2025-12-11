def get_grade(name, scores):

    score = scores.get(name, "Student not found")
    if score.isdigit():
        score = int(score)
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
    else:
        return score


def main():
    scores = {"Alice": "95", "Bob": "82", "Charlie": "67", "David": "74", "Eve": "58"}
    name = input("Enter student name: ").title()
    grade = get_grade(scores=scores, name=name)
    print(f"{name}'s grade: {grade}")


if __name__ == "__main__":
    main()

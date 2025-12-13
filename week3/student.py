class Student:
    def __init__(self, mark):
        self.mark = mark
        self.set_grade()

    def set_grade(self):
        if self.mark > 100 or self.mark < 0:
            print("Invalid mark input")
            self.__grade = None
        elif self.mark >= 90:
            self.__grade = "A+"
        elif self.mark >= 80:
            self.__grade = "A"
        elif self.mark >= 70:
            self.__grade = "B"
        elif self.mark >= 60:
            self.__grade = "C"
        elif self.__grade >= 40:
            self.__grade = "D"
        elif 0 <= self.mark < 40:
            self.__grade = "F"

    def get_grade(self):
        return self.__grade


def main():
    student = Student(87)
    print("Your grade is", student.get_grade())


if __name__ == "__main__":
    main()

class Employee:
    def __init__(self, name):
        self.name = name
        self.__salary = 0

    def set_salary(self, value):
        self.__salary = value

    def get_salary(self):
        return self.__salary

    def annual_salary(self):
        return self.get_salary() * 12


def main():
    employee = Employee("John")
    employee.set_salary(value=5000)
    print("Employee name: ", employee.name)
    print(f"Employee salary: {employee.get_salary()}")
    print(f"Employees annual salary: {employee.annual_salary()}")


if __name__ == "__main__":
    main()

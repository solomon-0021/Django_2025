from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary():
        pass


class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary
    


def main():
    emp = FullTimeEmployee(400)
    print(f"Salary: {emp.calculate_salary()}")

if __name__ == "__main__":
    main()

from  datetime import datetime

def calculate_birth_year(current_year, age):
    """ "Given the current year and a person's age,
    calculate their birth year."""
    birth_year = current_year - age

    return birth_year


def main():
    age = int(input("Enter your age: "))
    current_year = datetime.now().year
    birth_year = calculate_birth_year(current_year, age)
    print(f"You were born in {birth_year}.")

if __name__ == "__main__":
    main()



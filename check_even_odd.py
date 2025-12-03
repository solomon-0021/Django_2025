def check_even_odd(number):
    """Check if a given number is even or odd."""
    if number % 2 == 0:
        return "Even"
    return "Odd"


def main():
    number = int(input("Enter a number: "))
    result = check_even_odd(number)
    print(f"The number {number} is {result}.")

if __name__ == "__main__":
    main()

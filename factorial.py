def factorial(n):
    """Calculate the factorial of a given number n."""
    if n < 0:
        raise ValueError("Your number must be non-negative.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    number = int(input("Enter a number to calculate its factorial: "))
    try:
        result = factorial(number)
        print(f"The factorial of {number} is {result}.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

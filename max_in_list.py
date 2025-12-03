def max_in_list(numbers):
    """Return the maximum number in a list of numbers."""
    if not numbers:
        raise ValueError("The list cannot be empty.")
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number


def main():
    numbers = [2, 10, 5, 8, 3]
    try:
        result = max_in_list(numbers)
        print(f"The maximum number in the list is {result}.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

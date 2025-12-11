def check_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]


def main():
    number = int(input("Enter a number to check if it's a palindrome: "))
    if check_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")


if __name__ == "__main__":
    main()

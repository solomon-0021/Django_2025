def fizz_buzz(n):

    answer = []
    # first check for divisibility by 3 and 5
    # then as you want
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer


def main():
    num = int(input("Enter a number: "))
    result = fizz_buzz(num)
    print(result)


if __name__ == "__main__":
    main()

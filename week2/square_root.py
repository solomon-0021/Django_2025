def square_root(num):
    if num < 0:
        return None

    left, right = 0, num

    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared == num:
            return mid
        elif mid_squared < num:
            left = mid + 1
        else:
            right = mid - 1

    return right


def main():
    num = int(input("Enter a non-negative integer: "))
    result = square_root(num)
    if result is not None:
        print(f"The integer square root of {num} is {result}.")
    else:
        print("Please enter a non-negative integer.")


if __name__ == "__main__":
    main()

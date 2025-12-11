def move_zeros(nums):
    """Move all zeros to the end of the list
    while maintaining the order of non-zero
    elements."""
    n = len(nums)

    for i in range(n - 1):
        if nums[i] == 0:
            for j in range(i, n):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
    return nums


def main():
    nums = [0, 1, 0, 3, 12]
    print("Original list:", nums)
    result = move_zeros(nums)
    print("List after moving zeros:", result)


if __name__ == "__main__":
    main()

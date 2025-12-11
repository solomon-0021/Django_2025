def two_sum(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in nums_map:
            return [nums_map[diff], i]
        else:
            nums_map[num] = i

    return []  # if not found

def main():
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices of numbers that add up to {target}: {result}")


if __name__ == "__main__":
    main()
    
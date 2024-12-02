# Day 2 link: https://adventofcode.com/2024/day/2

safe = 0
max_dif = 3
min_dif = 1


def is_safe(nums: list) -> bool:
    return all(0 < nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1)) or all(
        -3 <= nums[i + 1] - nums[i] < 0 for i in range(len(nums) - 1)
    )


assert is_safe([7, 6, 4, 2, 1])
assert not is_safe([1, 2, 7, 8, 9])
assert not is_safe([9, 7, 6, 2, 1])
assert not is_safe([1, 3, 2, 4, 5])
assert not is_safe([8, 6, 4, 4, 1])
assert is_safe([1, 3, 6, 7, 9])


with open("input.txt", "r") as f:
    for line in f:
        nums = list(map(int, line.strip().split()))
        if is_safe(nums):
            safe += 1

print(safe)

safe_2 = 0

with open("input.txt", "r") as f:
    for line in f:
        nums = list(map(int, line.strip().split()))
        if any(is_safe(nums[:i] + nums[i + 1 :]) for i in range(len(nums) + 1)):
            safe_2 += 1

print(safe_2)

"""
Warmup: Two Sum
Date: 2026-07-20
Difficulty: Easy
Pattern: Hash Map

Task:
Given an integer array nums and an integer target, return the indices of the
two numbers that add up to target.

Assumptions:
- Each input has exactly one answer.
- The same element cannot be used twice.

Practice goals:
- Store number -> index in a dictionary.
- Check complement before storing the current number.
- Avoid reusing the same element.
- Return indices from the original array.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    # Write your solution here.
    seen: dict[int, int] = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def test_two_sum() -> None:
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 5, 3, 7, 9, 2], 10) == [2, 3]


if __name__ == "__main__":
    test_two_sum()
    print("All tests passed.")

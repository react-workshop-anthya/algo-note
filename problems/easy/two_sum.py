"""
Problem: Two Sum
Difficulty: Easy
Pattern: Hash Map

Summary:
Given an integer array nums and an integer target, return the indices of the two
numbers that add up to target. Each input has exactly one answer, and the same
element cannot be used twice.

Brute Force:
Check every pair of indices and return the pair whose values sum to target.

Optimized Approach:
Scan nums once while storing previously seen numbers in a hash map:
number -> index. For each number, check whether target - number was seen before.

Time Complexity: O(n)
Space Complexity: O(n)

Edge Cases:
- The answer uses the first two elements.
- Duplicate values can form the answer, such as [3, 3] with target 6.
- The complement may appear after the current number, so store only after
  checking the current complement.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
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

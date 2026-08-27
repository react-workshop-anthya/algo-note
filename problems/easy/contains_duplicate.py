"""
Problem: Contains Duplicate
Difficulty: Easy
Pattern: Hash Set

Summary:
Given an integer array nums, return True if any value appears at least twice.
Return False if every element is distinct.

Brute Force:
Compare every pair of elements. If any pair has the same value, return True.

Optimized Approach:
Scan nums once while storing previously seen values in a set. If the current
number already exists in the set, a duplicate was found.

Time Complexity: O(n)
Space Complexity: O(n)

Edge Cases:
- Duplicate appears at the beginning.
- Duplicate appears at the end.
- All values are distinct.
- Single-element input.
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


def test_contains_duplicate() -> None:
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1, 1]) is True
    assert contains_duplicate([1]) is False
    assert contains_duplicate([-1, 0, 2, -1]) is True


if __name__ == "__main__":
    test_contains_duplicate()
    print("All tests passed.")

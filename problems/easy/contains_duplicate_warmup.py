"""
Warmup: Contains Duplicate
Date: 2026-07-20
Difficulty: Easy
Pattern: Hash Set

Task:
Given an integer array nums, return True if any value appears at least twice.
Return False if every element is distinct.

Practice goals:
- Choose between set and dict.
- Use Python set syntax correctly.
- Return True only when a duplicate is found.
- Return False after scanning the whole list with no duplicate.
"""


def contains_duplicate(nums: list[int]) -> bool:
    # Write your solution here.
    set_seen = set()
    for num in nums:
        if num in set_seen:
            return True
        set_seen.add(num)
    return False


def test_contains_duplicate() -> None:
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1]) is False
    assert contains_duplicate([1, 1]) is True
    assert contains_duplicate([-1, 0, 2, -1]) is True


if __name__ == "__main__":
    test_contains_duplicate()
    print("All tests passed.")

"""
Problem: Container With Most Water
Date: 2026-09-17
Difficulty: Medium

Given a list of nonnegative heights, each height represents a vertical line
at its index. Adjacent lines are one unit apart. Choose two lines that form
a container with the x-axis and return the maximum water capacity.
The container cannot be tilted. Return the capacity, not the indices.

Constraints:
    2 <= len(height) <= 100_000
    0 <= height[i] <= 10_000

Test cases to design:
    - Exactly two lines.
    - Input containing zero heights.
    - Equal endpoint heights with the best pair in the interior.
"""


def max_area(height: list[int]) -> int:
    
    raise NotImplementedError


def test_max_area() -> None:
    """Add three test cases with independently calculated expected results."""
    raise NotImplementedError


if __name__ == "__main__":
    test_max_area()

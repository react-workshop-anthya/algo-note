"""
Problem: Valid Anagram
Difficulty: Easy
Pattern: Hash Map / Frequency Count

Summary:
Given two strings s and t, return True if t is an anagram of s. An anagram uses
the same characters with the same frequencies, but can appear in a different
order.

Brute Force:
For each character in one string, search and remove a matching character from
the other string. This repeatedly scans the remaining characters.

Optimized Approach:
Check length first. Count the frequency of each character in s with a
dictionary, then scan t and decrement the required count. If a character is
missing or already used up, return False.

Time Complexity: O(n + m), where n = len(s) and m = len(t). Since valid
anagrams must have equal length, this is often written as O(n).
Space Complexity: O(k), where k is the number of distinct characters. If the
input is limited to 26 lowercase English letters, this is O(1); otherwise, it
is O(k) and at most O(n).

Edge Cases:
- Different lengths.
- Empty strings.
- Same characters but different frequencies.
- Same frequencies in different order.
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts: dict[str, int] = {}

    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for char in t:
        if char not in counts or counts[char] == 0:
            return False

        counts[char] -= 1

    return True


def test_is_anagram() -> None:
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("a", "ab") is False
    assert is_anagram("", "") is True
    assert is_anagram("aacc", "ccac") is False
    assert is_anagram("ab", "ba") is True


if __name__ == "__main__":
    test_is_anagram()
    print("All tests passed.")

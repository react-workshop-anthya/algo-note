"""
Warmup: Valid Anagram
Date: 2026-07-20
Difficulty: Easy
Pattern: Hash Map / Frequency Count

Task:
Given two strings s and t, return True if t is an anagram of s, and False
otherwise.

An anagram uses the same characters with the same frequencies, but can be in a
different order.

Examples:
- s = "anagram", t = "nagaram" -> True
- s = "rat", t = "car" -> False

Practice goals:
- Check length early.
- Count character frequency with a dictionary.
- Decrease counts while scanning the second string.
- Return False when a required character is missing or overused.
"""


def is_anagram(s: str, t: str) -> bool:
    # Write your solution here.
    if len(s) != len(t):
        return False
    seen: dict[str, int] = {}
    for v in s:
        if v in seen:
            seen[v] += 1
        else:
            seen[v] = 1
    for v in t:
        if v in seen and seen[v] != 0:
            seen[v] -= 1
        else:
            return False
    return True


def test_is_anagram() -> None:
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("a", "ab") is False
    assert is_anagram("", "") is True
    assert is_anagram("aacc", "ccac") is False


if __name__ == "__main__":
    test_is_anagram()
    print("All tests passed.")

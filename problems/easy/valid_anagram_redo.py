"""
Redo: Valid Anagram
Date: 2026-08-05
Difficulty: Easy

Given two strings s and t, return True if t is an anagram of s, and False
otherwise.

An anagram uses the same characters with the same frequencies, but may place
them in a different order.
"""


def is_anagram(s: str, t: str) -> bool:
    pass


def test_is_anagram() -> None:
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("a", "ab") is False
    assert is_anagram("", "") is True
    assert is_anagram("aacc", "ccac") is False
    assert is_anagram("ab", "ba") is True
    assert is_anagram("aab", "abb") is False


if __name__ == "__main__":
    test_is_anagram()
    print("All tests passed.")

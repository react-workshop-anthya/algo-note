"""
Problem: Group Anagrams
Date: 2026-08-28
Difficulty: Medium

Given a list of strings, group the anagrams together. The groups and the
strings within each group may be returned in any order.

Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = {}

    for word in strs:
        key = "".join(sorted(word))

        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    return list(groups.values())


def normalize(groups: list[list[str]]) -> list[tuple[str, ...]]:
    """Normalize group order so tests accept any valid output ordering."""
    return sorted(tuple(sorted(group)) for group in groups)


def test_group_anagrams() -> None:
    assert normalize(
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    ) == normalize([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    assert normalize(group_anagrams([""])) == normalize([[""]])
    assert normalize(group_anagrams(["a"])) == normalize([["a"]])
    assert normalize(group_anagrams(["", ""])) == normalize([["", ""]])
    assert normalize(group_anagrams(["abc", "abc", "bca", "xyz"])) == normalize(
        [["abc", "abc", "bca"], ["xyz"]]
    )


if __name__ == "__main__":
    test_group_anagrams()
    print("All tests passed.")

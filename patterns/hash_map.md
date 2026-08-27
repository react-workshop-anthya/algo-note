# Hash Map

## When To Use

- Need to check whether a value has appeared before.
- Need fast lookup for complements, frequencies, or previous indices.
- Need to reduce repeated scanning from O(n^2) to O(n).

## Core Idea

Store useful information from earlier elements in a dictionary, then use O(1)
average-time lookup when processing the current element.

Use a set when only existence matters:

```python
seen = set()
```

Use a dictionary when extra information matters, such as index or frequency:

```python
seen = {}
```

For Two Sum, the map stores:

```python
num -> index
```

For each current number, check whether its complement already exists:

```python
complement = target - num
```

For frequency counting, the map stores:

```python
char -> count
```

For grouping, derive a canonical key shared by equivalent items:

```python
sorted_word -> list of original words
```

## Template

Hash Set:

```python
seen = set()

for num in nums:
    if num in seen:
        return True

    seen.add(num)

return False
```

Hash Map:

```python
seen = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        return [seen[complement], i]

    seen[num] = i
```

Frequency Count:

```python
counts = {}

for char in s:
    counts[char] = counts.get(char, 0) + 1

for char in t:
    if char not in counts or counts[char] == 0:
        return False

    counts[char] -= 1

return True
```

Grouping by a canonical key:

```python
groups = {}

for word in words:
    key = "".join(sorted(word))

    if key in groups:
        groups[key].append(word)
    else:
        groups[key] = [word]

return list(groups.values())
```

## Complexity

- Time: O(n), because each item is processed once.
- Space: O(n), because the map can store up to n items. If the key space is
  fixed, such as 26 lowercase English letters, space can be O(1).

## Common Mistakes

- Using `seen[complement]` directly before checking `complement in seen`.
- Forgetting that index `0` is falsy in Python.
- Storing the current number before checking the complement, which can reuse the
  same element.
- Confusing `num -> index` with `complement -> num`.
- Using a dictionary when a set is enough.
- Returning `True` after scanning all values without finding a duplicate.
- Writing `counts[char] += 1` before initializing `counts[char]`.
- Treating fixed alphabet size as O(1) time. It only makes auxiliary space O(1);
  the input still must be scanned.
- Returning the internal grouping dictionary when the required output is a list
  of groups.
- Treating the number of strings and the maximum string length as the same
  input dimension.

## Problems Practiced

| Date | Problem | Difficulty | Result | Review Due |
| --- | --- | --- | --- | --- |
| 2026-06-12 | Two Sum | Easy | Solved with hints | 2026-06-15 |
| 2026-06-15 | Contains Duplicate | Easy | Solved with hints | 2026-06-18 |
| 2026-07-20 | Valid Anagram | Easy | Solved with debugging | 2026-07-23 |
| 2026-08-28 | Group Anagrams | Medium | Solved with guidance | 2026-08-31 |

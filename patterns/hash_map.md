# Hash Map

## When To Use

- Need to check whether a value has appeared before.
- Need fast lookup for complements, frequencies, or previous indices.
- Need to reduce repeated scanning from O(n^2) to O(n).

## Core Idea

Store useful information from earlier elements in a dictionary, then use O(1)
average-time lookup when processing the current element.

For Two Sum, the map stores:

```python
num -> index
```

For each current number, check whether its complement already exists:

```python
complement = target - num
```

## Template

```python
seen = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        return [seen[complement], i]

    seen[num] = i
```

## Complexity

- Time: O(n), because each item is processed once.
- Space: O(n), because the map can store up to n items.

## Common Mistakes

- Using `seen[complement]` directly before checking `complement in seen`.
- Forgetting that index `0` is falsy in Python.
- Storing the current number before checking the complement, which can reuse the
  same element.
- Confusing `num -> index` with `complement -> num`.

## Problems Practiced

| Date | Problem | Difficulty | Result | Review Due |
| --- | --- | --- | --- | --- |
| 2026-06-12 | Two Sum | Easy | Solved with hints | 2026-06-15 |

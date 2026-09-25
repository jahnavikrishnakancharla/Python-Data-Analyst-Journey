# Day 11 — Python Sets

## Overview

Day 11 focuses on Python Sets and their practical use in data analysis.

A set is an unordered collection of unique elements in Python.

---

## Topics Covered

1. Creating Sets
2. Unique Elements
3. Unordered Nature
4. `add()`
5. `update()`
6. `remove()`
7. `discard()`
8. `pop()`
9. `clear()`
10. Membership Operators
11. `len()`
12. Union
13. Intersection
14. Difference
15. Symmetric Difference
16. Set Operators
17. List to Set Conversion
18. Set to List Conversion
19. Duplicate Removal
20. `issubset()`
21. `issuperset()`
22. `isdisjoint()`
23. Set Comprehension
24. Data Analyst Use Cases

---

## Python Terminology

### Set
An unordered collection of unique elements.

### Unique
A value that occurs without duplicates.

### Duplicate
The same value appearing more than once.

### Membership Operator
`in` and `not in` are used to check whether an element exists in a collection.

### Deduplication
Removing duplicate values from data.

### Set Comprehension
A concise way to create a set using iteration and a condition.

### Subset
A set whose all elements are contained in another set.

### Superset
A set that contains all elements of another set.

### Disjoint Sets
Two sets that have no common elements.

---

## Important Set Methods

### `add()`
Adds one element.

### `update()`
Adds multiple elements.

### `remove()`
Removes a specified element and raises an error if it does not exist.

### `discard()`
Removes a specified element without raising an error if it does not exist.

### `pop()`
Removes and returns an arbitrary element.

### `clear()`
Removes all elements.

---

## Set Operations

| Operation | Meaning | Method | Operator |
|---|---|---|---|
| Union | All elements from both sets | `union()` | `|` |
| Intersection | Common elements | `intersection()` | `&` |
| Difference | Elements only in first set | `difference()` | `-` |
| Symmetric Difference | Elements in only one set | `symmetric_difference()` | `^` |

---

## Set Comparison

### `issubset()`

Checks whether all elements of one set are present in another set.

```python
A.issubset(B)

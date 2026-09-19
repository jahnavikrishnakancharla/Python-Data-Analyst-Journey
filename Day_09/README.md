# Day 09 — Python Lists

## 📌 Overview

Today I learned Python Lists and practiced how lists are used to store, access, modify, filter, and analyze multiple values.

Lists are very important for Data Analysis because they help us work with collections of values before moving to tools such as NumPy and Pandas.

## 📚 Topics Covered

1. Creating Lists
2. Indexing
3. Negative Indexing
4. Slicing
5. Updating List Values
6. `append()`
7. `insert()`
8. `extend()`
9. `remove()`
10. `pop()`
11. `del`
12. `sort()`
13. `reverse()`
14. `len()`
15. `min()`, `max()`, `sum()`
16. Membership Operators — `in`, `not in`
17. Lists with `for` Loops
18. Lists with Conditions
19. Counting and Summing
20. List Comprehension — Filtering
21. List Comprehension — Transformation
22. Filter + Transformation
23. Nested Lists
24. Nested Lists + Loops
25. User Input → List
26. List Comprehension with `if-else`
27. Copying Lists
28. Common List Operations and Mistakes
29. Data Analyst Style List Filtering

## 💡 Important Concepts

### List Indexing

Python list indexing starts from `0`.

```python
numbers = [10, 20, 30]

print(numbers[0])
print(numbers[2])
```

### List Comprehension

List comprehensions provide a short way to create new lists.

```python
even_numbers = [num for num in numbers if num % 2 == 0]
```

### Filter + Transformation

```python
new_sales = [
    sale + (sale * 10 / 100)
    for sale in sales
    if sale >= 5000
]
```

This combines:

* Looping
* Filtering
* Transformation

## 📊 Data Analyst Connection

Lists help build the basic logic used in data analysis:

```text
Raw Data
   ↓
Store Data
   ↓
Filter Data
   ↓
Transform Data
   ↓
Calculate Statistics
   ↓
Find Insights
```

These concepts become much more powerful when working with NumPy arrays and Pandas DataFrames.

## 🧠 Key Methods

| Method      | Purpose                |
| ----------- | ---------------------- |
| `append()`  | Add one item           |
| `insert()`  | Add item at a position |
| `extend()`  | Add multiple items     |
| `remove()`  | Remove by value        |
| `pop()`     | Remove by index        |
| `sort()`    | Sort the list          |
| `reverse()` | Reverse the list       |
| `copy()`    | Create a separate copy |

## 📁 Files

```text
Day_09/
│
├── lists_practice.py
├── list_challenges.py
├── mini_project.py
├── README.md
└── requirements.txt
```

## 🎯 Learning Outcome

After completing Day 9, I can:

* Create and modify Python lists
* Access list elements using indexing
* Use slicing
* Add and remove values
* Sort and reverse data
* Calculate basic statistics
* Filter data using conditions
* Use list comprehensions
* Work with nested lists
* Apply list concepts to simple Data Analyst tasks

## 🚀 Next Step

Next I will continue with the next Python data-handling concepts and gradually move toward NumPy and Pandas for Data Analysis.

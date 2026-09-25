# ==========================================
# DAY 11 - PYTHON SETS
# ==========================================

# 1. Creating a Set
skills = {"Python", "SQL", "Pandas", "Excel", "Power BI"}
print("Skills:", skills)

print("=" * 50)

# 2. Unique Elements
numbers = {10, 20, 10, 30, 20, 40, 10}
print("Unique numbers:", numbers)

print("=" * 50)

# 3. add()
skills = {"Python", "SQL", "Pandas"}
skills.add("Excel")
print("After add():", skills)

print("=" * 50)

# 4. update()
skills = {"Python", "SQL"}
skills.update(["Pandas", "Excel", "Power BI"])
print("After update():", skills)

print("=" * 50)

# 5. remove()
skills = {"Python", "SQL", "Pandas", "Excel"}
skills.remove("SQL")
print("After remove():", skills)

print("=" * 50)

# 6. discard()
skills = {"Python", "SQL", "Pandas", "Excel"}
skills.discard("Java")
print("After discard():", skills)

print("=" * 50)

# 7. pop()
skills = {"Python", "SQL", "Pandas", "Excel"}
removed_skill = skills.pop()
print("Removed by pop():", removed_skill)
print("Remaining skills:", skills)

print("=" * 50)

# 8. clear()
skills = {"Python", "SQL", "Pandas", "Excel"}
skills.clear()
print("After clear():", skills)

print("=" * 50)

# 9. Membership Operators
skills = {"Python", "SQL", "Pandas", "Excel"}

print("Python" in skills)
print("Java" in skills)
print("Java" not in skills)

print("=" * 50)

# 10. len()
print("Number of skills:", len(skills))

print("=" * 50)

# 11. Union
python_students = {"Janu", "Ravi", "Kiran"}
sql_students = {"Ravi", "Kiran", "Anil"}

all_students = python_students.union(sql_students)
print("Union:", all_students)

print("=" * 50)

# 12. Intersection
common_students = python_students.intersection(sql_students)
print("Intersection:", common_students)

print("=" * 50)

# 13. Difference
python_only = python_students.difference(sql_students)
print("Python only:", python_only)

print("=" * 50)

# 14. Symmetric Difference
unique_students = python_students.symmetric_difference(sql_students)
print("Symmetric difference:", unique_students)

print("=" * 50)

# 15. Set Operators
A = {1, 2, 3}
B = {3, 4, 5}

print("A | B:", A | B)
print("A & B:", A & B)
print("A - B:", A - B)
print("A ^ B:", A ^ B)

print("=" * 50)

# 16. List to Set Conversion
categories = [
    "Clothing",
    "Electronics",
    "Clothing",
    "Beauty",
    "Electronics",
    "Books"
]

unique_categories = set(categories)
print("Unique categories:", unique_categories)

print("=" * 50)

# 17. Set to List Conversion
unique_categories = {"Clothing", "Electronics", "Beauty", "Books"}

categories_list = list(unique_categories)
print("Categories list:", categories_list)

print("=" * 50)

# 18. Removing Duplicates from a List
categories = [
    "Clothing",
    "Electronics",
    "Clothing",
    "Beauty",
    "Electronics",
    "Books"
]

unique_categories = list(set(categories))
print("List after deduplication:", unique_categories)

print("=" * 50)

# 19. issubset()
python_skills = {"Python", "Pandas"}
data_skills = {"Python", "Pandas", "SQL", "Excel"}

print("Is subset:", python_skills.issubset(data_skills))

print("=" * 50)

# 20. issuperset()
print("Is superset:", data_skills.issuperset(python_skills))

print("=" * 50)

# 21. isdisjoint()
A = {"Python", "Pandas"}
B = {"SQL", "Excel"}

print("Are A and B disjoint?:", A.isdisjoint(B))

print("=" * 50)

# 22. Set Comprehension
numbers = [10, 20, 30, 40, 50]

even_numbers = {x for x in numbers if x % 2 == 0}

print("Even numbers:", even_numbers)

print("=" * 50)

# 23. Data Analyst Use Case
customer_ids = [
    101, 102, 103, 101, 104,
    102, 105, 106, 103
]

unique_customer_ids = set(customer_ids)

print("Unique customer IDs:", unique_customer_ids)
print("Number of unique customers:", len(unique_customer_ids))

print("=" * 50)

# 24. Comparing Two Customer Groups
group_a = {101, 102, 103, 104}
group_b = {103, 104, 105, 106}

print("Customers in both groups:", group_a & group_b)
print("Only in Group A:", group_a - group_b)
print("Only in Group B:", group_b - group_a)
print("All unique customers:", group_a | group_b)

# ==========================================
# END OF DAY 11
# ==========================================

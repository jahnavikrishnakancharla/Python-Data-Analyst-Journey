# ==========================================
# DAY 10 - PYTHON TUPLES
# ==========================================

# 1. What is a Tuple?
student = ("Janu", "Data Science", 9.4)
print("Tuple:", student)

# 2. Ordered Tuple
numbers = (10, 20, 30, 40)
print("First element:", numbers[0])

# 3. Immutable
# Tuple elements cannot be changed directly.
# numbers[0] = 100  # This will cause an error

# 4. Creating Tuples
numbers = (10, 20, 30, 40)
names = ("Janu", "Ravi", "Kiran")
mixed = ("Janu", 20, 9.4, True)

print("Numbers:", numbers)
print("Names:", names)
print("Mixed tuple:", mixed)

# 5. Indexing
student = ("Janu", "CSD", 9.4)

print(student[0])
print(student[1])
print(student[2])

# 6. Negative Indexing
print(student[-1])
print(student[-2])
print(student[-3])

# 7. Slicing
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[0:3])
print(numbers[2:])

# 8. Tuple Packing
student = "Janu", "CSD", 9.4
print("Packed tuple:", student)

# 9. Tuple Unpacking
student = ("Janu", "CSD", 9.4)

name, branch, cgpa = student

print("Name:", name)
print("Branch:", branch)
print("CGPA:", cgpa)

# 10. count()
numbers = (10, 20, 10, 30, 10, 40)

print("Count of 10:", numbers.count(10))

# 11. index()
numbers = (10, 20, 30, 20, 40)

print("First index of 20:", numbers.index(20))

# 12. Tuple + For Loop
sales = (4500, 7800, 2300, 9100, 5600)

for sale in sales:
    if sale >= 5000:
        print("Sale:", sale)

# 13. Membership Operators
categories = ("Clothing", "Electronics", "Books", "Beauty")

print("Books" in categories)
print("Laptop" in categories)
print("Shoes" not in categories)

# 14. Nested Tuples
students = (
    ("Janu", 9.4),
    ("Ravi", 8.7),
    ("Kiran", 9.1)
)

print(students)
print(students[0][0])
print(students[2][1])

# 15. List to Tuple
sales_list = [1000, 2000, 3000]

sales_tuple = tuple(sales_list)

print("Tuple:", sales_tuple)

# 16. Tuple to List
sales_tuple = (1000, 2000, 3000)

sales_list = list(sales_tuple)

print("List:", sales_list)

sales_list.append(4000)

print("Updated list:", sales_list)

sales_tuple = tuple(sales_list)

print("Updated tuple:", sales_tuple)

# 17. List vs Tuple
my_list = ["Clothing", "Books", "Beauty"]
my_tuple = ("Clothing", "Books", "Beauty")

print("List:", my_list)
print("Tuple:", my_tuple)

# 18. Data Analyst Use Case
sales = (
    ("Clothing", 12000),
    ("Electronics", 8500),
    ("Books", 4500),
    ("Beauty", 9200)
)

for category, value in sales:
    if value >= 9000:
        print("High Sales Category:", category)

# ==========================================
# END OF DAY 10 PRACTICE
# ==========================================

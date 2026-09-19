# ============================================================
# DAY 09 - PYTHON LISTS
# Python for Data Analysis
# ============================================================


# ------------------------------------------------------------
# 1. Creating a List
# ------------------------------------------------------------

students = ["Jahnavi", "Ravi", "Kiran"]
marks = [85, 72, 91, 68, 95]

print("Students:", students)
print("Marks:", marks)


# ------------------------------------------------------------
# 2. Indexing
# ------------------------------------------------------------

print("\n--- Indexing ---")
print("First student:", students[0])
print("Second student:", students[1])


# ------------------------------------------------------------
# 3. Negative Indexing
# ------------------------------------------------------------

print("\n--- Negative Indexing ---")
print("Last student:", students[-1])
print("Second-last student:", students[-2])


# ------------------------------------------------------------
# 4. Slicing
# ------------------------------------------------------------

print("\n--- Slicing ---")
print("First three marks:", marks[:3])
print("Middle marks:", marks[1:4])
print("From third mark:", marks[2:])
print("From second mark:", marks[1:])


# ------------------------------------------------------------
# 5. Updating List Values
# ------------------------------------------------------------

marks[1] = 82
marks[-2] = 78

print("\n--- Updated Marks ---")
print(marks)


# ------------------------------------------------------------
# 6. append()
# ------------------------------------------------------------

products = ["Shirt", "Jeans"]

products.append("Shoes")

print("\n--- append() ---")
print(products)


# ------------------------------------------------------------
# 7. insert()
# ------------------------------------------------------------

products.insert(1, "Watch")

print("\n--- insert() ---")
print(products)


# ------------------------------------------------------------
# 8. extend()
# ------------------------------------------------------------

products.extend(["Bag", "Cap"])

print("\n--- extend() ---")
print(products)


# ------------------------------------------------------------
# 9. remove()
# ------------------------------------------------------------

products.remove("Jeans")

print("\n--- remove() ---")
print(products)


# ------------------------------------------------------------
# 10. pop()
# ------------------------------------------------------------

products.pop(1)

print("\n--- pop() ---")
print(products)


# ------------------------------------------------------------
# 11. del
# ------------------------------------------------------------

del products[-1]

print("\n--- del ---")
print(products)


# ------------------------------------------------------------
# 12. sort()
# ------------------------------------------------------------

sales = [90, 89, 67, 45, 56]

sales.sort(reverse=True)

print("\n--- Descending Sort ---")
print(sales)

sales.sort()

print("--- Ascending Sort ---")
print(sales)


# ------------------------------------------------------------
# 13. reverse()
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print("\n--- Reverse ---")
print(numbers)


# ------------------------------------------------------------
# 14. len()
# ------------------------------------------------------------

sales = [4500, 1200, 7800, 3200, 9500, 2100]

print("\n--- len() ---")
print("Number of sales:", len(sales))


# ------------------------------------------------------------
# 15. min(), max(), sum()
# ------------------------------------------------------------

print("\n--- min(), max(), sum() ---")
print("Minimum:", min(sales))
print("Maximum:", max(sales))
print("Total:", sum(sales))
print("Average:", sum(sales) / len(sales))


# ------------------------------------------------------------
# 16. Membership Operators
# ------------------------------------------------------------

categories = ["Clothing", "Electronics", "Books", "Beauty"]

print("\n--- Membership ---")
print("Clothing" in categories)
print("Laptop" in categories)
print("Books" not in categories)


# ------------------------------------------------------------
# 17. List + for Loop
# ------------------------------------------------------------

print("\n--- Sales above 5000 ---")

for sale in sales:
    if sale >= 5000:
        print(sale)


# ------------------------------------------------------------
# 18. List + Condition
# ------------------------------------------------------------

print("\n--- High Sales ---")

high_sales = []

for sale in sales:
    if sale >= 5000:
        high_sales.append(sale)

print(high_sales)


# ------------------------------------------------------------
# 19. Counting and Summing
# ------------------------------------------------------------

count = 0
total = 0

for sale in sales:
    if sale >= 5000:
        count += 1
        total += sale

print("\n--- Count and Total ---")
print("High sales count:", count)
print("High sales total:", total)


# ------------------------------------------------------------
# 20. List Comprehension - Filtering
# ------------------------------------------------------------

numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = [num for num in numbers if num % 2 == 0]

print("\n--- List Comprehension - Filtering ---")
print(even_numbers)


# ------------------------------------------------------------
# 21. List Comprehension - Transformation
# ------------------------------------------------------------

doubled_numbers = [num * 2 for num in numbers]

print("\n--- List Comprehension - Transformation ---")
print(doubled_numbers)


# ------------------------------------------------------------
# 22. Filter + Transformation
# ------------------------------------------------------------

sales = [1200, 4500, 7800, 2300, 9500, 3200]

increased_sales = [
    sale + (sale * 10 / 100)
    for sale in sales
    if sale >= 5000
]

print("\n--- Filter + Transformation ---")
print(increased_sales)


# ------------------------------------------------------------
# 23. Nested Lists
# ------------------------------------------------------------

students = [
    ["Jahnavi", 9.4],
    ["Ravi", 8.7],
    ["Kiran", 9.1]
]

print("\n--- Nested Lists ---")
print(students)


# ------------------------------------------------------------
# 24. Nested Lists + Loop
# ------------------------------------------------------------

print("\n--- Students with CGPA >= 9.0 ---")

for student in students:
    if student[1] >= 9.0:
        print(student[0], student[1])


# ------------------------------------------------------------
# 25. User Input -> List
# ------------------------------------------------------------

# Example:
# numbers = []
#
# for i in range(5):
#     num = int(input("Enter number: "))
#     numbers.append(num)
#
# print(numbers)


# ------------------------------------------------------------
# 26. List Comprehension with if-else
# ------------------------------------------------------------

numbers = [10, 15, 20, 25]

number_type = [
    "Even" if num % 2 == 0 else "Odd"
    for num in numbers
]

print("\n--- List Comprehension with if-else ---")
print(number_type)


# ------------------------------------------------------------
# 27. Copying Lists
# ------------------------------------------------------------

original = [10, 20, 30]

copied_list = original.copy()

copied_list.append(40)

print("\n--- Copying Lists ---")
print("Original:", original)
print("Copied:", copied_list)


# ------------------------------------------------------------
# 28. Common List Operations
# ------------------------------------------------------------

data = [10, 20, 30, 40]

print("\n--- Common List Operations ---")

print("Length:", len(data))
print("Minimum:", min(data))
print("Maximum:", max(data))
print("Total:", sum(data))


# ------------------------------------------------------------
# 29. Data Analyst Style Filtering
# ------------------------------------------------------------

sales = [4500, 1200, 7800, 3200, 9500]

high_sales = [
    sale for sale in sales
    if sale >= 5000
]

print("\n--- Data Analyst Style Filtering ---")
print("High Sales:", high_sales)

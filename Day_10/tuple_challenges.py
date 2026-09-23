# ==========================================
# DAY 10 - TUPLE CHALLENGES
# ==========================================


# Challenge 1 - Tuple Analysis

marks = (85, 92, 76, 92, 88, 95, 92)

print("Number of elements:", len(marks))
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("92 occurs:", marks.count(92), "times")
print("First index of 92:", marks.index(92))

print("=" * 50)


# Challenge 2 - Data Analyst Sales Filtering

sales = (
    ("Clothing", 12000),
    ("Electronics", 8500),
    ("Books", 4500),
    ("Beauty", 9200),
    ("Games", 15000)
)

for category, value in sales:
    if value >= 9000:
        print(category)

print("=" * 50)


# Challenge 3 - Tuple Unpacking

employee = ("Jahnavi", "Data Analyst", 45000)

name, role, salary = employee

print("Name:", name)
print("Role:", role)
print("Salary:", salary)

print("=" * 50)


# Challenge 4 - List to Tuple

categories = ["Clothing", "Books", "Beauty", "Electronics"]

cat_tuple = tuple(categories)

print("Tuple:", cat_tuple)

print("Beauty" in cat_tuple)

print("=" * 50)

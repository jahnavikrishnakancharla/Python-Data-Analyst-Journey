# ==========================================
# DAY 8 - FUNCTIONS PRACTICE
# ==========================================


# 1. Basic Function

def welcome():
    print("Welcome to Python Learning")


welcome()


# 2. Function with Parameter

def greet(name):
    print("Hello", name)


greet("Janu")


# 3. Function with Two Parameters

def add(a, b):
    print(a + b)


add(10, 20)


# 4. Function with Return

def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)
print("Addition:", result)


# 5. Function with User Input

def mult(a, b):
    return a * b


a = int(input("Enter a: "))
b = int(input("Enter b: "))

result = mult(a, b)
print("Multiplication:", result)

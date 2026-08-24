# ==========================================
# DAY 8 - FUNCTIONS CHALLENGES
# ==========================================


# Challenge 1 - Square

def square(num):
    return num ** 2


num = int(input("Enter number: "))

result = square(num)
print("Square:", result)


# Challenge 2 - Even or Odd

def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input("Enter number: "))

result = check_even(num)
print("Result:", result)


# Challenge 3 - Factorial

def factorial(num):
    fact = 1

    while num:
        fact = fact * num
        num = num - 1

    return fact


num = int(input("Enter number: "))

result = factorial(num)
print("Factorial:", result)


# Challenge 4 - Find Maximum

def find_max(a, b, c):

    if a > b and a > c:
        return a

    elif b > a and b > c:
        return b

    else:
        return c


a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

result = find_max(a, b, c)

print("Largest:", result)

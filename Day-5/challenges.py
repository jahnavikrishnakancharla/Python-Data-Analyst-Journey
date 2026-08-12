# =========================================================
# DAY 05 - FOR LOOP CHALLENGES
# =========================================================


# Challenge 1: Numbers divisible by 5 from 1 to 50

print("================ Challenge 1 ================")

for i in range(1, 51):
    if i % 5 == 0:
        print("Divisible by 5 Number :", i)

print("================ Challenge 1 Completed ================\n")


# Challenge 2: Numbers divisible by both 3 and 5
# from 1 to 100

print("================ Challenge 2 ================")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Number :", i)

print("================ Challenge 2 Completed ================\n")


# Challenge 3: Factorial using a for loop

print("================ Challenge 3 ================")

num = 5
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Number :", num)
print("Factorial :", fact)

print("================ Challenge 3 Completed ================\n")


# Challenge 4: Right-aligned Star Pattern

print("================ Challenge 4 ================")

for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)

print("================ Challenge 4 Completed ================\n")

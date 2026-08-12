# =========================================================
# DAY 05 - FOR LOOP PRACTICE
# =========================================================

# Program 1: Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

print("\n================ Program 1 Completed ================\n")


# Program 2: Print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)

print("\n================ Program 2 Completed ================\n")


# Program 3: Print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print("Even Number :", i)

print("\n================ Program 3 Completed ================\n")


# Program 4: Print odd numbers from 1 to 20
for i in range(1, 21):
    if i % 2 != 0:
        print("Odd Number :", i)

print("\n================ Program 4 Completed ================\n")


# Program 5: Print a name 5 times
name = input("Enter Name : ")

for i in range(5):
    print(name)

print("\n================ Program 5 Completed ================\n")


# Program 6: Multiplication table
num = int(input("Enter Number : "))

for i in range(1, 11):
    print(num, "*", i, "=", num * i)

print("\n================ Program 6 Completed ================\n")


# Program 7: Sum of numbers from 1 to 10
total = 0

for i in range(1, 11):
    total = total + i

print("Sum of Numbers from 1 to 10 :", total)

print("\n================ Program 7 Completed ================\n")


# Program 8: Sum of even numbers from 1 to 20
total = 0

for i in range(1, 21):
    if i % 2 == 0:
        total = total + i

print("Sum of Even Numbers :", total)

print("\n================ Program 8 Completed ================\n")


# Program 9: Squares from 1 to 10
for i in range(1, 11):
    square = i ** 2
    print("Number :", i, "| Square :", square)

print("\n================ Program 9 Completed ================\n")


# Program 10: Cubes from 1 to 10
for i in range(1, 11):
    cube = i ** 3
    print("Number :", i, "| Cube :", cube)

print("\n================ Program 10 Completed ================\n")

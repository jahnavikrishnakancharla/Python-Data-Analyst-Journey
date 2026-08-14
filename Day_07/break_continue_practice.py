# Program 1 - break at 6

i = 1
while i <= 10:
    print(i)
    if i == 6:
        break
    i = i + 1


# Program 2 - Stop when user enters 0

while True:
    num = int(input("Enter your number: "))

    if num == 0:
        break

    print(num)


# Program 3 - Stop when negative number

while True:
    num = int(input("Enter your number: "))

    if num < 0:
        print("Stop the program")
        break

    print(num)


# Program 4 - Stop when divisible by 7

while True:
    num = int(input("Enter your number: "))

    if num % 7 == 0:
        print("Stop the program")
        break

    print(num)


# Program 5 - Continue example

i = 1
while i <= 10:
    if i == 5:
        i = i + 1
        continue

    print(i)
    i = i + 1


# Program 6 - Pass example

for i in range(1, 6):
    if i == 3:
        pass

    print(i)

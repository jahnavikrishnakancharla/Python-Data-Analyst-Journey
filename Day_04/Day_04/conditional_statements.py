# Program 1 - Even or Odd

num = int(input("Enter your Number : "))
if num % 2 == 0:
    print("The Number is Even")
else:
    print("The Number is Odd")

print("\n================ Program 2 =================")

# Program 2 - Positive, Negative or Zero

num = int(input("Enter your Number : "))
if num > 0:
    print("The Number is Positive")
elif num < 0:
    print("The Number is Negative")
else:
    print("The Number is Zero")

print("\n================ Program 3 =================")

# Program 3 - Largest of Two Numbers

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

if num1 > num2:
    print("Largest Number :", num1)
else:
    print("Largest Number :", num2)

print("\n================ Program 4 =================")

# Program 4 - Largest of Three Numbers

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))

if num1 >= num2 and num1 >= num3:
    print("Largest Number :", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest Number :", num2)
else:
    print("Largest Number :", num3)

print("\n================ Program 5 =================")

# Program 5 - Voting Eligibility

age = int(input("Enter Age : "))

if age >= 18:
    print("Eligible for Vote")
else:
    print("Not Eligible for Vote")

print("\n================ Program 6 =================")

# Program 6 - Pass or Fail

marks = int(input("Enter Student Marks : "))

if marks >= 35:
    print("Student Pass")
else:
    print("Student Fail")

print("\n================ Program 7 =================")

# Program 7 - Leap Year

year = int(input("Enter Year : "))

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

print("\n================ Program 8 =================")

# Program 8 - Login System

username = input("Enter Username : ")
password = input("Enter Password : ")

if username == "admin" and password == "123":
    print("Login Successful")
else:
    print("Invalid Username or Password")

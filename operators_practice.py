# ==========================================
# Day 2 - Python Operators Practice
# Author: Jahnavi Krishna
# ==========================================

# Addition
a = 10
b = 20
print("Addition:", a + b)

# Subtraction
a = 20
b = 10
print("Subtraction:", a - b)

# Multiplication
a = 8
b = 5
print("Multiplication:", a * b)

# Division
a = 25
b = 4
print("Division:", a / b)

# Floor Division
print("Floor Division:", a // b)

# Modulus
print("Modulus:", a % b)

# Power
print("Power:", 5 ** 2)

# Cube of a Number
num = int(input("\nEnter a number: "))
cube = num ** 3
print("Cube:", cube)

# Area of Rectangle
length = float(input("\nEnter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of Rectangle:", area)

# Area of Circle
radius = float(input("\nEnter radius: "))
area = 3.14 * radius * radius
print("Area of Circle:", area)

# Simple Interest
principal = float(input("\nEnter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (Years): "))
si = (principal * rate * time) / 100
print("Simple Interest:", si)

# Celsius to Fahrenheit
celsius = float(input("\nEnter Temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Area of Triangle
base = float(input("\nEnter Base: "))
height = float(input("Enter Height: "))
triangle_area = (base * height) / 2
print("Area of Triangle:", triangle_area)

# Perimeter of Rectangle
length = float(input("\nEnter Length: "))
width = float(input("Enter Width: "))
perimeter = 2 * (length + width)
print("Perimeter of Rectangle:", perimeter)

# Average of Three Numbers
num1 = float(input("\nEnter First Number: "))
num2 = float(input("Enter Second Number: "))
num3 = float(input("Enter Third Number: "))
average = (num1 + num2 + num3) / 3
print("Average:", average)
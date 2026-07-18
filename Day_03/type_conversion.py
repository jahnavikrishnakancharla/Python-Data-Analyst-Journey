# ==========================================
# Day 3 - Type Conversion
# Author: Jahnavi Krishna
# ==========================================

age = 20

print("Original Value:", age)
print("Original Type:", type(age))

# Integer to Float
float_age = float(age)
print("\nConverted to Float:", float_age)
print("Type:", type(float_age))

# Integer to String
string_age = str(age)
print("\nConverted to String:", string_age)
print("Type:", type(string_age))

cgpa = 9.4

# Float to Integer
int_cgpa = int(cgpa)

print("\nOriginal CGPA:", cgpa)
print("Converted to Integer:", int_cgpa)
print("Type:", type(int_cgpa))

# User Input Conversion
number = input("\nEnter a number: ")

print("\nBefore Conversion:", type(number))

number = int(number)

print("After Conversion:", type(number))
print("Square of Number:", number ** 2)

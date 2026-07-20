# =====================================================
# Day 3 - Python Data Types & Type Conversion
# Python for Data Analyst Learning Journey
# =====================================================

# ================= Program 1 ==========================
print("============= Program 1 : Calculator =================")

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

add = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print("Addition       :", add)
print("Subtraction    :", sub)
print("Multiplication :", mult)
print("Division       :", div)

# ================= Program 2 ==========================
print("\n============= Program 2 : Integer to String =================")

num = 21

print("Original Value :", num)
print("Original Type  :", type(num))

convert = str(num)

print("Converted Value :", convert)
print("Converted Type  :", type(convert))

# ================= Program 3 ==========================
print("\n============= Program 3 : Age After 5 Years =================")

age = int(input("Enter your age : "))

print("Current Age :", age)
print("Age After 5 Years :", age + 5)

# ================= Program 4 ==========================
print("\n============= Program 4 : Float to Integer =================")

cgpa = float(input("Enter your CGPA : "))

convert = int(cgpa)

print("Original Type  :", type(cgpa))
print("Converted Type :", type(convert))

# ================= Program 5 ==========================
print("\n============= Program 5 : Square and Cube =================")

num3 = 5

square = num3 * num3
cube = num3 * num3 * num3

print("Square :", square)
print("Cube   :", cube)

# ================= Program 6 ==========================
print("\n============= Program 6 : Check Data Types =================")

name = input("Enter your name : ")
age = int(input("Enter your age : "))
cgpa1 = float(input("Enter your CGPA : "))

print("\nData Types")
print(type(name))
print(type(age))
print(type(cgpa1))

# ================= Mini Project =======================
print("\n============= Student Report System =================")

std_name = input("Enter Student Name : ")
age = int(input("Enter Age : "))
branch = input("Enter Branch : ")
college = input("Enter College Name : ")
city = input("Enter City : ")
state = input("Enter State : ")
cgpa = float(input("Enter CGPA : "))
phone = int(input("Enter Phone Number : "))
email = input("Enter Email ID : ")

is_student = True

print("\n================ Student Details ================")
print("Student Name :", std_name)
print("Age          :", age)
print("Branch       :", branch)
print("College      :", college)
print("City         :", city)
print("State        :", state)
print("CGPA         :", cgpa)
print("Phone Number :", phone)
print("Email ID     :", email)
print("Student      :", is_student)

print("\n================ Data Types ====================")

print("Name          :", type(std_name))
print("Age           :", type(age))
print("CGPA          :", type(cgpa))
print("Phone Number  :", type(phone))
print("Student       :", type(is_student))

print("\n================ Type Conversion ===============")

print("Age Original Type       :", type(age))
age_float = float(age)
print("Age Converted Type      :", type(age_float))

print("CGPA Original Type      :", type(cgpa))
cgpa_int = int(cgpa)
print("CGPA Converted Type     :", type(cgpa_int))

print("Phone Original Type     :", type(phone))
phone_str = str(phone)
print("Phone Converted Type    :", type(phone_str))

print("\n============= Project Completed Successfully! =============")

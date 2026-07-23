print("==================== STUDENT RESULT ANALYSIS SYSTEM ====================")

# Student Details
name = input("Enter Name                  : ")
roll_no = int(input("Enter Roll Number           : "))

print("\n==================== Student Marks ====================")

tel = int(input("Enter Telugu Marks          : "))
hin = int(input("Enter Hindi Marks           : "))
eng = int(input("Enter English Marks         : "))
math = int(input("Enter Maths Marks           : "))
sci = int(input("Enter Science Marks         : "))
soc = int(input("Enter Social Marks          : "))

# Calculations
total_marks = tel + hin + eng + math + sci + soc
avg = total_marks / 6

# Display Student Report
print("\n==================== STUDENT RESULT REPORT ====================")

print("Name              :", name)
print("Roll Number       :", roll_no)

print("\nSubject Marks")
print("-------------------------------")
print("Telugu            :", tel)
print("Hindi             :", hin)
print("English           :", eng)
print("Maths             :", math)
print("Science           :", sci)
print("Social            :", soc)

print("\nTotal Marks       :", total_marks)
print("Average Marks     :", round(avg, 2))

# Result and Grade
if tel >= 35 and hin >= 35 and eng >= 35 and math >= 35 and sci >= 35 and soc >= 35:
    print("Result            : PASS")

    if avg >= 90:
        print("Grade             : A+")
    elif avg >= 80:
        print("Grade             : A")
    elif avg >= 70:
        print("Grade             : B")
    elif avg >= 60:
        print("Grade             : C")
    elif avg >= 50:
        print("Grade             : D")
    else:
        print("Grade             : F")

else:
    print("Result            : FAIL")
    print("Grade             : F")

print("\n==================== PROJECT COMPLETED SUCCESSFULLY ====================")

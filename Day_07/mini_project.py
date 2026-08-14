print("==============================================")
print("          STUDENT MARKS ANALYZER")
print("==============================================")

total = 0
count = 0
highest = 0
passed = 0
failed = 0

while True:

    mark = float(input("Enter Student Mark (-1 to stop): "))

    # Stop entering marks
    if mark == -1:
        break

    # Skip invalid marks
    if mark < 0 or mark > 100:
        print("Invalid Mark! Skipping...")
        continue

    # Process valid mark
    total = total + mark
    count = count + 1

    # Find highest mark
    if mark > highest:
        highest = mark

    # Pass / Fail
    if mark >= 40:
        passed = passed + 1
    else:
        failed = failed + 1


# Display results
print("\n==============================================")
print("                 RESULT")
print("==============================================")

if count > 0:
    average = total / count

    print("Number of Students :", count)
    print("Total Marks        :", total)
    print("Average Marks      :", average)
    print("Highest Mark       :", highest)
    print("Passed Students    :", passed)
    print("Failed Students    :", failed)
else:
    print("No valid marks entered.")

print("==============================================")

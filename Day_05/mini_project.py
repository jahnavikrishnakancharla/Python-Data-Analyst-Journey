# =========================================================
# DAY 05 - MINI PROJECT
# SALES DATA ANALYZER
# =========================================================

print("==================== SALES DATA ANALYZER ====================")

n = int(input("Enter Number Of Products : "))

total_sales = 0
highest = 0
lowest = 0

for i in range(1, n + 1):

    name = input("Enter Product Name : ")
    sale = float(input("Enter Sale Amount : "))

    print("Product :", name, "| Sale :", sale)

    # Calculate total sales
    total_sales += sale

    # Find highest sale
    if sale > highest:
        highest = sale

    # Find lowest sale
    if i == 1:
        lowest = sale
    elif sale < lowest:
        lowest = sale


# Calculate average
average = total_sales / n

print("\n==================== SALES REPORT ====================")

print("Number Of Products :", n)
print("Total Sales        :", total_sales)
print("Average Sales      :", average)
print("Highest Sale       :", highest)
print("Lowest Sale        :", lowest)

print("=======================================================")
print("             SALES ANALYSIS COMPLETED")
print("=======================================================")

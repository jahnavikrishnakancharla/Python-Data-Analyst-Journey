num = int(input("Enter your num: "))
original = num
digits = 0
total = 0
rev = 0

while num > 0:
    digit = num % 10
    digits = digits + 1
    total = total + digit
    num = num // 10
    rev = rev * 10 + digit

print("Number of Digits :", digits)
print("Sum of Digits :", total)
print("Reverse :", rev)

if original == rev:
    print("Palindrome : Yes")
else:
    print("Palindrome : No")

if original % 2 == 0:
    print("Even / Odd : Even")
else:
    print("Even / Odd : Odd")

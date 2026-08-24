# ==========================================
# DAY 8 MINI PROJECT
# PASSWORD STRENGTH CHECKER
# ==========================================


# Function to check whether the password
# contains at least 8 characters
def check_length(password):
    return len(password) >= 8


# Function to check whether the password
# contains at least one uppercase letter
def check_uppercase(password):
    for char in password:
        if char.isupper():
            return True

    return False


# Function to check whether the password
# contains at least one lowercase letter
def check_lowercase(password):
    for char in password:
        if char.islower():
            return True

    return False


# Function to check whether the password
# contains at least one number
def check_digit(password):
    for char in password:
        if char.isdigit():
            return True

    return False


# Function to check whether the password
# contains at least one special character
def check_special_character(password):

    # Characters considered special characters
    special_characters = "!@#$%^&*()-_=+[]{};:,.?/"

    # Check every character in the password
    for char in password:

        # Check whether the character is special
        if char in special_characters:
            return True

    return False


# Function to calculate the password strength
def check_strength(password):

    # Start the score at zero
    score = 0

    # Check password length
    if check_length(password):
        score = score + 1

    # Check uppercase letter
    if check_uppercase(password):
        score = score + 1

    # Check lowercase letter
    if check_lowercase(password):
        score = score + 1

    # Check number
    if check_digit(password):
        score = score + 1

    # Check special character
    if check_special_character(password):
        score = score + 1

    # Return the final score
    return score


# ==========================================
# MAIN PROGRAM
# ==========================================

# Display the project title
print("========================================")
print("       PASSWORD STRENGTH CHECKER")
print("========================================")


# Ask the user to enter a password
password = input("Enter your password: ")


# Check each password condition
length = check_length(password)
uppercase = check_uppercase(password)
lowercase = check_lowercase(password)
digit = check_digit(password)
special = check_special_character(password)


# Calculate the total strength score
score = check_strength(password)


# Display the results
print("\n============= ANALYSIS =============")


# Display whether the password has enough characters
if length:
    print("✓ Length: Good")
else:
    print("✗ Length: Too Short")


# Display uppercase result
if uppercase:
    print("✓ Uppercase: Yes")
else:
    print("✗ Uppercase: No")


# Display lowercase result
if lowercase:
    print("✓ Lowercase: Yes")
else:
    print("✗ Lowercase: No")


# Display number result
if digit:
    print("✓ Number: Yes")
else:
    print("✗ Number: No")


# Display special character result
if special:
    print("✓ Special Character: Yes")
else:
    print("✗ Special Character: No")


# Display the score
print("\nScore:", score, "/ 5")


# Decide the final password strength
if score <= 2:
    strength = "WEAK"

elif score <= 4:
    strength = "MEDIUM"

else:
    strength = "STRONG"


# Display final strength
print("Password Strength:", strength)

print("========================================")

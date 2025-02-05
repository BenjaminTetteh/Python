# Problem: You are given a certain amount of money in cents.
# Write a Python program to convert this amount into dollars, quarters,
# dimes, nickels, and pennies. There are 100 cents in a dollar, 25 cents in a quarter,
# 10 cents in a dime, 5 cents in a nickel, and 1 cent in a penny.

# Tasks: Create a Python solution that accepts an integer input representing
# the total amount of money in cents. Output the converted total number of dollars,
# quarters, dimes, nickels, and pennies based on the input value.


# Accept an integer input in cents
cents = int(input("Enter amount in cents: "))

# Convert cents to dollars, quarters, dimes, nickel and pennies
# The integer division operator (//) performs division but only keeps the integer (whole number) part of the result, discarding any fractional or decimal part.
# The modulus operator (%) in Python returns the remainder of a division operation.

dollars = cents // 100 # 1 dollar = 100 cents
cents = cents % 100 # Remaining cents after dollars

quarters = cents // 25 # 1 quarter = 25 cents
cents = cents % 25 # Remaining cents after quarters

dimes = cents // 10 # 1 dime = 10 cents
cents = cents % 10 # Remaining cents after dimes

nickels = cents // 5 # 1 nickel = 5 cents
cents = cents % 5 # Remaining cents after nickel

pennies = cents # Remaining cents are pennies

# Output the result
print(f"The total amount is: ${dollars} dollars, {quarters} quarters, {dimes} dimes, {nickels} nickels and {pennies} pennies")

# End

# Problem: Given a 9-digit unformatted student identification number, the task is to develop a Python solution 
# that formats this identification number into a specific format with hyphens inserted at specific positions.

# Task: Create a Python program that accepts a 9-digit unformatted student identification number 
# and outputs it as a formatted string with hyphens inserted in the required positions.


# Prompt the user for a 9-digit unformatted student identification number

try:
    # Input the student ID as a string to preserve leading zeros, if any
    student_id = input("Enter a 9-digit unformatted student ID: ")

    # Check if the input is exactly 9 digits and numeric
    if len(student_id) == 9 and student_id.isdigit():
        # Format the student ID with hyphens: 111-22-3333
        formatted_id = f"{student_id[:3]}-{student_id[3:5]}-{student_id[5:]}"
        print("Formatted Student ID:", formatted_id)
    else:
        print("Error: Please enter exactly 9 digits.")

except Exception as e:
    print("An error occurred:", str(e))

# End

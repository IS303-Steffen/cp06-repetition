import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# ================
# RANGE() PRACTICE
# ================

# 1. PRACTICE: USER SPECIFIED NUMBER OF LOOPS:
# Ask the user: "How many students do you want to enter? "
# Then, use a for loop to enter information for that number of students.

# at the beginning of each iteration of the loop, print out:
# "Enter information for student <x>" with x being 1, 2, 3, etc.
# then enter a name and gpa and print it out


num_students = int(input("How many students do you want to enter? "))

for student_num in range(1, num_students+1):
    print(f"Enter information for student {student_num}:")

    name = input("Enter the student name: ")
    
    gpa = float(input(f"Enter {name}'s GPA: "))
    
    print(f"{name} has a GPA of {gpa}")
    
print("Thank you")


# 2. PRACTICE: MANIPULATING NUMBERS
# Create a Python program that asks the user to enter an integer n.
# Then, use a for loop to print the results of 2 to the power of 1 to n.
'''
Example
If the user enters 5, your program should print:

2
4
8
16
32
'''

# Get input from the user
n = int(input("Enter an integer: "))

# Use a for loop to print the first n square numbers starting from 1
for i in range(1, n + 1):
    print(2 ** i)


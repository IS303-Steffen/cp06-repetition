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

# =====================
# BREAK & CONTINUE
# =====================

'''
OVERVIEW
--------
Break and continue are two control statements.
They apply to both while and for loops the same.

They will almost always be used in conjunction with an if statement.

- break:
    - instantly exit the loop

- continue:
    - stop the current iteration of the loop,
      but then go to the top of the loop and
      continue on with the next iteration of the loop.

'''

# 1. BREAK OUT OF A LOOP:
# Below I included the solution to the problem from 01_while_loops.py
# However, add logic so that if the user enters "QUIT" when it
# asks for a student name, it immediately gets out of the loop

answer = input("Do you want to enter a student name? ").upper()

while answer == "Y":
    full_name = input("Enter the student name: ")
    
    gpa = float(input(f"Enter {full_name}'s GPA: "))
    
    print(f"{full_name} has a GPA of {gpa}")
    
    answer = input("Do you want to enter another student name? ").upper()

print("Thank you")


# 2. SKIP AN ITERATION OF THE LOOP:
# Below I included the solution to the problem from 01_while_loops.py
# However, add logic so that if the user enters a gpa of 0 or below,
# it prints a message ("invalid GPA") and starts the loop over

answer = input("Do you want to enter a student name? ").upper()

while answer == "Y":
    full_name = input("Enter the student name: ")

    gpa = float(input(f"Enter {full_name}'s GPA: "))
        
    print(f"{full_name} has a GPA of {gpa}")
    
    answer = input("Do you want to enter another student name? ").upper()

print("Thank you")







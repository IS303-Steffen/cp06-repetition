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

# ============
# NESTED LOOPS
# ============

'''
OVERVIEW
--------
Just like with nested if statements, you can do nested loops.

Just be sure to indent with each nested loop.

TERMS TO KNOW
-------------

Outer loop:
    - the one the starts first.

Inner loop:
    - the one inside the other loop. You could have multiple layers of these.

When you get to the inner loop, that inner loop finishes looping through
everything before the next iteration of the outer loop starts.

EXAMPLE
-------  
for x in range(10):
    print(x)
    for y in range(5):
        print(y)
'''

# 1. OUTER AND INNER PRINT STATEMENTS
# Make an outer loop that prints out numbers 1 to 3 one at a time.
# Inside the outer loop, make an inner loop that prints out numbers
# 100 to 105 one at a time.
# When you print out the inner numbers, tab them over once
for outer_num in range(1, 4):
    print(outer_num)
    for inner_num in range(100, 106):
        print(f"\t{inner_num}")


# 2. GATHER MULTIPLE SUB INPUTS PER INPUT
# ask how many students to enter scores for
# then create a loop for the entered number and ask:
# "How many test scores to enter for student <x>"
# then create a loop for the number of tests for that student.
# Ask for test scores like this:
# "Enter a test score for Test X: "
# then print out "Student <outer x> scored <test score> on Test <inner x>" 

num_students = int(input("How many students to enter scores for? "))

for student in range(1, num_students +1):
    num_tests = int(input(f"How many test scores to enter "
                          f"for student {student}: "))

    for test in range(1, num_tests + 1):
        score = int(input(f"Enter a test score for test {test}: "))
        print(f"Student {student} scored {score} on test {test}")
    



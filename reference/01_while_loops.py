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

# =====
# LOOPS
# =====

'''
OVERVIEW
--------
Loops form the basis for tons of basic code. 

Two types:

while:
    - you provide a conditional statement. The loop repeats until
      the statement is false

for:
    - you provide an "iteratable" variable (like a range, a list,
      dictionary, etc.) and it loops for however many elements
      are in that variable.
    - Note that python structures for loops differently than most other
      programming languages.

We will start off with while loops
'''


'''
INFINITE LOOPS
--------------
while loops will run until the condition you provide turns false.
If it never becomes false, it will run FOREVER!!!!

You never want to do this, but run the example below just so you
can recognize what it looks like for when you accidentally do it.

If you click in the terminal and press ctrl + c, it'll terminate the code.
you could also click the trash can in the terminal window
'''

# 1. SEE EXAMPLE OF INFINITE LOOP:
# Uncomment the code below and run it.

# while True:
#     print("this")
#     print("was")
#     print("a")
#     print("bad")
#     print("idea")

'''
STRUCTURE OF WHILE LOOPS
------------------------
You can think of while loops as "if statements" that keep repeating as
long as the condition listed is true.

The trick is to think of a condition that can eventually become False.

EXAMPLE
-------
x = 5
while x < 10:
    print(x)
    x += 1

'''


# 2. CONTINUALLY GATHER STUDENT DATA:
# Ask the user: "Do you want to enter a student name? (enter Y or N): "
# While the answer is "Y":
# ask the user to enter a name, then to enter a GPA,
# and then print out the student's name and GPA
# then ask, if they want to enter another student's name (enter Y or N)
# when they are done entering student info, print "Finished, thank you."
student_answer = input("Do you want to enter a student name? "
                       "(enter Y or N): ").upper()

while student_answer == "Y":
    student_name = input("Enter the student name: ")
    
    student_gpa = float(input(f"Enter {student_name}'s GPA: "))
    
    print(f"{student_name} has a GPA of {student_gpa}")
    
    # THIS PART IS IMPORTANT, we're giving a chance for the loop to end
    student_answer = input("Do you want to enter a student name? "
                           "(enter Y or N): ").upper()

print("Finished, thank you")


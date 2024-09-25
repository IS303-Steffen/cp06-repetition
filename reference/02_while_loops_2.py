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
# WHILE LOOPS CONTINUED
# =====================

'''
OVERVIEW
--------
In the last file we stopped the loop when a value was changed.

Here we can try to run a while loop for a specific number of times.
'''


# 1. CONTINUALLY GATHER STUDENT DATA:
# Do the same thing as the last practice, (feel free to copy and paste and 
# then edit it), but at the start, change it to ask:
# "How many students do you want to enter? "
# then enter a name and gpa and print it out, but don't
# repeatedly ask if they want to enter another student
# just automatically end it once the number they initially entered is reached.

# Hint: this means you need to keep track of how many times the loop has run.
# How could you do that?

counter = 0
num_students = int(input("How many students to enter? "))

while counter < num_students:
    print(f"this is the current loop {counter + 1}")
    full_name = input("Enter the student name: ")
    
    gpa = float(input(f"Enter {full_name}'s GPA: "))
    
    print(f"{full_name} has a GPA of {gpa}")
    
    counter += 1  # this is a shorthand for counter = counter + 1
    
print("Thank you")






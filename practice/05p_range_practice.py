# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

#######
# range
#######

# Practice:

'''
Ask the user: "How many students do you want to enter? "
Then, use a for loop to enter information for that number of students.

at the beginning of each iteration of the loop, print out:
  "Enter information for student x" with x being 1, 2, 3, etc.
then enter a name and gpa and print it out
'''




# Practice:
'''
    Create a Python program that asks the user to enter an integer n. Then, use a for loop to print the first n square numbers starting from 1.

    Example
    If the user enters 5, your program should print:

    1
    4
    9
    16
    25
'''




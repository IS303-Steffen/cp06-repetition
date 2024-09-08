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


# Nested Loops:

'''
Just like with nested if statements, you can do nested loops. 

Just be sure to indent with each nested loop.

'''

# Practice 
# ask how many students to enter scores for
# then loop through each student and ask:
#       "How many test scores to enter for student x"
# then loop and enter in a test score like this:
#       "Enter a test score for Test X: "
#       then print out "Student X scored X on Test X" 


    
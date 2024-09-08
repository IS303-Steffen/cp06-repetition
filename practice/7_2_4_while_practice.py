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

# Practice:
'''
    prompt the user to enter numbers until they enter the number 0.
    After entering `0`, the program should display the sum of all numbers entered.

    Try doing this without using break
'''


# Practice:
'''
    Do the same thing, but use break
'''

# Practice:
'''
    Do the same thing, but only add up a number if it is odd.
    If it is even, print out "even number, won't add this
'''







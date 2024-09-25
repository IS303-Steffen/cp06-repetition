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

# ====================
# WHILE LOOPS PRACTICE
# ====================


# 1. PRACTICE: WHILE WITHOUT BREAK 
# Prompt the user to enter numbers until they enter the number 0.
# After entering 0, the program should display the sum of all numbers entered.
# Do this without using break


# 2. PRACTICE: WHILE WITH BREAK 
# Do the same as in Practice #1, but use break


# 3. PRACTICE: WHILE WITH CONTINUE
# Do the same as in Practice #1 or #2, but only add up a number if
# it is odd. Use continue to do accomplish this (even though there
# are other ways you could easily do it)

# Hint: An easy way to check if a number is even or odd is to use modulus %
# Google or use AI if you fogot how % works in python.


'''
SHOULD YOU USE BREAK?
---------------------

Often, coders will suggest not using break, because it isn't
very clear from the top of the loop, what the purpose of the loop is,
or how it will eventually terminate.

I personally think it is ok if you comment your code well and if the loop
is pretty short. Otherwise I might prefer just writing a condition that
will become false.
'''





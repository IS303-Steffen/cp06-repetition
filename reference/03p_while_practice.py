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

current_sum = 0
current_number = None #arbitrary value 

while current_number != 0:
    current_number = int(input("please enter a number: "))
    current_sum = current_sum + current_number
    # you could also use the += shortcut

print("Total Sum:", current_sum)

# 2. PRACTICE: WHILE WITH BREAK 
# Do the same as in Practice #1, but use break
current_sum = 0
while True:
    current_number = int(input("please enter a number: "))
    if current_number == 0:
        break
    current_sum = current_sum + current_number

print("Total Sum:", current_sum)


# 3. PRACTICE: WHILE WITH CONTINUE
# Do the same as in Practice #1 or #2, but only add up a number if
# it is odd. Use continue to do accomplish this (even though there
# are other ways you could easily do it)

# Hint: An easy way to check if a number is even or odd is to use modulus %
# Google or use AI if you fogot how % works in python.

current_sum = 0
while True:
    current_number = int(input("please enter a number: "))
    if current_number == 0:
        break
    
    if current_number % 2 == 0:
        print("even number, won't add this.")
        continue
    current_sum = current_sum + current_number

print("Total Sum:", current_sum)






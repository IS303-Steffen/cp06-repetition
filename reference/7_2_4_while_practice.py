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
currentSum = 0
currentNumber = 23456 #arbitrary value

while currentNumber != 0:
    currentNumber = int(input("please enter a number: "))
    currentSum = currentSum + currentNumber

print("current Sum:", currentSum)

# Practice:
'''
    Do the same thing, but use break
'''
currentSum = 0
while True:
    currentNumber = int(input("please enter a number: "))
    if currentNumber == 0:
        break
    currentSum = currentSum + currentNumber

print("current Sum:", currentSum)

# Practice:
'''
    Do the same thing, but only add up a number if it is odd.
    If it is even, print out "even number, won't add this
'''
currentSum = 0
while True:
    currentNumber = int(input("please enter a number: "))
    if currentNumber == 0:
        break
    
    if currentNumber % 2 == 0:
        print("even number, won't add this.")
    else:
        currentSum = currentSum + currentNumber

print("current Sum:", currentSum)






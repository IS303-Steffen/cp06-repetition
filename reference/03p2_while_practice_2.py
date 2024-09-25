# optional stuff that will clear the window each time you run it.
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


# 1. PRACTICE: COMBINING DATA STRUCTURES WITH LOOPS
# Repeatedly ask the user:
# "Enter in a name of a friend. To stop enter STOP: "
# Store each name in a list
# Do this until they enter "STOP"

# After they enter "STOP", in a separate loop, ask the user:
# "Enter in the number of a friend in the list to see their name.
#  Enter 0 to exit: "

# E.g. if they enter 1, show them the first friend in the list,
# if they enter 3, show them the 3rd member of the list.
# do this until they enter 0 to exit.

# You can do this without using break, or with it, whatever you prefer

# CHALLENGE: Make it so that if they enter a number longer than
# the number of names in the list, it
# prints out "Invalid number, you only have X friends in the list" and doesn't
# throw an error. You might find the len() function good at this.



friend_list = []

while True:
    friend_name = input("Enter in a name of a friend. To stop enter STOP: ")
    if friend_name == "STOP":
        break
    else:
        friend_list.append(friend_name)


while True:
    friend_number = int(input("Enter in the number of a friend in the list "
                              "to see their name. Enter 0 to exit: "))
    
    if friend_number == 0:
        break
    elif friend_number <= len(friend_list):
        print(friend_list[friend_number -1])
    else:
        print(f"Invalid number, you only have "
              f"{len(friend_list)} friends in the list")



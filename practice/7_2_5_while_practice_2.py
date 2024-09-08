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
Repeatedly ask the user:
    "Enter in a name of a friend. To stop enter STOP: "
Store each name in a list
Do this until they enter "STOP"

After they enter "STOP", in a separate loop, ask the user:
    ""Enter in the number of a friend in the list to see their name. Enter 0 to exit: ""

E.g. if they enter 1, show them the first friend in the list, if they enter 3, show them the 3rd member of the list.
do this until they enter 0 to exit.

BONUS IF WE HAVE TIME: Make it so that if they enter a number longer than the number of names in the list, it
prints out "Invalid number, you only have X friends in the list" and doesn't throw an error. You might find the len() function good at this.
'''




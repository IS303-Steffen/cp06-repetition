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


# Practice
'''
Given the schedule dictionary below:
print out each day of the week, and then below each day,
print each class that occurs on that day, tabbed out from the day of the week:
    E.g.:
    Monday:
        Math
        Science

after each day's classes, print an extra blank line so it looks nicer.

remember that with a dicitonary, you can get the keys and values by using dictionary_variable.items()

'''


schedule = {
    "Monday": ["Math", "Science"],
    "Tuesday": ["English", "History", "Art"],
    "Wednesday": ["Math", "Science", "PE"],
    "Thursday": ["English", "Art"],
    "Friday": ["Math", "History", "Science", "PE"]
}

for key_day, value_subject_list in schedule.items():
    print(f"{key_day}:")
    for subject in value_subject_list:
        print(f"\t{subject}")
    print()

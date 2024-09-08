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

'''
    range() is a function that creates a range object.
    Think of it as a datatype whose only purpose (or at least primary purpose)
    Is to create an iterable of a certain length to loop through.

    Like "I know I want to loop 5 times. let me just make a range object of 5"


'''

# Practice:
# Use range(5) and a for loop to print out
# "This will repeat 5 times":

for _ in range(5):
    print("this will repeat 5 times")


'''
Notice we didn't use the looping variable in the previous example?
You can name it anything you want, but convention, is if you 
don't reference the looping variable inside the loop, you can name it as an underscore
this is just an easy way to show you arent' using it.
'''
# Practice:
# But now, lets use the looping variable with range()
# print out "This is loop #: 0" and then 2, 3, etc. up to 4

for range_num in range(5):
    print(f"This is loop #: {range_num}")


'''
    What if you want the range to start at 1, not 0?

    range(stopping point).  Note it stops before it reaches the stopping point.
    range(starting point, stopping point)
    range(starting point, stopping point, step value)
'''

# Let's practice using starting points, stopping points, and step values.

# Practice:
# print "This is loop #: " from 1 to 5
for range_num in range(1, 6):
    print(f"This is loop #: {range_num}")


# Practice:
# print "This is loop #: " from 0 to 10, but in increments of 2, so 0, 2, 4, etc.
for range_num in range(0, 11, 2):
    print(f"This is loop #: {range_num}")


# Practice
# # print "This is loop #: " from 10 to -10, in increments of -2, so 10, 8, 6, etc.
for range_num in range(10, -11, -2):
    print(f"This is loop #: {range_num}")



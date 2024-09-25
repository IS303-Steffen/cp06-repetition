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

# =======
# RANGE()
# =======

'''
OVERVIEW
--------
range() is a function that creates a range object.
Think of it as a datatype whose only purpose (or at least primary purpose)
Is to create an iterable of a certain length to loop through.

For example:
"I know I want to loop 5 times. let me just make a range object of 5"


EXAMPLE
-------  
for x in range(10):
    print(x)
'''


# 1. LOOPING X TIMES
# Use range(5) and a for loop to print out "This will repeat 5 times" 5 times

for _ in range(5):
    print("this will repeat 5 times")

'''
Notice we didn't use the looping variable in the previous example?
You can name it anything you want, but conventionally, if you 
don't reference the looping variable inside the loop,
you can name it as an underscore "_"
this is just an easy way to show you don't use that variable.
'''

# 2. LOOPING X TIMES, PRINTING THE LOOPING VARIABLE
# Now run the loop 5 times, but print out the looping variable
# print out "This is loop #: 0" and then 2, 3, etc. up to 4

for range_num in range(5):
    print(f"This is loop #: {range_num}")

'''
ADDITIONAL PARAMETERS FOR RANGE()
---------------------------------
What if you want the range to start at 1, not 0?

range(<stopping point>)
    - what we've already been using
    - Note it stops before it reaches the stopping point.
      because it starts at zero

range(<starting point>, <stopping point>)
    - Useful if you want to start counting at 1

range(<starting point>, <stopping point>, <step value>)
    - Allows you to do stuff like every other number, every 3rd number, etc.
'''

# 3. LOOP 5 TIMES, STARTING AT 1
# Print "This is loop #: " from 1 to 5 using range()
for range_num in range(1, 6):
    print(f"This is loop #: {range_num}")


# 4. LOOP 5 TIMES, STARTING AT 1
# Print "This is loop #: " from 0 to 10,
# but in increments of 2, so 0, 2, 4, etc.
for range_num in range(0, 11, 2):
    print(f"This is loop #: {range_num}")

# 5. LOOP INTO THE NEGATIVES
# Print "This is loop #: " from 10 to -10, in increments of -2,
# so 10, 8, 6, etc.
for range_num in range(10, -11, -2):
    print(f"This is loop #: {range_num}")

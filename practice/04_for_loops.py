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

# =========
# FOR LOOPS
# =========

'''
OVERVIEW
--------
For loops are useful in two main situations:

1. With iterable variables (like data structures)
- You have an iterable variable (list, dictionary, range, string, etc.)
  and you want to repeat code for each thing  in that iterable variable.
- An iterable just means a variable that you can "iterate" or step/loop through
  one by one. In most cases, they are just data structures.

2. Doing something for exactly X number of times
- You usually would use a range variable to do that.
- While loops work well for this too, but most people would proably use a for
  loop

EXAMPLE
-------  
iterable_variable = ["example_1", "example_2", "example_3"]

for looping_variable in iterable_variable:
    print(looping_variable)

TERMS TO KNOW
-------------
iterator variable:
    - The variable that has lots of things inside it to step through

looping variable:
    - you make this variable name up on the spot.
      It will represent every individual element in the iterator variable
'''


# 1. UNDERSTANDING THE LOOPING VARIABLE
# given a list of names, for each name,
# print out "This is the character's name: " and then the character's name
example_list = ["Harry", "Hermione", "Ronald", "Luna"]


# 2. LOOPING WITH DICTIONARIES
# Practice:
# given a dictionary, write:
# a for loop that prints out just the keys (default)
# a for loop that prints out just the values (use .values())
# a for loop that prints out the keys and values (use .items())
# Hint: for .items(), do you remember how unpacking works?

grade_dict = {"A": 4.0, "A-": 3.7, "B+": 3.4, "B": 3.0}


# 3. LOOPING WITH STRINGS
# print out each individual character
# in the word "Supercalifragilisticexpialidocious"
'''
strings are iterables too!
not very common to loop through, but you can do it.
'''







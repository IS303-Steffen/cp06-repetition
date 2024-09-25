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

# =============================
# TO USE OR NOT TO USE RANGE()?
# =============================

'''
OVERVIEW
--------
Many people that come from other coding languages tend to write out
for loops to iterate through lists using range.

This works just fine, but isn't very "pythonic"

See the examples below.
'''

example_list = ["Thurston Moore", "Kim Gordon", "Lee Ranaldo", "Steve Shelley"]

# 1. LOOPING THROUGH A LIST USING RANGE() AND AN INDEX
'''
This way you access the individual items in the list by their index
You know how long the list is by using len()
'''
for index in range(len(example_list)):
    print(example_list[index])


# 2. DIRECTLY LOOPING THROUGH THE LIST
'''
This way you directly access the individual elements in list and put them
into the looping variable ("name" in this case) one by one.

This structure is quite unique to Python. I personally love it.
'''
for name in example_list:
    print(name)


'''
WHICH TO USE?
-------------

I prefer the 2nd way (the more "pythonic" way),
but either will work.

Your textbook occasionally uses the first way, likely because
the textbook was originally written for Java, and the first way
is closer to what you might do in Java, C#, etc.
'''
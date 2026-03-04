from helper_functions import clear_screen
clear_screen()

# ====================
# LIST COMPREHENSIONS
# ====================

'''
OVERVIEW
--------
A list comprehension is a compact way to build a list.

It is essentially a for loop that:
1. Loops through some data
2. Applies logic or transformations
3. Stores the result in a list

List comprehensions are NOT required to write Python,
but they are very common in real-world code.

Anything you can do with a list comprehension,
you can also do with a normal for loop.
'''


# ------------------------
# TRADITIONAL FOR LOOP
# ------------------------
# First, let's remind ourselves how we normally build a list

numbers = []

for x in range(5):
    numbers.append(x)

print(numbers)


'''
The code above:
- Starts with an empty list
- Loops 5 times
- Adds each number to the list

List comprehensions just compress this idea
into a single line.
'''


# ------------------------
# BASIC LIST COMPREHENSION
# ------------------------
# Same result as above, written as a list comprehension

numbers = [x for x in range(5)]
print(numbers)


'''
GENERAL STRUCTURE
-----------------
[ <what you want to store>  for <loop variable> in <iterable> ]

Read it as:
"Give me a list of ____ for each ____ in ____"
'''


# 1. CREATING A LIST OF NUMBERS
# Create a list that contains the numbers 0 through 9



# 2. MODIFYING VALUES
# Create a list that contains the squares of numbers 0 through 4
# e.g. the end result should be (0, 1, 4, 9, 16)



'''
List comprehensions are often used in business contexts
to transform data, such as:
- Prices with tax added
- Sales totals
- Adjusted scores
'''


# 3. BUSINESS EXAMPLE
# Add a 10% tax to each price

prices = [10, 25, 40, 100]



# ------------------------
# ADDING CONDITIONS
# ------------------------
# List comprehensions can include conditions (if statements)

'''
STRUCTURE WITH A CONDITION
--------------------------
[ <value> for <item> in <iterable> if <condition> ]
'''


# 4. FILTERING DATA
# Create a list of only the prices over $30




# 5. COMBINING LOGIC AND TRANSFORMATION
# Take only prices over $30 and add tax to them

prices_over_30_with_tax = [price * 1.10 for price in prices if price > 30]
print(prices_over_30_with_tax)


'''
KEY TAKEAWAYS
-------------
- List comprehensions are a shortcut, not a requirement
- They replace simple for-loops that build lists
- They are commonly used for:
  - Cleaning data
  - Transforming values
  - Filtering lists

If a list comprehension ever feels confusing, you can always just write out a
regular for loop instead.
'''
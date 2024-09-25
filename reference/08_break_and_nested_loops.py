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

# ======================
# BREAK AND NESTED LOOPS
# ======================

'''
OVERVIEW
--------
When working with nested loops, it is important to remember that
break (and continue) will only affect the loop it is used in.

So if you break out of an inner loop, you will still be in the outer loop
'''

# 1. BREAKING OUT OF AN INNER LOOP
# Given the dictionary below, loop through each restaurant and print out
# its name. Then print out each item on the menu of each restaurant.
# however, you absolutely hate Onion rings. So if you print out "Onion rings"
# immediately print "I refuse to eat here!" and stop printing out the rest
# of that restaurant's menu. But continue to the next restaurant.


restaurants_dict = {
    "Burger King": ["Whopper", "Chicken Fries", "French Fries", "Onion rings", "Soft Drinks"],
    "Jack in the Box": ["Tacos", "Onion rings", "Burgers", "Chicken Nuggets", "Curly Fries"],
    "McDonald's": ["Big Mac", "Chicken McNuggets", "French Fries", "McFlurry", "Filet-O-Fish"],
    "Taco Bell": ["Crunchwrap Supreme", "Burrito", "Nachos", "Quesadilla", "Chalupa"],
    "Sonic Drive-In": ["Burgers", "Hot Dogs", "Milkshakes", "Onion rings", "Tater Tots"],
}

for restaurant, menu in restaurants_dict.items():
    print(restaurant)
    for item in menu:
        print(f"\t{item}")
        if item == "Onion rings":
            print("I refuse to eat here!")
            break
    print()
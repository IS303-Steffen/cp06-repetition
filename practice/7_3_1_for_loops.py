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


# for loops

'''
Useful in two main situations:
    - You have an iterable variable (list, dictionary, range, string, etc. An iterable just means a variable with other variables inside it)
      and you want to repeat code for however many things are in that iterable variable

    - You want to repeat something x times. Like "do this 5 times". You usually would use a range variable to do that.

'''
# structure of for loops:
'''
    for looping_variable in iterable_variable:
        code that will repeat

    for:
        always there

    looping_variable:
        you make this variable name up on the spot. It will represent every individual element in the iterable_variable
        sometimes called the iterator variable

    iterable_variable:
        this is the range, list, etc that you want to loop through
'''

# Practice:
# given a list of names, for each name,
# print out "This is the character's name: " and then the character's name

example_list = ["Harry", "Hermione", "Ronald", "Luna"]



# Practice:
# given a dictionary, do:
    # a for loop that prints out just the keys (default)
    # a for loop that prints out just the values (use .values(), or put the keys back in the dictionary)
    # a for loop that prints out the keys and values (use .items())

grade_dict = {"A": 4.0, "A-": 3.7, "B+": 3.4, "B": 3.0}

# just the keys:


# just the values:



# keys and values (remember unpacking?):



# strings are iterables too!
# not as common to loop through, but you can:

# practice: 
# print out each individual character in the word "Supercalifragilisticexpialidocious"
poppins_word = "Supercalifragilisticexpialidocious"







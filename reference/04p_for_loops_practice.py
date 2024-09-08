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
You are provided with two lists of first names: friends_of_X and friends_of_Y.
Each list contains about 15 names, and there is some overlap between the lists.

Write a Python program that loops through the list of Person X's friends.

For each friend in Person X's list, the program should print the friend's name.

If the friend is also in Person Y's list, print " - Mutual friend with Person Y!" after their name.
'''

# Sample lists of friends
friends_of_X = ["Alice", "Bob", "Charlie", "David", "Emma", "Fiona", "George", "Hannah", "Isla", "Jack", "Katie", "Liam", "Mia", "Noah", "Olivia"]
friends_of_Y = ["Brad", "Charlie", "Daisy", "Emma", "Fiona", "George", "Henry", "Isla", "Jane", "Katie", "Liam", "Mike", "Nina", "Olivia", "Peter"]

# Loop through each friend of Person X
for friend in friends_of_X:
   
    mutual_friend = '' # set this to be empty each iteration
    if friend in friends_of_Y: # add the extra message only if the friend is inside of person Y's list
        mutual_friend = " - Mutual friend with Person Y!"

    print(friend + mutual_friend)





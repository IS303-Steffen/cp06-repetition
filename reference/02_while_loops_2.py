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


# LOOPS
'''
Loops form the basis for tons of basic code. 

Two types:

    - while: you provide a conditional statement. The loop repeats until the statement is false

    - for: you provide an "iteratable" variable (like a range, a list, dictionary, etc.) and it
           loops for however many elements are in that variable.
           Note that this is different than most other programming languages. 

'''

# Practice:
# Do the same thing as the last practice, but instead, ask at first:
# "How many students do you want to enter? "
# then enter a name and gpa and print it out, but don't repeatedly ask if they want to enter another student
# just automatically end it once the number they initially entered is reached.

# Hint: this means you need to keep track of how many times the loop has run. How could you do that?

counter = 0
num_students = int(input("How many students to enter? "))

while counter < num_students:
    print(f"this is the current loop {counter + 1}")
    full_name = input("Enter the student name: ")
    
    gpa = float(input(f"Enter {full_name}'s GPA: "))
    
    print(f"{full_name} has a GPA of {gpa}")
    
    counter += 1  # this is a shorthand for counter = counter + 1
    
print("Thank you")






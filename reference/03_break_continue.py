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

# Break and continue
'''
Break and continue are two control statements. They apply to while and for loops the same.
They will almost always be used in conjunction with an if statement.

Two types:

    - break: instantly exit the loop

    - continue: stop the current iteration of the loop, but then continue on with the next iteration of the loop.

'''


# break
# this will make you exit the loop immediately, continue on with anything after the loop


# Practice:
# do the same thing from 7_2_1 (Ask if you want to enter a student name, etc.)
# but inside the while loop, if they enter "QUIT", immediately exit the loop

answer = input("Do you want to enter a student name? ").upper()

while answer == "Y":
    full_name = input("Enter the student name: ")
    if full_name.upper() == "QUIT":
        # HERE IS THE BREAK
        break
        
    gpa = float(input(f"Enter {full_name}'s GPA: "))
    
    print(f"{full_name} has a GPA of {gpa}")
    
    answer = input("Do you want to enter a student name? ").upper()

print("Thank you")



# continue
# Do the same as the above, but if the user enters 0 for the GPA, 
# then use a continue statement to start the iteration of the loop over.

answer = input("Do you want to enter a student name? ").upper()

while answer == "Y":
    full_name = input("Enter the student name: ")
    gpa = float(input(f"Enter {full_name}'s GPA: "))
    
    if gpa == 0:
        # HERE IS THE CONTINUE
        continue
        
    print(f"{full_name} has a GPA of {gpa}")
    answer = input("Do you want to enter a student name? ").upper()

print("Thank you")







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

# NEVER ENDING LOOPS
'''
You can uncomment the below code for fun.
Note: you can highlight the text and use ctrl + / (windows) or cmd + / to comment or uncomment things in bulk

while loops will run until the condition you provide turns false.
If it never becomes false, it will run FOREVER!!!!

if you click in the terminal and press ctrl + c, it'll terminate the code.
you could also click the trash can in the terminal window
'''

# while True:
#     print("this")
#     print("was")
#     print("a")
#     print("bad")
#     print("idea")
   
# Let's try something more useful:

# Practice:
# Ask the user: "Do you want to enter a student name? (enter Y or N): "
# While the answer is "Y":
# ask the user to enter a name, then to enter a GPA, and then print out the student's name and GPA
# then ask, if they want to enter another student's name (enter Y or N)
# when they are done entering student info, print "Finished, thank you."
student_answer = input("Do you want to enter a student name? (enter Y or N): ").upper()

while student_answer == "Y":
    student_name = input("Enter the student name: ")
    
    student_gpa = float(input(f"Enter {student_name}'s GPA: "))
    
    print(f"{student_name} has a GPA of {student_gpa}")
    
    # THIS PART IS IMPORTANT, we're giving a chance for the loop to end
    student_answer = input("Do you want to enter a student name? (enter Y or N): ").upper()

print("Finished, thank you")


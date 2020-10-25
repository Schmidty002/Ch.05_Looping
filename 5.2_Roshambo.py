'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

import random

game = True

uscore = 0
cscore = 0
nilscore = 0

while game:
    computer = random.randrange(1,4)
    print("What would you like to do?\n")
    print("If rock, enter 1\nIf paper, enter 2\nIf scissors, enter 3\nIf view score, enter 4\nIf quit, enter 0")
    print()
    user = input()
    if user == "1" or user == "2" or user == "3" or user == "4" or user == "0":     #filters invalid answers
        user = int(user)
    else:
        print("Invalid Answer\n")
        continue1
    if user == 1:                           #Sets user's choice
        print("User: Rock")
    elif user == 2:
        print("User: Paper")
    elif user == 3:
        print("User: Scissors")
    elif user == 4:                             #Checks score
        print("User:",uscore)
        print("Computer:",cscore)
        print("Ties:",nilscore)
        print()
    elif user == 0:                             #Exits game
        print("Exiting game...")
        game = False
    if user == 1 or user == 2 or user == 3:
        if computer == 1:                       #Sets computer's choice
            print("Computer: Rock\n")
        elif computer == 2:
            print("Computer: Paper\n")
        else:
            print("Computer: Scissors\n")
        if user == computer:                    #Determines match results and adjusts score
            print("Tie\n")
            nilscore += 1
        elif user == 1 and computer == 2:
            print("You Lost\n")
            cscore += 1
        elif user == 1 and computer == 3:
            print("You Won!\n")
            uscore += 1
        elif user == 2 and computer == 1:
            print("You Won!\n")
            uscore += 1
        elif user == 2 and computer == 3:
            print("You Lost\n")
            cscore += 1
        elif user == 3 and computer == 1:
            print("You Lost\n")
            cscore += 1
        elif user == 3 and computer == 2:
            print("You Won!\n")
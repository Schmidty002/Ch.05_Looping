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

while game:
    user = random.randrange(1,4)
    computer = random.randrange(1,4)
    uscore = 0
    cscore = 0
    nilscore = 0
    if user == 1:
        print("User: Rock")
    elif user == 2:
        print("User: Paper")
    else:
        print("User: Scissors")
    if computer == 1:
        print("Computer: Rock")
    elif computer == 2:
        print("Computer: Paper")
    else:
        print("Computer: Scissors")
    if user == computer:
        print("Tie")
        nilscore += 1
    elif user == 1 and computer == 2:
        print("You Lost")
        cscore += 1
    elif user == 1 and computer == 3:
        print("You Win!")
        uscore += 1
    elif user == 2 and computer == 1:
        print("You Win!")
        uscore += 1
    elif user == 2 and computer == 3:
        print("You Lose")
        cscore += 1
    elif user == 3 and computer == 1:
        print("You Lose")
        cscore += 1
    elif user == 3 and computer == 2:
        print("You Win!")
    else:
        print("come again?")

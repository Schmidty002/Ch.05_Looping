'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''

import random
global heads,tails
heads = 0
tails = 0
for i in range(50):
    if random.randrange(0,2) == 0:
        print("Heads")
        heads += 1
    else:
        print("Tails")
        tails += 1
print("Total heads:",heads)
print("Total tails:",tails)
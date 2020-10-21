  #Sign your name:________________

'''
 1. Make the following program work.
   '''  
     # print("This program takes three numbers and returns the sum.")
     # total = 0
     #
     # for i in range(3):
     #     x = input("Enter a number: ")
     #     total = total + i
     # print("The total is:", x)
  
print("This program takes three numbers and returns the sum.")
total = 0
for i in range(3):
    x = int(input("Enter a number: "))
    total += x
print("The total is:",total)

'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''

for i in range(2,101):
    if i%2==0:
        print(i)



'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''

x = 10
while x >= 0:
    print(x)
    x -= 1
print("Blast off!")




'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
print(random.randrange(0,11))





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
print("Today I'll be asking you for seven numbers.")
global sum,pos,neg,nil
sum = 0
pos = 0
neg = 0
nil = 0
for i in range(7):
    num = int(input("Number: "))
    sum += num
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        nil += 1
print("Sum:",sum)
print("No. of positive answers:",pos)
print("No. of negative answers:",neg)
print("No. of zeroes entered:",nil)

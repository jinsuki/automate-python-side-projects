# collatzNum.py - Finds the collatz number of any number
# The program seeks to return 1 from any integer by either dividing
# or multiplying it by 3 and adding 1 to it until it can divide to 1.

import sys

def collatzFind(number): 
    if number == 1: # breaks recursion if collatz found
        sys.exit()
    elif number % 2 == 0: # checks to see if even, if so divide by 2 and repeat
        number = number / 2
        print(int(number))
        collatzFind(number)
    else: # checks to see if odd, if so 3 * num + 1 and repeat 
        number = (3 * number) + 1
        print(int(number))
        collatzFind(number)

print('Please enter a number')
try: #try-catch block to prevent noninteger values
    userInput = int(input())
except ValueError:
    print('non-integer value detected, please try again')

collatzFind(userInput)

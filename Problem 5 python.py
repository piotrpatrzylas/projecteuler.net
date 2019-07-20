# =============================================================================
# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 
# =============================================================================
from math import factorial

def checkDiv(number):
    for i in range(20, 10, -1):
        if (number % i != 0):
            return False
    return True

maximum = factorial(20)
counter = 232792540

while counter <= maximum:
    if checkDiv(counter):
        print ("Your number is: ", counter)
        break
    else:
        counter += 1
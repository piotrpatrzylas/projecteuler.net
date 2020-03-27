# =============================================================================
# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# =============================================================================

def isPrime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    else:
        return True

def largePrime(n):
    counter = 0
    number = 2
    result = 0
    while counter != n:
        if isPrime(number):
            result = number
            counter += 1
            number += 1
        else:
            number += 1
    return result

largePrime(10001)
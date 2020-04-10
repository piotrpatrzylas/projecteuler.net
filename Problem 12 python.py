# =============================================================================
# Highly divisible triangular number
# Problem 12
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number
# would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?
# =============================================================================
from math import ceil

def triangular(n):
    t_number = 1
    for i in range(2, n+1):
        t_number += i
    return t_number


def get_divisors(n):
    val = 1
    for i in range(1, ceil(n/2)+1):
        if n % i == 0:
            val += 1
    return val


def check_t(n_div):
    t_number = 1
    while True:
        t_value = triangular(t_number)
        if get_divisors(t_value) > n_div:
            return t_value
        else:
            t_number += 1

print(check_t(500))



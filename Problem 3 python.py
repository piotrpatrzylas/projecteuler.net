# =============================================================================
#  Largest prime factor
#  Problem 3
#  The prime factors of 13195 are 5, 7, 13 and 29.
#  What is the largest prime factor of the number 600851475143 ?
# =============================================================================

import math
large_number = 600851475143
for x in range(2,math.floor(math.sqrt(large_number))):
    if large_number % x == 0:
        print(x)
        large_number /= x
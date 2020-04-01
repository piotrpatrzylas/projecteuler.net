# =============================================================================
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# =============================================================================

def sumofprimes(n):
    sieve = []
    prime = []
    for i in range(2, n+1):
        if i not in sieve:
            prime += [i]
            for j in range(i*i, n+1, i):
                sieve.append(j)
    results = 0
    for i in prime:
        results += i
    return results
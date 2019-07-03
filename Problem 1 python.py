# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# 1. Long
results = 0
for n in range(1,1000):
    if ((n % 3 == 0) or (n % 5 == 0)):
        results = results + n
print (results)

# 2. List comprehension

results2 = sum([ x for x in range(1000) if ((x % 3 == 0) or (x % 5 == 0))])

results == results2
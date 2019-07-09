  # Largest prime factor
  # Problem 3
  # The prime factors of 13195 are 5, 7, 13 and 29.
  # What is the largest prime factor of the number 600851475143 ?

long_number = 600851475143

# Sieve of Eratosthenes from https://stackoverflow.com/questions/3789968/generate-a-list-of-primes-up-to-a-certain-number?noredirect=1&lq=1
sieve <- function(n)
{
  n <- as.integer(n)
  if(n > 1e6) stop("n too large")
  primes <- rep(TRUE, n)
  primes[1] <- FALSE
  last.prime <- 2L
  for(i in last.prime:floor(sqrt(n)))
  {
    primes[seq.int(2L*last.prime, n, last.prime)] <- FALSE
    last.prime <- last.prime + min(which(primes[(last.prime+1):n]))
  }
  which(primes)
}
# generate list with all primes till 10000
prime_list = sieve(10000)
res_list = list()

find_primes = function (prime_list) {
  
  for (num in c(1:length(prime_list))) {
    if (long_number %% prime_list[num] == 0) {
      print (prime_list[num])
      res_list = c(res_list, prime_list[num])}}
return (res_list)
}
results = find_primes(prime_list)
indice = which.max(results)

#print results
print(results[indice])
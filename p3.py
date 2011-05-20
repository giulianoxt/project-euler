from math import sqrt, ceil

N = 600851475143
lim = int(ceil(sqrt(N)))

def primes(max_prime):
  sieve = [True] * (max_prime+1)
  for i in xrange(2, max_prime+1):
    if sieve[i]:
      yield i
      for j in xrange(i+i, max_prime+1, i):
        sieve[j] = False

print [p for p in primes(lim) if not N % p][-1]


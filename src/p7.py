def primes(max_prime):
  sieve = [True] * (max_prime+1)
  for i in xrange(2, max_prime+1):
    if sieve[i]:
      yield i
      for j in xrange(i+i, max_prime+1, i):
        sieve[j] = False

def is_prime(n):
  if n == 1: return False
  if n < 4: return True
  if not n % 2: return False
  if n < 9: return True
  if not n % 3: return False
  
  from math import sqrt, floor

  r = floor(sqrt(n))
  f = 5

  while f <= r:
    if not (n % f and n % (f+2)): return False
    f += 6
  
  return True


from math import ceil, sqrt

def primes(max_prime):
  L = max_prime+1
  sieve = [True] * L
  yield 2
  for i in xrange(3, L, 2):
    if sieve[i]:
      yield i
      i2 = i*i
      if i2 < L:
        for j in xrange(i2, L, 2*i):
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


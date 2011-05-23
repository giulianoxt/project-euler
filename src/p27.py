from euler import *
from itertools import count

m = 40
m_prod = 1 * 41

for b in primes(1000):
  for a in xrange(1-b, 1001):
    cnt = 1
    for n in count(1):
      x = n*n + a*n + b
      if is_prime(x):
        cnt += 1
      else:
        break
    
    if cnt > m:
      m = cnt
      m_prod = a*b

print m_prod


from math import *
from euler import *

res = 0
prime_s = set(primes(1000000))
for p in prime_s:
  nd = int(ceil(log10(p)))
  p_10 = 10**(nd-1)

  for _ in xrange(nd-1):
     p = (p/10) + (p%10)*p_10
     if p not in prime_s:
       break
  else:
     res += 1

print res


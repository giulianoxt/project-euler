from euler import *
from itertools import count, ifilter

def abundant(n):
  return sum(divisors(n)) > 2*n

L = 28124
abund = set(ifilter(abundant, xrange(L)))

res = 0
for n in xrange(L):
  sum_2 = False
  for a in abund:
    b = n-a
    if a > b:
      break
    if b in abund:
      sum_2 = True
      break
  if not sum_2:
    res += n

print res


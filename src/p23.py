from euler import *
from itertools import count

def abundant(n):
  return sum(divisors(n)) > 2*n

L = 28124
abund = map(abundant, xrange(L))

res = 0
for n in xrange(L):
  sum_2 = False
  for a in count(1):
    b = n-a
    if a > b:
      break
    if abund[a] and abund[b]:
      sum_2 = True
      break
  if not sum_2:
    res += n

print res


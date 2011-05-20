from euler import *

def d(n):
  return sum(x for x in divisors(n) if x < n)

def amicable(a):
  b = d(a)
  return a != b and d(b) == a

print sum(filter(amicable, xrange(1, 10000)))


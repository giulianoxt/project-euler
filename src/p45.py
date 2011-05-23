from math import sqrt
from itertools import count

def is_int(n):
  return n == int(n)

def is_triangle(x):
  dsq = sqrt(1 + 8*x)
  return is_int((-1 + dsq) / 2)

def is_pentagonal(x):
  dsq = sqrt(1 + 24*x)
  return is_int((1 + dsq) / 6)


for n in count(144):
  x = n*(2*n - 1)
  if is_triangle(x) and is_pentagonal(x):
    print x
    break


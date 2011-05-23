from sys import exit
from itertools import count
from math import log10, floor

def same(a, b):
  if len(a) == len(b):
    return a == sorted(b)
  else:
    return False

def num_digits(n):
  f = floor(log10(max(n, 1)))
  return int(f + 1)


st, lim = 100, 666
while True:
  for k in xrange(st, lim+1):
    nd_k = num_digits(k)
    n = 10**nd_k + k
    n_str = sorted(str(n))
    
    if all(same(n_str, str(m*n)) for m in xrange(6,1,-1)):
      print n
      exit(0)
 
  st *= 10
  lim = lim*10 + 6


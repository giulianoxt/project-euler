from math import sqrt

def value(s):
  return sum(ord(c)-ord('A')+1 for c in s) 

def is_nat(n):
  return n == int(n) and n > 0

def is_triangle(s):
  val = value(s)
  sqrt_d = sqrt(1 + 8*val)
  return is_nat((-1 + sqrt_d) / 2)

words = input()
print len(filter(is_triangle, words))


from math import floor, factorial

perm_end = 1000000
perm_pos = 0
perm, ds = '', range(10)

while ds:
  to_go = factorial(len(ds)-1)

  x = 0
  while perm_pos + (x+1)*to_go < perm_end:
    x += 1
  
  perm += str(ds.pop(x))
  perm_pos += x*to_go

print perm


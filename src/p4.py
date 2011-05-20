L = 1000
m = 0

for i in xrange(1, L):
  for j in xrange(i+1, L):
    x = i*j
    if x <= m: continue
    s = str(x)
    if s == s[::-1]: m = x

print i, j, m


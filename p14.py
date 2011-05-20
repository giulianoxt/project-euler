import euler

M, x = 1, 1
for i in xrange(2, 1000000):
  sz = euler.collatz_size(i)
  if sz > M:
  M = sz
    x = i

print x


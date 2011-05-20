res = 0
for n in xrange(10, 1000000):
  if n == sum(int(d)**5 for d in str(n)):
    res += n

print res


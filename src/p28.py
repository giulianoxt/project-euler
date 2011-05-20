from euler import sum_pa

res, i = 1, 1

for step in xrange(2, 1001, 2):
  res += sum_pa(i+step, i+4*step, 4)
  i += 4*step

print res


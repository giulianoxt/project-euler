def valid(b, p):
  return (2*b*p - p*p) % (2*(b-p)) == 0


max, max_p = 0, -1

for p in xrange(10, 1001):
  n_sols = sum(1 for b in xrange(1, p-1) if valid(b, p))

  if n_sols > max:
    max = n_sols
    max_p = p

print max_p


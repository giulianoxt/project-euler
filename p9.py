def find(L):
  for a in xrange(1, L):
    for b in xrange(a+1, L):
      c = L-a-b

      if a+b >= L: break
      if a*a + b*b == c*c:
        print a, b, c
        return


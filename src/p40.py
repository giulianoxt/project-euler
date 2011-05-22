from euler import product
from itertools import count

def end_l(lim):
  end_l = [0]
  pos, nd = 0, 0
  while pos <= lim:
    pos += (10**nd * 9) * (nd+1)
    nd += 1
    end_l.append(pos)
  return end_l

def get_digit(pos, end_l):
  for nd in count(1):
    end_p = end_l[nd]
    if pos <= end_p:
       break

  pos -= end_l[nd-1] + 1
  n_pos = pos/nd

  n = n_pos + 10**(nd-1)
  dig_pos = pos - n_pos*nd

  return int(str(n)[dig_pos])

l = end_l(1000000)
print product(get_digit(10**p, l) for p in xrange(7))


from euler import *
from itertools import product as iproduct


st_digs = [2, 3, 5, 7]
md_digs = [1, 3, 5, 7, 9]
trunc_rl = set(st_digs)
trunc_lr = set(st_digs)
trunc = set()

while len(trunc) < 11:
  rl = trunc_rl.copy()
  trunc_rl.clear()

  for x, d in iproduct(rl, md_digs):
    n = x*10 + d
    if is_prime(n):
      trunc_rl.add(n)

  lr = trunc_lr.copy()
  trunc_lr.clear()

  for x, d in iproduct(lr, xrange(1, 10)):
    nd = num_digits(x)
    n = (d * 10**nd) + x
    if is_prime(n):
      trunc_lr.add(n)
      if n in trunc_rl:
        trunc.add(n)

print sum(trunc)


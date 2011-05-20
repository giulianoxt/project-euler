from euler import *

lim = 1000
mod = 10**10

res = 0
for n in xrange(1, lim+1):
  res = (res + n_pow_m_mod_k(n, n, mod)) % mod

print res


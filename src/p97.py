from euler import *

k = 10**10
x = n_pow_m_mod_k(2, 7830457, k)
x = (x * 28433) % k
x = (x + 1) % k

print x


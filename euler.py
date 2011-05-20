from math import ceil, floor, sqrt

def gcd(a, b):
  if a < b: return gcd(b, a)
  if not b: return a
  return gcd(b, a%b)

def lcm(a, b):
  return (a*b) / gcd(a, b)

def primes(limit, sieve = []):
  if limit <= 2:
    if limit == 2: yield 2
    return

  bound = (limit-1)/2 
  sieve = [False] * (bound+1)

  c_limit = int(ceil((sqrt(limit)-1)/2))
  
  for i in xrange(1, c_limit+1):
    if not sieve[i]:
      j0 = 2*i*(i+1)
      if j0 <= bound:
        for j in xrange(j0, bound+1, 2*i+1):
          sieve[j] = True
  
  yield 2
  for i in xrange(1, bound+1):
    if not sieve[i]:
      yield 2*i+1

def factors(n):
  f, n0 = {}, n
  for p in primes(n):
    while not n % p:
      f[p] = f.get(p, 0) + 1
      n /= p
    if n == 1:
      break

  return f

def product(l):
  return reduce(lambda x,y: x*y, l, 1)

def is_prime(n):
  if n == 1: return False
  if n < 4: return True
  if not n % 2: return False
  if n < 9: return True
  if not n % 3: return False

  r, f = floor(sqrt(n)), 5

  while f <= r:
    if not (n % f and n % (f+2)): return False
    f += 6
  
  return True

def fibonacci(num, _start = (1, 1)):
  a, b = _start
  for _ in xrange(num):
    yield a
    a, b = b, a+b

def fibonacci_inf(_start = (1, 1)):
  a, b = _start
  while True:
    yield a
    a, b = b, a+b

def collatz_size(n, _mem = {1 : 1}):
  if not n in _mem:
    if n % 2:
      _mem[n] = 1 + collatz_size(3*n+1, _mem)
    else:
      _mem[n] = 1 + collatz_size(n/2, _mem)
    
  return _mem[n]

def divisor_count(n):
  i, c = 1, 0
  while i*i <= n:
    if not n % i:
      c += 2
    i += 1
  return c-1 if i*i == n else c

def divisors(n):
  i, s = 1, set()
  while i*i <= n:
    div, mod = divmod(n, i)
    if not mod:
      yield i
      if div != i: yield div
    i += 1

def sum_pa(a_1, a_n, n):
  return (n*(a_1 + a_n)) / 2

def sum_pg(a_1, q, n):
  return (a_1*(q**n - 1)) / (q - 1)

def sum_1_n(n):
  return (n*(n+1))/2

def sum_1_n2(n):
  return (n*(n+1)*(2*n+1))/6

def sum_1_n3(n):
  return sum_1_n(n)**2

def n_pow_m_mod_k(n, m, k):
  if m == 0:
    return 1
  if m % 2:
    return (n % k) * ((n_pow_m_mod_k(n, (m-1)/2, k) ** 2) % k)
  else:
    return (n_pow_m_mod_k(n, m/2, k)**2) % k



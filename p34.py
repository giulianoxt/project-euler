from math import factorial as fact

f = [fact(d) for d in xrange(10)]

res = 0
n = 10
while n <= 1000000:
  ds = map(int, str(n))
  ds_sum = sum(f[d] for d in ds)

  if n == ds_sum:
    res += n

  if n > 10000:
    if ds_sum - f[ds[-1]]-f[ds[-2]]-f[ds[-3]]-f[ds[-4]] + 4*f[9] < n:
      n = (n/10000)*10000 + 10000
      continue

    if ds_sum - f[ds[-1]]-f[ds[-2]] + 2*f[9] < n:
      n = (n/100)*100 + 100
      continue

    if ds_sum - f[ds[-1]] + f[9] < n:
      n = (n/10)*10 + 10
      continue
    
  n += 1

print res


def div_1(d):
  num = 1
  cnt = 0
  rem = {}
  
  while num:
    if num in rem:
      return cnt - rem[num] + 1

    cnt += 1
    rem[num] = cnt
    num = (num % d) * 10

  return 0


max, max_d = 0, 0

for d in xrange(7, 1000):
  cnt = div_1(d)
  if cnt > max:
    max = cnt
    max_d = d

print max_d


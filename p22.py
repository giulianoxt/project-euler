names = open('p22.in').read().split(',')
names = [n[1:-1] for n in names]
names.sort()

res = 0
for i in xrange(len(names)):
  tmp = sum(ord(c)-ord('A')+1 for c in names[i])
  res += tmp*(i+1)

print res


trig = open('p67.in').read()
trig = [map(int, l.split()) for l in trig.strip().split('\n')]

def search(i, j, _mem = {}):
  if i < 0 or j < 0 or j > i: return 0
  if (i,j) in _mem: return _mem[i,j]

  best = max(search(i-1, k, _mem) for k in (j-1,j))  
  res = _mem[i,j] = trig[i][j] + best
  return res

print max(search(len(trig)-1, j) for j in xrange(len(trig[-1])))


trig = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

trig = [map(int, l.split()) for l in trig.split('\n')]

def search(i, j, _mem = {}):
  if i < 0 or j < 0 or j > i: return 0
  if (i,j) in _mem: return _mem[i,j]

  best = max(search(i-1, k, _mem) for k in (j-1,j))  
  res = _mem[i,j] = trig[i][j] + best
  return res

print max(search(len(trig)-1, j) for j in xrange(len(trig[-1])))


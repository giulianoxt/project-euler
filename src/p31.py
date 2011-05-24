coins = [1, 2, 5, 10, 20, 50, 100, 200]
n_coins, max_v = 8, 200

ways = [[1] * n_coins for _ in xrange(max_v+1)]

for v in xrange(1, max_v+1):
  for i in xrange(n_coins):
    ways[v][i] = 0
    if i:
      ways[v][i] += ways[v][i-1]
    if v >= coins[i]:
      ways[v][i] += ways[v-coins[i]][i]

print ways[max_v][n_coins-1]


from euler import *

i = 0
for f in fibonacci_inf():
  i += 1
  if len(str(f)) == 1000:
    break

print i


from euler import divisor_count

trig, i = 0, 1

while True:
  trig += i
  i += 1
  print trig
  if divisor_count(trig) > 500:
   break


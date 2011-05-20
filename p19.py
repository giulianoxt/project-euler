def is_leap_year(y):
  if not y % 400:
    return True
  if not y % 100:
    return False
  return not y % 4

def days_on_month(m, y): 
  if m == 2:
    if is_leap_year(y):
      return 29
    else:
      return 28
  elif m in (4, 6, 9, 11):
    return 30
  else:
    return 31

res = 0
dw = 2
m = 1
y = 1901

while True:
  if y == 2001:
    break
  if dw == 0:
    res += 1

  dw = (dw + days_on_month(m, y)) % 7
  if m < 12:
    m += 1
  else:
    m = 1
    y += 1

print res


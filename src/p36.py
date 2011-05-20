from itertools import chain, ifilter, imap

def palindromes(max_size, base = 10):
  def digit(d):
    if d < 10: return str(d)
    return chr(d-10+ord('A'))

  def palindromes_sz(size, first = False):
    if not size:
      yield ''
      return

    first_dig = 1 if first else 0
    for dig in xrange(first_dig, base):
      d = digit(dig)
      if size == 1:
        yield d
      else:
        for pali in palindromes_sz(size-2):
          yield d + pali + d
  
  l = (palindromes_sz(s,True) for s in xrange(1,max_size+1))
  return chain(*l)

c = 0
for bin_pal in palindromes(20, base = 2):
  n = int(bin_pal, 2)
  ns = str(n)
  if n < 1000000 and ns == ns[::-1]:
    c += n

print c


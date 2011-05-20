digits = [
 'zero', 'one', 'two', 'three', 'four', 'five',
 'six', 'seven', 'eight', 'nine'
]

dozens = {
 10: 'ten',
 11: 'eleven',
 12: 'twelve',
 13: 'thirteen',
 14: 'fourteen',
 15: 'fifteen',
 16: 'sixteen',
 17: 'seventeen',
 18: 'eighteen',
 19: 'nineteen',
 20: 'twenty',
 30: 'thirty',
 40: 'forty',
 50: 'fifty',
 60: 'sixty',
 70: 'seventy',
 80: 'eighty',
 90: 'ninety'
}

def write(n):
  if n == 1000:
    return 'one thousand'
  elif n > 99:
    tmp = write(n/100) + ' hundred'
    if n % 100:
      return tmp + ' and ' + write(n % 100)
    else:
      return tmp
  elif n > 9:
    if n in dozens:
      return dozens[n]
    else:
      tmp = dozens[(n/10)*10]
      if n % 10:
        return tmp + ' ' + write(n % 10)
      else:
	return tmp
  else:
    return digits[n]

words = (write(i) for i in xrange(1, 1001))
all = (''.join(''.join(w.split()) for w in words))
print len(list(all))


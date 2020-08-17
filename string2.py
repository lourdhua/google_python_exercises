# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  if s.endswith('ing'):
    res = s+'ly'
  elif len(s)>=3:
    res = s + 'ing'
  else:
    res = s
  return res

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  res1 = s
  for i in range(0,s.count('not')):
    res = res1.find('not')
    res2 = s[res:].find('bad')
    if res2 > 0:
      res1 = res1.replace(res1[res:(res + res2 + len('bad'))],'good')   #first occ.of 'not' + first occ.of 'bad' after first occ.of 'not' + len(bad)
  return res1

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  if len(a)%2 == 0:
    af = a[0:int(len(a)/2)]
    ab = a[int(len(a)/2):]
  if len(a)%2 == 1:
    af = a[0:int((len(a)+1)/2)]
    ab = a[int((len(a)+1)/2):]
  if len(b)%2 == 0:
    bf = b[0:int(len(b)/2)]
    bb = b[int(len(b)/2):]
  if len(b)%2 == 1:
    bf = b[0:int((len(b)+1)/2)]
    bb = b[int((len(b)+1)/2):]
  print(a,b)
  return af+bf+ab+bb

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  #print
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad! but not bad'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  #print
  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()

import cmath
## character counts in a string
def charcount(s):
  cset = set(s)
  d={}
  for i in cset:
    d[i] = s.count(i)
  print(d)
	
## consecutive character counts in a string
def maxCntConsChar(s):
  cnt = 1
  maxcnt = 0
  print(s)
  for i in range(len(s)-1):
    if s[i]==s[i+1]:
      cnt = cnt+1
      if(maxcnt<cnt):
        print(s[i],cnt)
        maxcnt = cnt
    else:
      cnt = 1
  print (maxcnt)
	
def triarea(a,b,c):
  s = (a+b+c)/2
  area = (s*(s-a)*(s-b)*(s-c))**0.5
  print(area)

def factorial(x):
  if x == 1:
    return 1
  else:
    return x*factorial(x-1)

##specific char counts
def countVowels(a):
  cset = {'a','e','i','o','u'}
  cdict = dict.fromkeys(cset,0)
  print(cdict)
  for i in cset:
    cdict[i] = a.count(i)
  print(cdict)

def sortAlpha(a):
  w = a.split()
  w.sort()
  for i in w:
    print(i,end=' ')

# get the word that repeats after
def repeatingWord(a):
  wlist = a.split('/')
  res = ''
  for i in range(0,len(wlist)-1):
    if wlist[i] in wlist[i+1:]:
      res = wlist[i]
  return res

# get the word that repeats after
def repeatingWordAlternate(a):
  cset = set(a.split('/'))
  cd = dict.fromkeys(cset,1)
  for i in cset:
    cd[i] = a.count(i)
  return cd

# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  charcount('comicom')
  maxCntConsChar('ccccmmm')
  triarea(3,4,5)
  print(factorial(6))
  countVowels('little brown fox')
  sortAlpha('current alpha book cures distance distr')
  print(repeatingWord('https:/www.w3resource.com/python-exercises/python-exercises/resource/exercises'))
  print(repeatingWordAlternate('https:/www.w3resource.com/python-exercises/python-exercises/resource/exercises'))
if __name__ == '__main__':
  main()

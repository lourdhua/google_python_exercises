import numpy as np

#sum up the list items
def sumlist(a1):
  sl = 1
  #sum(a1)  #will work only if the list items are integers, else fail
  #np.cumsum(a1) #returns an array of list with cumulative sum of 'a1' elements. list must contain only numbers
  print('Sum of list integers: ',sum([v for v in a1 if isinstance(v,int)]))
  """ 
  # If we need to multiply the list items - use below snippet
  for it in a1:
    if isinstance(it,int):
      sl = sl*it
  print(sl)
  """

from functools import reduce
def listcalc(opr,l):
  if opr=='sum':
    res = sum([item for item in l if (isinstance(item,int) or isinstance(item,float))])
    #res = reduce(lambda x,y:x+y,l)
  elif opr=='mul':
    res = reduce(mul,l)
    res = reduce(lambda x,y:x*y,l)
  elif opr=='sqrt':
    res = [x**2 for x in l if (isinstance(x,int) or isinstance(x,float))]
  return res

#take only digits(int, float) from given list
def takedigits(a1):
  lif = [x for x in a1 if(isinstance(x,int) or isinstance(x,float))]
  print('Filtered list with only Numbers: ',lif)

#count the list items with same first and last characters (takes only strings)
def firstlast(a1):
  cnt = 0
  for item in a1:
    if isinstance(item,str) and len(item) >=2 and item[0]==item[-1]:
      cnt = cnt +1
  print ('Count of List items with same first and last char: ',cnt)

from operator import itemgetter, attrgetter
#sort tuples based on each last element https://docs.python.org/3/howto/sorting.html
def sorttuple(tl):
  print('Tuple Sorted based on last element of each item: ',sorted(tl,key=itemgetter(-1)))

import collections
#count the frequency of list items
def countlistelts(a1):
  print('Frequency of list items: ',collections.Counter(a1))

#returns the common element from a1 and a2 lists
def commonitems(a1,a2):
  print('Common elements from a1 & a2: ',set(a1) & set(a2))

from itertools import zip_longest, chain, tee
#returns the common element from a1 and a2 lists
def swap_nth_elements(a1,n):
  print ('Swapped elements: ',list(chain.from_iterable(zip_longest(a1[1::n],a1[::n]))))
    
#sorting
def subkeysort(ss):
  ss.sort(key=lambda e:e['k']['sk'],reverse=True)
  print('Sorted by sub key: ',ss)

def zipper(cn,cc):
  list(zip(cn,cc))  #[('Black', '#000000'), ('Red', '#FF0000'), ('Maroon', '#800000'), ('Yellow', '#FFFF00'), ('gray', '#FFF000'), ('white', '#FFFFFF'), ('red', '#FF0000'), ('Black', '#000000')]
  set(zip(cn,cc))   #{('red', '#FF0000'), ('Black', '#000000'), ('Yellow', '#FFFF00'), ('gray', '#FFF000'), ('Maroon', '#800000'), ('Red', '#FF0000'), ('white', '#FFFFFF')}
  dict(zip(cn,cc))  #{'Black': '#000000', 'Red': '#FF0000', 'Maroon': '#800000', 'Yellow': '#FFFF00', 'gray': '#FFF000', 'white': '#FFFFFF', 'red': '#FF0000'}

def maxitem(c):
  return max(c,key=sum)
  
from itertools import groupby
def removedups(a1):
  print([key for key,group in groupby(a1)])

def fillLists(a,b):
  for i in range(0,10):
    a.append(i)
  for i in range(0,10):
    b.append(i)

def listofDicts(cn,cc):
  return [{'colorName':f,'colorCode':c} for f,c in zip(cn,cc)]

import random  
def main():
  a1 = [1,4,5,'ksd','df',6,7.2,99.03,'ili','ksk','alsdf2ana','xx','n',2, 2, 3, 5, 6, 4, 3, 1, 5, 2, 2, 5]
  a2 = [4,5,'kTV','df',6.2,99.03]
  tl = [(1,11),(2,4),(1,3),(1,2)]
  ss = [{'k': {'sk': 7}}, {'k': {'sk': 10}}, {'k': {'sk': 5}}]
  cn = ['Black', 'Red', 'Maroon', 'Yellow', 'gray', 'white', 'red', 'Black']
  cc = ['#000000', '#FF0000', '#800000', '#FFFF00', '#FFF000', '#FFFFFF', '#FF0000', '#000000']
  c = [[2,4,5],[9,10],[202,4,2],[9,4,38,154]]
  N = random.randint(0,100000)
  a=[random.randint(0,1000) for i in range(0,N)]    #generating a random list of length N with values between 0...1000
  b=[random.randint(0,999999) for i in range(0,N)]  #generating a random list of length N with values between 0...999,999
  l=[4,5,7,2,4]
  cn = ["Black", "Red", "Maroon", "Yellow"]
  cc = ["#000000", "#FF0000", "#800000", "#FFFF00"]
  #a = [263, 9, 29] #[0,1,2,2,3,5]
  #b = [308673, 599055, 944984] #[500000,500000,0,0,0,20000]
  sumlist(a1)
  takedigits(a1)
  firstlast(a1)
  sorttuple(tl)
  countlistelts(a1)
  commonitems(a1,a2)
  swap_nth_elements(a1,2)   #swaps every 2nd element with its previous one
  subkeysort(ss)
  zipper(cn,cc)
  maxitem(c)
  removedups(a1)
  fillLists(a,b)
  #print('N:',N)
  #print('a:',a)
  #print('b:',b)
  listcalc('sum',l)
  listofDicts(cn,cc)
if __name__ == '__main__':
  main()

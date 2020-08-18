from operator import itemgetter
def basic_ops(d):
    print('original:',d)
    print('keys: ',d.keys())
    print('values: ',d.values())
    print('items: ',d.items())
    print('Sorted: ',dict(sorted(d.items(),key=lambda v:v[1] if isinstance(v[1],int) else 0)))
    #print('Sorted: ',dict(sorted(d.items(),key=itemgetter(1))))     #dict() creates the dictionary from the sorted-returned sequence
    print('Min value: ',min((x for x in d.values() if isinstance(x,int)), default='no numbers'))
    print('Sum: ',sum(x for x in d.values() if isinstance(x,int)))
    print('Check Empty List:',bool(d))                              #returns false if list is empty
    #return sorted(d.items(),key=itemgetter(1))

##################
import re
from collections import Counter
def counterops(fname):
    w=re.findall(r'w+',open(fname).read().lower())  #w results a list of words from given file
    Counter(w).most_common(10)      #gives most common 10 words from file
    wc = Counter(w)
    sorted(wc.elements())           #returns list of elements from wc in ascending order
    wc.most_common(10)              #gives most common 10 words from file
    wc.subtract({'what':2,'lourdhu':2})     #tries to subtract given items of count from counter wc
    
##################
def main():
    c={'a': 4, 'h': 1, 'b': 1, 'd': 1, 'l': 4}
    d={1: 'a', 2: 'g', 3: 'x', 6: 'n', 5: 's', 4: 'i', 99:5, 100:3, 80:80, 91:'7'}
    fname = 'small.txt'
    basic_ops(d)
    counterops(fname)
if __name__ == '__main__':
    main()

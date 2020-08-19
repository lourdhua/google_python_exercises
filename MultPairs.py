"""
Scenario:

Arrays A and B consisting of N non-negative integers are given. Together, they represent N real numbers, denoted as C[0], ..., C[N−1]. Elements of A represent the integer parts and the corresponding elements of B (divided by 1,000,000) represent the fractional parts of the elements of C. More formally, A[I] and B[I] represent C[I] = A[I] + B[I] / 1,000,000.
For example, consider the following arrays A and B:
A[0] = 0 B[0] = 500,000 A[1] = 1 B[1] = 500,000 A[2] = 2 B[2] = 0 A[3] = 2 B[3] = 0 A[4] = 3 B[4] = 0 A[5] = 5 B[5] = 20,000
They represent the following real numbers:
C[0] = 0.5 C[1] = 1.5 C[2] = 2.0 C[3] = 2.0 C[4] = 3.0 C[5] = 5.02
A pair of indices (P, Q) is multiplicative if 0 ≤ P < Q < N and C[P] * C[Q] ≥ C[P] + C[Q].
The above arrays yield the following multiplicative pairs:
•	(1, 4), because 1.5 * 3.0 = 4.5 ≥ 4.5 = 1.5 + 3.0,
•	(1, 5), because 1.5 * 5.02 = 7.53 ≥ 6.52 = 1.5 + 5.02,
•	(2, 3), because 2.0 * 2.0 = 4.0 ≥ 4.0 = 2.0 + 2.0,
•	(2, 4) and (3, 4), because 2.0 * 3.0 = 6.0 ≥ 5.0 = 2.0 + 3.0.
•	(2, 5) and (3, 5), because 2.0 * 5.02 = 10.04 ≥ 7.02 = 2.0 + 5.02.
•	(4, 5), because 3.0 * 5.02 = 15.06 ≥ 8.02 = 3.0 + 5.02.
Write a function:
def solution(a, b)
that, given arrays A and B, each containing N non-negative integers, returns the number of multiplicative pairs of indices.
If the number of multiplicative pairs is greater than 1,000,000,000, the function should return 1,000,000,000.
For example, given:
A[0] = 0 B[0] = 500,000 A[1] = 1 B[1] = 500,000 A[2] = 2 B[2] = 0 A[3] = 2 B[3] = 0 A[4] = 3 B[4] = 0 A[5] = 5 B[5] = 20,000
the function should return 8, as explained above.
Write an efficient algorithm for the following assumptions:
•	N is an integer within the range [0..100,000];
•	each element of array A is an integer within the range [0..1,000];
•	each element of array B is an integer within the range [0..999,999];
•	real numbers created from arrays are sorted in non-decreasing order.
"""

import datetime
def solution(a,b):
  c = []
  cnt = 0
  maxlen = 100000
  stime = datetime.datetime.now()
  if (0 < len(a) <= maxlen) and (0 < len(b) <= maxlen) and (len(a)==len(b)):        #List length check
    if (0 <= min(a) and max(a) <=1000) and (0 <= min(b) and max(b) <=999999):       #min max values check
      ns = datetime.datetime.now()
      c = [a[i] + b[i]/1000000 for i in range(0,len(a))]                            #[expr for iterator in range(sequence)]
      ne=datetime.datetime.now()
      print("Duration for C:",ne-ns)

      bfs = datetime.datetime.now()
      c.sort()
      afs = datetime.datetime.now()
      print("sort time:",afs-bfs)
      #print('c:',c)
      for pi in range(0,len(c)):
        for qi in range(pi+1,len(c)):
          #print(pi,qi,c[pi],c[qi],c[pi]*c[qi],c[pi]+c[qi])
          cnt = cnt+1 if c[pi]*c[qi] >= c[pi]+c[qi] else cnt                        #truevalue if condition else falsevalue
          if cnt >= 1000000000:
            cnt = 1000000000
            break
    else:
      print('List values out of range: Expected A[0]...A[N-1]=[0...1000] and B[0]...B[N-1]=[0...999999], Recieved: ['
        ,min(a),'...',max(a),'] and [',min(b),'...',max(b),']')
  elif (len(a) == 0):
    print('List A is empty')
  elif (len(b) == 0):
    print('List B is empty')
  else:
    print('Given Arrays A & B must be of same length with range of 0...',maxlen)
  print('Count:',cnt)
  etime = datetime.datetime.now()
  duration = etime - stime
  print('Start:',stime,' End:',etime,' Duration:',duration)
  return cnt

import random  
def main():
  N = random.randint(0,100000)
  a=[random.randint(0,1000) for i in range(0,N)]    #generating a random list of length N with values between 0...1000
  b=[random.randint(0,999999) for i in range(0,N)]  #generating a random list of length N with values between 0...999,999
  solution(a,b)

if __name__ == '__main__':
  main()

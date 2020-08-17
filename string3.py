# swap the first two chars of a and b then concatenate them both; assume they are with lengh>2
def mixmatch(a,b):
    if len(a)>2 and len(b)>2:
        res = b[0:2] + a[2:] + ' ' + a[0:2] + b[2:]
    else:
        res = a + ' ' + b
    return res
    
def tester(got, expected):
    if got == expected:
        print ('OK: expected: %s and Got: %s' %( repr(expected), repr(got) ))
    else:
        print ('NOT OK: expected: %s and Got: %s' %( repr(expected), repr(got) ))

#Take the first character of given string input
#replace its occurrences (other than first one) with '*' and return the replaced string
def replacer(s):
    res = s[0]+s[1:].replace(s[0],'*')
    return res

# Inputs: Index value = ind, Occurrence = occ, String = s
# Find the given indexed character inside the string s.
# Replace its occurrence mentioned as in 'occ' with '*'
def w_char_w_occ(ind,occ,s):
    if len(s)>=ind:
        x = s[ind]
        print('char to replace: %s' %(x))
        oInd = 0
        for i in range(0,occ):
            oInd = oInd + s[oInd:].find(x)
            print('Looping in occurrence Index: ',oInd)
            i += i
        res = s[0:oInd]+'*'+s[oInd+1:]
    else:
        res = 'low strength'
    return res

#Inputs: String, Substring, occurrenceNumber=n
#Split the string into multiple parts based on Substring
#Find and return 'n'th part
def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    print(parts)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)

def main():
    tester(mixmatch('abcd','xyza'),'xycd abza')
    tester(mixmatch('ab','yza'),'ab yza')
    tester(mixmatch('a',''),'a ')

    tester(replacer('googlegig'),'goo*le*i*')
    tester(replacer('g'),'g')
    tester(replacer(' f'),' f')
    
    findnth('foofbargfsf', 'f', 2)
    tester(w_char_w_occ(5,2,'aabbbcccd'),'aabbbc*cd')
main()
import random
import itertools

def millertest(d, n):
    a = 2 + random.randint(1, n-4)
    x = pow(a, d, n)        # (a ^ d) % n
    if (x == 1 or x == n-1):
        return True
    while (d != n-1):
        x = (x * x) % n 
        d *= 2
        if (x == 1):
            return False
        if (x == n-1):
            return True 
    return False

def isPrime(n, k):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n%2 == 0 or n%3 == 0):
        return False
    d = n - 1
    while (d%2 == 0):
        d //=2 
    for i in range(k):
        if (millertest(d, n) == False):
            return False
    return True

if __name__ == '__main__':
    firstlast = input().split()
    first = int(firstlast[0])
    last = int(firstlast[1])
    count = 0
    k = 4
    b = ""
    if len(str(first))>9:
        i=0
        while i<len(str(first)) and str(first)[i] == str(last)[i]:
            b+=str(first)[i]
            i+=1
    q = len(b)
    l = len((str(last))
    f = len((str(first))
    for i in range(f,l+1):
        L = [p for p in itertools.product(['2','3','5','7'], repeat=i-q)]
        for c in range(len(L)):
            a = int(b+''.join(L[c]))
            if a >= first and a <= last:
                if(isPrime(a, k)):
                    count += 1
    print(count)
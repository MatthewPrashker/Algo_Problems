from sys import stdin, stdout
from collections import defaultdict

#dictionary mapping a prime to the exponent appearing in n
def factor(n):
    ans = defaultdict(int)
    d = 2
    while(d*d <= n):
        if(n%d == 0):
            e = 0
            while(n%d == 0):
                n = n // d
                e += 1
            ans[d] = e
        d += 1 
    if(n > 1):
        ans[n] = 1
    return ans
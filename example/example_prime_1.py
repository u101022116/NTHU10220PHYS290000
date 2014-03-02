from __future__ import division, print_function

def factor(n):
    factorlist = []
    k = 2
    while k <= n:
        while n%k == 0:
            factorlist.append(k)
            print(k)
            n //= k
        k += 1
    return factorlist

print(23,factor(23))
print(17556,factor(17556))
print(factor(99991))
#print(factor(1345678))
#print(factor(12345678910))

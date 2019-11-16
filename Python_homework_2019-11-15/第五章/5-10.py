from random import randint#因数分解
from math import sqrt
def factoring(n):
    if not isinstance(n,int):
        print('You must give an integer')
        return
    result=[]
    for p in primes:
        while n!=1:
            if n%p ==0:
                n=n/p
                result.append(p)
            else:
                break
    else:
        result='*'.join(map(str,result))
        return result
    if not result:
        return n
testdata=[randint(10,1000) for i in range(10)]
maxdata=max(testdata)
primes=[p for p in range(2,maxdata) if 0 not in [p%d for d in range(2, int(sqrt(p)+1))]]
for data in testdata:
    r=factoring(data)
    print(data,'=',r)
    print(data==eval(r))
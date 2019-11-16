import math
def cni1(n,i):
    return int(math.factorial(n)/math.factorial(i)/math.factorial(n-i))
def cni2(n,i):
    if not (isinstance(n,int) and isinstance(i,int) and n>=i):
        print('n and i must be integers and n must be larger than or equal to i.')
        return
    result=1
    min,max=sorted((i,n-i))
    for i in range(n,0,-1):
        if i>max:
            result =i*result
        elif i<=min:
            result =i/result
        return result
print(cni2(6,3))
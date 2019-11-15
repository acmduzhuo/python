import math
def IsPrime(v):
    n = int(math.sqrt(v)+1)
    for i in range(2,n):
        if v%i==0:
            return 'No'
    else:
        return 'Yes'
x = int(input("请输入一个整数："))
print(IsPrime(x))
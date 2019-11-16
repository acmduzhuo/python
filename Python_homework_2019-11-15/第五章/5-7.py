def demo(m,n):#最大公约数，最小公倍数
    p=m*n
    while m%n !=0:
        m,n=n,m%n
    return(n,p//n)
def demo(m,n):#gcd函数实现
    import math
    r=math.gcd(m,n)
    return (r,(m*n)//r)
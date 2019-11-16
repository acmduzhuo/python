def demo(v,n):#求a+aa+aaa+aaaa......
    assert type(n) == int and 0<v<10,'v must be integer between 1 and 10'
    result,t=0,0
    for i in range(n):
        t=t*10+v
        result += t
    return result
print(demo(3,4))

def demo(a,n):#python方法
    a=str(a)
    result=sum(eval(a*i) for i in range(1,n+1))
    return result
print(demo(3,4))
def demo(x,n):#小于n的放在n前，大于放在后
    t1=[i for i in x if i<n]
    t2=[i for i in x if i>n]
    return t1+[n]+t2
def demo(x,n):
    t1=[]
    t2=[]
    for i in x:
        if i<n:
            t1.append(i)
        elif i>n:
            t2.append(i)
    return t1+[n]+t2
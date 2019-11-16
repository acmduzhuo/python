import random
def mergesort(seq,reverse=False):
    mid=len(seq)//2
    left,right=seq[:mid],seq[mid:]
    if len(left)>1:
        left=mergesort(left)
    if len(right)>1:
        right=mergesort(right)
    temp=[]
    while left and right:
        if left[-1] >= right[-1]:
            temp.append(left.pop())
        else:
            temp.append(right.pop())
    temp.reverse()
    result=(left or right) +temp
    if reverse:
        i,j=0,len(result)-1
        while i<j:
            result[i],result[j]=result[j],result[i]
            i+=1
            j-=1
    return result
for i in range(100):
    reverse = random.choice((True,False))
    x=[random.randint(1,100) for i in range(20)]
    y=sorted(x,reverse=reverse)
    x=mergesort(x,reverse)
    if x!=y:
        print('error')
from random import randint
def bubblesort(lst,end=None,reverse=False):
    if end==None:
        length=len(lst)
    else:
        length=end
    if length<=1:
        return
    flag=False
    for j in range(length-1):
        exp='lst[j]>lst[j+1]'
        if reverse:
            exp='lst[j]<lst[j+1]'
        if eval(exp):
            lst[j],lst[j+1]=lst[j+1],lst[j]
            flag=True
    if flag==False:
        return
    else:
        bubblesort(lst,length-1,reverse)
lst=[randint(1,100) for i in range(20)]
print('Before sorted:\n',lst)
bubblesort(lst)
print('After sorted:\n',lst)
from random import randint
def quicksort(lst,reverse=False):
    if len(lst)<=1:
        return lst
    pivot=lst.pop()
    first,second=[],[]
    exp='x<=pivot'
    if reverse==True:
        exp='x>=pivot'
    for x in lst:
        first.append(x) if eval(exp) else second.append(x)
    return quicksort(first,reverse)+[pivot]+quicksort(second,reverse)
lst=[randint(1,100) for i in range(10)]
print(quicksort(lst,True))
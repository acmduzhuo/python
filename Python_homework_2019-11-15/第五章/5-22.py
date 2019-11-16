def binarysearch(lst,value):
    start=0
    end=len(lst)
    while start<end:
        middle=(start+end)//2
        if value==lst[middle]:
            return middle
        elif value>lst[middle]:
            start=middle+1
        elif value<lst[middle]:
            end=middle-1
    return False
from random import randint
lst=[randint(1,50) for i in range(20)]
lst.sort()
print(lst)
result=binarysearch(lst,30)
if result != False:
    print('Success,its position is:',result)
else:
    print('Fail.not exist.')

import bisect
lst=list(range(10))
print(lst)
print(bisect.bisect_left(lst,5))
print(bisect.bisect_right(lst,5))
print(bisect.bisect_left(lst,5.5))
print(bisect.bisect_right(lst,5.5))
lst.insert(6,5.5)
bisect.insort_left(lst,7.9)
print(lst)
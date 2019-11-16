def selectsort(lst,reverse=False):
    length=len(lst)
    for i in range(0,length):
        m=i
        for j in range(i+1,length):
            exp='lst[j]<lst[m]'
            if reverse:
                exp='lst[j]>lst[m]'
            if eval(exp):
                m=j
        if m != i:
            lst[i],lst[m]=lst[m],lst[i]
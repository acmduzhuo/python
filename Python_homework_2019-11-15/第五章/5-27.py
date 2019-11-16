def primes(maxnumber):
    lst=list(range(3,maxnumber,2))
    m=int(maxnumber**0.5)
    for index in range(m):
        current=lst[index]
        if current>m:
            break
        lst[index+1:]=list(filter(lambda x:x%current!=0,lst[index+1:]))
    return [2]+lst
print(primes(100))
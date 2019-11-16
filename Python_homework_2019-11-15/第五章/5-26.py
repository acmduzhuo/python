import random
def getwoclosestelements(seq):
    seq=sorted(seq)
    dif=float('inf')
    for i,v in enumerate(seq[:-1]):
        d=abs(v-seq[i+1])
        if d<dif:
            first,second,dif=v,seq[i+1],d
    return(first,second)
seq=[random.random() for i in range(20)]
print(seq)
print(sorted(seq))
print(getwoclosestelements(seq))
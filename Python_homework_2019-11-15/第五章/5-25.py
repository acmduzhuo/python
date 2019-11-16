from itertools import combinations
from random import sample
def subasendinglist(lst):
    for length in range(len(lst),0,-1):
        for sub in combinations(lst,length):
            if list(sub)==sorted(sub):
                return sub
def getlist(start=0,end=100,number=20):
    if number>end-start:
        return None
    return sample(range(start,end),number)
def main():
    lst=getlist(number=10)
    if lst:
        print(lst)
        print(subasendinglist(lst))
main()
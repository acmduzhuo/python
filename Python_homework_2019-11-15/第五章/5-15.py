def main(n):#黑洞数
    start=10**(n-1)
    end=10**n
    for i in range(start,end):
        big=''.join(sorted(str(i),reverse=True))
        little=''.join(reversed(big))
        big,little=map(int,(big,little))
        if big-little==i:
            print(i)
n=4
main(4)
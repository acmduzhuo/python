from collections import defaultdict
def yanghui(n):
    triangle=defaultdict(int)
    for row in range(n):
        triangle[row,0]=1
        print(triangle[row,0],end=' ')
        for col in range(1,row+1):
            triangle[row,col]=triangle[row-1,col-1]+triangle[row-1,col]
            print(triangle[row,col],end=' ')
        print()
yanghui(5)
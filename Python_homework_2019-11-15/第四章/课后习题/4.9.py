x = int(input())
if x < 0:
    print(0)
elif x>=0 and x<5:
    print(x)
elif x>=5 and x<10:
    print(3*x-5)
elif x>=10 and x<20:
    print(0.5*x-2)
else:
    print(0)

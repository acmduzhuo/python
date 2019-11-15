while 1:
    print("input a number less than 1000")
    t=int(input())
    if t<2 or t>999:
        print("wrong number")
    else:
        break
print(t, end="")
print(" = ", end="")
i=2
while 1:
    if t==i:
        print(i, end="")
        break
    if t%i==0:
        print(i, end="")
        print(" * ", end="")
        t=t/i
    else:
        i+=1

a = [1,2,3,4]
x = [2,3]
for i in a:
    for j in a:
        if i==j:
            continue
        else:
            x.append((i*10+j))
for i in a:
    for j in a:
        for k in a:
            if i==j or j==k or i==k:
                continue
            else:
                x.append((i*100+j*10+k))
for i in a:
    for j in a:
        for k in a:
            for l in a:
                if i==j or j==k or i==k or l==i or l==k or l==j:
                    continue
                else:
                    x.append((i*1000+j*100+k*10+l))
y=[2,3,11]
for q in range(13,4322):
    if  q%2!=0 and q%3!=0 and q%5!=0 and q%7!=0 and q%11!=0:
        y.append(q)
z=[]
for o in x:
    for t in y:
        if o==t:
            z.append(o)
print(z)

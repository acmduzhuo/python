def Sorted(v):
    t = v[::]
    r = []
    while t:
        tt = min(t)
        r.append(tt)
        t.remove(tt)
    return r
if __name__ == '__main__':
    a = [1, 3, 2]
    print(Sorted(a))
from itertools import cycle#报数字游戏
def demo(lst,k):
    t_lst=lst[:]
    while len(t_lst)>1:
        c=cycle(t_lst)
        for i in range(k):
            t=next(c)
        index=t_lst.index(t)
        t_lst=t_lst[index+1:]+t_lst[:index]
    return t_lst[0]
lst=list(range(1,11))
print(demo(lst,3))  
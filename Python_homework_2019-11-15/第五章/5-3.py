def demo(lst,k):#接受有n个整数的列表和一个整数k，将列表下标k之前的元素逆序，下标k之后的元素逆序，整个列表逆序
    x=list[k-1::-1]
    y=listt[:k-1:-1]
    return list(reversed(x+y))
def demo(lst,k):#列表循环左移k位
    temp=lst[:]
    for i in range(k):
        temp.append(temp.pop(0))
    return temp
def demo(lst,k):#切片实现
    return lst[k:]+lst[:k]

from collections import deque#调用函数实现
q=deque(range(10))
q.rotate(3)
print(q)
q.rotate(-3)
print(q)

# print(int('11111', 2))#31
# print(int(3.2)) #3
# print(int('12', 16)) #18

# print(chr(ord('D') + 2))
# print(ord('D') + 2)

# x = 21
# y = 10
# print(x / y)#2.1
# print(x // y)#2

# x = 2.1
# y = 0.8
# print(x % y) #0.5

# print(range(1, 10))

#3.3
# import random
#
# a = [0] * 1000
#
# for i in range(1000):
#     n = random.randint(0, 101)
#     a[n] += 1
#     print(n)
# for i in range(101):
#     print(i,end = "")
#     print("出现了", end = "")
#     print(a[i],end = "")
#     print("次")

# print([3] in [1, 2, 3, 4])

#3.5
# x = input()
# xlist = x.split(",")
# xlist = [int(xlist[i]) for i in range(len(xlist))]
# arr = input().split(" ")
# a = int(arr[0])
# b = int(arr[1])
# print(xlist[a:b+1])

#3.9
# aDict = {'age':39, 'score':98, 'name':78, 'sex':31}
# print('请输入键值：')
# str = input()
# if str in aDict:
#     print(aDict[str])
# else:
#     print('您输入的键不存在')

#3.10
import random
s = []
for i in range(20):
    s.append(random.randint(0,100))
a = s[0:10]
a.sort()
b = s[10:20]
b.sort()
b.reverse()
print(s)
print(a)
print(b)
s = a + b
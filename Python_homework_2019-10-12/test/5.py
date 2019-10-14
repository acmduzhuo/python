a = 1234
b = a
arr = []
while b != int(0):
    arr.append(int(b%10))
    b = int(b/10)# 转化为整型
n = list(map(lambda x: x, arr))#通过转化为整型的数组来处理
n = n[::-1]#逆置，创建一个与原字符串顺序相反的字符串
print(n)

# a = 1234
# n = lambda i:[int(i) for i in str(a)]# 转化为字符处理
# print(n(a))
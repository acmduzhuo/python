# a = []
# for i in range(1, 10):#从0到9
#     if i % 2 == 0:#判定条件
#         a.append(i)#满足条件进入列表
# print(a)

a = [i for i in range(1, 10) if i % 2 == 0]#列表推导式
print(a)
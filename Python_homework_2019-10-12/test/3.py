alist = ['  aa', '  bb  ', 'cc  ']
# for i in range(3):#设置三重循环
#     alist[i] = alist[i].replace(' ', '')#将空格替换
# print(alist)

# alist = [alist[i].replace(' ', '') for i in range(3)]#列表推导式
# print(alist)

# a = []
# for i in range(3):#设置三重循环
#     a.append(alist[i].replace(' ', ''))#将空格替换
# print(a)

a = [alist[i].replace(' ', '') for i in range(3)]#列表推导式
print(a)
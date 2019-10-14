# x = (1, 2, 3)
# print(type(x))#查看元组类型
# print(x[0])#访问特定位置元素
# print(x[-1])#访问最后一个元素
# # x[1] = 4#元组是不可变的
# # print(x)
# x = (3)
# print(x)
# x = (3, )
# print(x)#如果元组中只有一个元素，要在后面加一个逗号
# x = ()
# x = tuple()
# # print(tuple(range(5)))#其他迭代对象转化为元组
# g = ((i+2)**2 for i in range(10))#创建生成器对象
# print(g)
# print(tuple(g))#将生成器对象转化为元组
# print(list(g))#生成器已经遍历对象，无元素
# g = ((i+2)**2 for i in range(10))#重新建立生成器对象
# print(g.__next__())#使用生成器g.__next__()方法获取元素
# print(next(g))#获取下一个元素
# g = ((i+2)**2 for i in range(10))
# for item in g:
#     print(item, end = ' ')#遍历生成器对象
x = filter(None, range(20))
print(1 in x)
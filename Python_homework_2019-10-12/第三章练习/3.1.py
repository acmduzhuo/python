# a_list = ['a', 'b','mpilgrim', 'z', 'example']
# a_list = []#创建空列表
# print(list((3, 5, 7, 9, 11)))#元组转化为列表
# print(list(range(1, 10, 2)))#range对象转化为列表
# print(list('hello, world'))#将字符串转化为列表
# print(list({3, 7, 5}))#集合转化为列表
# print(list({'a': 3, 'b':9, 'c':78}))#字典键转化为列表
# print(list({'a': 3, 'b':9, 'c':78}.items()))#字典键值转化为列表
# x = list()#创建空列表
# x = [1, 2, 3]
# del x
# print(x)#删除列表
# x = list('Python')
# # print(x)
# print(x[0])#第一个元素
# print(x[-1])#第二个元素
# x = [1, 2, 3]
# print(id(x))#查看ID
# x.append(4)
# print(x)#在尾部增加元素
# x.insert(0, 0)#在指定位置增加元素
# print(x)
# x.extend([5, 6, 7])#在尾部增加多个元素
# print(x)
# print(id(x))#内训地址不变
# x = [1, 2, 3, 4, 5, 6, 7]
# print(x.pop())#弹出并返回尾部元素
# print(x.pop(0))#弹出并返回指定元素
# x.clear()
# print(x)#删除所有元素
# x = [1, 2, 1, 1, 2]
# x.remove(2)
# print(x)#删除首个为2的元素
# del x[3]#删除指定位置元素
# print(x)
# x = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# print(x.count(3))#元素3在列表中出现的次数
# print(x.count(5))#不存在，返回0
# print(x.index(2))#元素2首次出现在列表中的索引
# print(x.index(5))#异常报错
# x = list(range(11))#从0到10的整数列表
# import random
# random.shuffle(x)#打乱顺序
# print(x)
# x.sort(key = lambda item:len(str(item)), reverse=True)
# print(x)#转化为字符串的以后按照长度降序排列
# x.sort(key = str)
# print(x)#转化为字符串的以后按照长度升序排列
# x.sort()
# print(x)#按照默认顺序排列
# x.reverse()
# print(x)#逆序输出
# x = [1, 2, [3, 4]]
# y = x.copy()#浅复制x
# print(y)
# y[2].append(5)#对子列表增加元素
# x[0] = 6#并不会影响到y
# y.append(6)#在新列表尾部增加元素
# print(x)
# x = [1, 2, 3]
# print(id(x))
# x = x + [4]
# print(id(x))#地址发生变化
# x += [5]
# print(id(x))#为列表增加元素，地址不会变
# x = [1, 2, 3, 4]
# print(id(x))
# x = x * 2
# print(id(x))#地址发生了变化
# x *= 2
# print(id(x))#地址未发生变化
# x = list(range(11))
# import random
# random.shuffle(x)
# print(x)
# print(all(x))#测试所有元素都等价为True
# print(any(x))#测试是否有等价于True的元素
# print(max(x))#返回最大值
# print(max(x, key = str))#按照规则返回最大值
# print(min(x))#返回最小值
# print(sum(x))#返回元素之和
# print(len(x))#返回元素个数
# print(list(zip(x, [1]*11)))#多列表元素重新组合
# print(list(zip(range(1, 4))))

aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
# print(id(aList))
# print(aList[::])#返回包含原列表所有元素的新列表
# print(id(aList[::]))#地址发生了变化
# print(aList[::-1])#返回原列表的逆序列表
# print(aList[::2])#返回序号为偶数的元素，序号从0开始
# print(aList[1::2])#返回序号为偶数的元素，序号从0开始
# print(aList[::3])#返回序号为3的倍数元素，序号从0开始
# print(aList[2::2])#返回序号为偶数的元素，序号从0开始[5, 7, 11, 15]
# print(aList[3:6])#返回序号3至5[6, 7, 9]
# print(aList[0:100])#结束位置大于列表长度[3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
# print(aList[100])#切片位置大于列表长度，报错
print(aList[100::])#切片开始位置大于列表长度，显示空列表
print(aList[-10:3])#视为从列表头部开始[3, 4, 5]
print(len(aList))#列表长度
print(aList[-2:-1])
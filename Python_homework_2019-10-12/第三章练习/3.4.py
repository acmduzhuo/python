# a = {3, 5}
# print(type(a))
# a_set = set(range(8, 14))
# print(a_set)
# b_set = set([0, 1, 2, 3, 0, 1, 2, 3, 7, 8])
# print(b_set)#去除重复元素
# x = set()#空集合

# import random
# {x.trip() for x in ('he', 'she   ' ,'  I')}
# print(x)

# import random
# x = {random.randint(1, 500) for i in range(100)}
# print(x)
# print(len(x))
# print({str(x) for x in range(10)})

# s = {1, 2, 3}
# s.add(3)#增加元素
# s.update({3, 4})#更新当前字典，忽略重复元素
# print(s)
# s.discard(5)#删除元素，元素不存在既忽略
# s.remove(5)#删除元素，元素不存在报错
# s.pop()

a_set = set([8, 9, 10, 11, 12, 13])
b_set = {0, 1, 2, 3, 7 ,8}
print(a_set | b_set)#并集
print(a_set.union(b_set))#并集
print(a_set & b_set)#交集
print(a_set.intersection(b_set))#交集
print(a_set.difference(b_set))#差集
print((a_set - b_set))#差集
print(a_set ^ b_set)#对称差集{0, 1, 2, 3, 7, 9, 10, 11, 12, 13}
print(a_set.symmetric_difference(b_set))#对称差集
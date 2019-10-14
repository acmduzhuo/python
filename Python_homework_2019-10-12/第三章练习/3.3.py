# x = dict()
# x = {}#空字典
# keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3, 4]
# dictionary = dict(zip(keys, values))#根据已有数据创建字典
# d = dict(name = 'Dog', age = 39)
# aDict = dict.fromkeys(['name', 'age', 'sex'])
# print(aDict)
aDict = {'age':39, 'score':[98, 97], 'name':'Dong', 'sex':'male'}
# print(aDict['age'])#指出键所在的位置
# print(aDict['address'])#报错
# if 'Age' in aDict:
#     print(aDict['Age'])
# else:
#     print('Not Exists.')
# print(aDict.get('age'))#返回对应的键值
# print(aDict.get('address', 'Not Exists.'))#指定的键不存在时返回默认值
# aDict['age'] = 39#修改元素值
# aDict['address'] = 'SDIBT'#增加新元素
# print(aDict)
# aDict.update({'a':97, 'age':39})
# print(aDict)
# del aDict['age']
# print(aDict)#删除字典元素
# aDict.popitem()#弹出最后一个元素
# print(aDict)
# aDict.pop('sex')
# print(aDict)

# import collections
# x = collections.OrderedDict()
# x['a'] = 3
# x['b'] = 5
# x['c'] = 8
# print(x)#OrderedDict([('a', 3), ('b', 5), ('c', 8)])

# import string
# import random
# x = string.ascii_letters+string.digits+string.punctuation
# z = ''.join([random.choice(x) for i in range(1000)])
# from collections import defaultdict
# frequences = defaultdict(int)
# print(frequences)#defaultdict(<class 'int'>, {})
# for utem in z:
#     frequences[item] += 1#修改每个字符的频率
# frequences.items()

# from collections import Counter
# frequences=Counter(z)
# print(frequences.items())
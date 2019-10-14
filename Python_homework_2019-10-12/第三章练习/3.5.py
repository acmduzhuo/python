# x, y, z = 1, 2, 3
# v_tuple = (False, 3.5, 'exp')
# (x, y, z) = v_tuple
# print(x, y, z)#False 3.5 exp
# x, y, z = v_tuple
# print(x, y, z)#False 3.5 exp
# x, y, z = range(3)
# print(x, y, z)#0 1 2
# x, y, z = iter([1, 2, 3])
# print(x, y, z)#1 2 3

a = [1, 2, 3]
b, c, d = a
x, y, z = sorted([1, 2, 3])
s = {'a':1, 'b':2, 'c':3}
b, c, d = s.items()
print(s)#{'a': 1, 'b': 2, 'c': 3}
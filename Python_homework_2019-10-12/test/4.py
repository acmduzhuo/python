from functools import reduce #reduce函数在python3的内建函数移除了，放入了functools模块
n = reduce(lambda x, y: x+y, range(1, 101)) #1+2 3+3 6+4, 将之后的数不断作为y计算
print(n)
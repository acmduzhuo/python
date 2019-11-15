import random
x = [random.randint(0,100) for i in range(20)]#生成随机数
print(x)
y=x[::2]#使用切片间隔，选取偶数下标元素
y.sort()#对偶数下标元素进行排序
y.reverse()#对已排序好的偶数下标元素进行反向排序
x[::2]=y#将值赋予原列表
print(x)
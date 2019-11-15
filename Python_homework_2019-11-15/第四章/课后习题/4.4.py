import random
x = [random.randint(0,100) for i in range(50)]#生成随机数
print(x)#输出
i = len(x)-1
while i>=0:
    if x[i]%2==1:#筛选并删除
        del x[i]
    i-=1
print(x)
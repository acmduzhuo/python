# sum = 0
# for i in  range(65)#从0到64
#     sum += 2**i ##累加
# print(sum)


lis = [2**i for i in range(65)] #列表推导式 将幂计入列表
print(sum(lis))
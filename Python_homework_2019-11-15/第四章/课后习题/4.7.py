# x = []
# for i in range(1, 100):
#     if i%2 == 1:
#         x.append(i)
# print(x)
# print(sum(x))

x = [i for i in range(1, 100)]
for i in x:
    if i%2==0:
        x.remove(i)
print(x)
print(sum(x))

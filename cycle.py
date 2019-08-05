# print(1 + 2 + 3);
# names = ['Michael', 'Bob', 'Tracy']
# for a in names:
#     print(a)
# a = [1, 2, 3, 4, 5, 6]
# for b in a:
#     print(b)
# x = 2
# x = x + 2
# print(x)
# sum = 0
# n = input()
# nn = int(n)
# for x in range(nn+1):
#     sum = sum + x
# print(sum)
# print(list(range(3)))
#sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
#     print(sum)
# L = ['Bart', 'Lisa', 'Adam']
# n = 0
# while n < 3:
#     print('Hello,', L[n])
#     n = n + 1
# n = 1
# while n <= 10:
#     if n > 5:
#         break
#     print(n)
#     n = n + 1
# print('End')#注意纵向排列，它决定着嵌套关系
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
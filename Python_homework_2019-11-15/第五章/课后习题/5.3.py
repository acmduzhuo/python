def count_all(str):
    res = [0, 0, 0, 0]
    for i in str:
        if i.islower():
            res[0] += 1
        elif i.isupper():
            res[1] += 1
        elif i.isdigit():
            res[2] += 1
        else:
            res[3] += 1
    return ('A-Z', res[1]), ('a-z', res[0]), ('0-9', res[2]), ('others', res[3])
str = input()
print(count_all(str))
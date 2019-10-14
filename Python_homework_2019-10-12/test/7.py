result = []
for x in [1, 2, 3]:#寻找x
    for y in [3, 1, 4]:#寻找y
        if x == 1:#限制x
            if x != y:#限制y
                result.append((x, y))
print(result)
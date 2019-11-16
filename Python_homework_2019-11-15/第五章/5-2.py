def demo(s):#接受字符串，返回元组，第一个元素为大写字母个数，第二个为小写
    result=[0,0]
    for ch in s:
        if ch.islower():
            result[1] += 1
        elif ch.isupper():
            result[0] += 1
    return tuple(result)
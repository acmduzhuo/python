from random import randint  # 24点游戏
from itertools import permutations

exps = ('((%s%s%s)%s%s)%s%s', '(%s%s%s)%s(%s%s%s)', '(%s%s(%s%s%s)%s%s)', '%s%s((%s%s%s)%s%s)', '%s%s(%s%s(%s%s%s))')
ops = r'+-*/'


def test24(v):
    result = []

    def check(exp):
        try:
            return int(eval(exp)) == 24
        except:
            return False

    for a in permutations(v):
        t = [exp % (a[0], op1, a[1], op2, a[2], op3, a[3]) for op1 in ops for op2 in ops for op3 in ops for exp in exps
             if check(exp % (a[0], op1, a[1], op2, a[2], op3, a[3]))]
        if t:
            result.append(t)
        return result


for i in range(20):
    print('=' * 20)
    lst = [randint(1, 14) for j in range(4)]
    r = test24(lst)
    if r:
        print(r)
    else:
        print('NO answer for ', lst)
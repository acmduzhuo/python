from random import randint#猜数字
def guess (maxvalue=100,maxtimes=5):
    value=randint(1,maxvalue)
    for i in range (maxtimes):
        prompt='Start to guess:'if i==0 else 'Guess again:'
        try:
            x=int(input(prompt))
        except:
            print('Must input an integer between 1 and',maxvalue)
        else:
            if x==value:
                print('congratulations')
                break
            elif x>value:
                print('too big')
            else:
                print('too little')
    else:
        print('gave over')
        print('the value is',value)
guess(5)
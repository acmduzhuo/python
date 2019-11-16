def crypt(source,key):
    from itertools import cycle
    result=''
    temp=cycle(key)
    for ch in source:
        result=result+chr(ord(ch)^ord(next(temp)))
    return result
source='Shandong Institute of Bussiness and Technology'
key='Dong'

print('before encrypted:'+source)
encrypted=crypt(source,key)
print('after encrypted:'+encrypted)
decrypted=crypt(encrypted,key)
print('after decrypted:'+decrypted)
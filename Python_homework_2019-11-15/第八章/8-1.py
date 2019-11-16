import re
telnumber='''suppose my phone No is 0535-1234567,yours is 010-12345678,his is 025-87654321'''
pattern=re.compile(r'(\d{3,4})-(\d{7,8})')
index=0
while True:
    matchresult=pattern.search(telnumber,index)
    if not matchresult:
        break
    print('-'*30)
    print('sucess:')
    for i in range(3):
        print('searched content:',matchresult.group(i),'start from:',matchresult.start(i),'End at:',matchresult.end(i),'Its span is:',matchresult.span(i))
    index=matchresult.end(2)

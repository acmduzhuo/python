def hannoi(num,src,dst,temp=None):#汉诺塔
    global times
    assert type(num)==int,'num must be an integer'
    assert num>0,'num must >0'
    if num==1:
        print('The {0} Times move:{1}==>{2}'.format(times,src,dst))
        times +=1
    else:
        hannoi(num-1,src,temp,dst)
        hannoi(1,src,dst)
        hannoi(num-1,temp,dst,src)
times=1
hannoi(3,'A','C','B')
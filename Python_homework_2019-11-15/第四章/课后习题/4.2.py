years = int(input('请输入你要查询的年份:'))  #输入你要查询的年份
if ((years%4==0 and years%100!=0) or (years%400==0)):  # 判断是否是闰年
    print (years,"是闰年")
else:
    print('不是闰年')
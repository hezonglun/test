#分支结构

#单分支结构
#取款程序
money=1000      #余额
s=int(input('请输入取款金额\n'))     #取款金额
if money>=s:                    #判断余额是否充足
    money=money-s
    print('取款成功，余额为:',money)


#双分支结构 if...else
#从键盘录入一个整数，判断是奇数还是偶数
num=int(input('请输入一个整数\n'))
if num%2==0:
    print(num,'是偶数')
else:
    print(num,'是奇数')


#多分支结构
"""从键盘录入一个整数 成绩
90-100 A
80-89  B
70-79  C
60-69  D
0-59   E
小于0或大于100 为非法数据（不在成绩的有限范围）
"""
score=int(input('请输入一个成绩:'))
if 90<=score<=100:
    print('A级')
elif 80<=score<=89:
    print('B级')
elif 70<=score<=79:
    print('C级')
elif 60<=score<=69:
    print('D级')
elif 0<=score<=59:
    print('E级')
else:
    print('非法数据，请重新输入')


#嵌套if的使用
'''
会员 >=200     8折
--- >=100     9折
---------     不打折
非会员  >=200  打9.5折
------------  不打折
'''
answer=input('您是会员吗？y/n')
money=int(input('请输入购物金额'))
if answer=='y':     #会员
    if money>=200:
        money=money*0.8
        print('打8折，付款金额为:', money)
    elif money>=100:
        money=money*0.9
        print('打9折，付款金额为:', money)
    else:
        print('不打折，付款金额为:', money)
else:               #非会员
    if money>=200:
        money=money*0.95
        print('打95折，付款金额为:',money)
    else:
        print('不打折，付款金额为:', money)


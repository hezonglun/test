#pass语句
money=int(input('请输入金额'))
if money >= 200:
   pass
elif money >= 100:
    money = money * 0.9
    print('打9折，付款金额为:', money)
else:
    print('不打折，付款金额为:', money)


#任何对象均有布尔值；可判断对象是否为空
age=int(input('请输入你的年龄'))
if age:
    print(age)
else:
    print('年龄为:',age)